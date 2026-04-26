#!/usr/bin/env python3
"""
generate-pdf.py -- HTML to PDF via WeasyPrint

Usage:
    python generate-pdf.py <input.html> <output.pdf> [--format=letter|a4]

Requires: weasyprint >= 60.0
    pip install weasyprint

Replaces the previous Playwright-based generate-pdf.mjs with a lighter
dependency that doesn't require a full browser installation.
"""

import sys
import re
import os
from pathlib import Path

try:
    import weasyprint
except ImportError:
    print("ERROR: weasyprint not installed. Run: pip install weasyprint", file=sys.stderr)
    sys.exit(1)


def normalize_text_for_ats(html: str) -> tuple[str, dict[str, int]]:
    """
    Normalize text for ATS compatibility by converting problematic Unicode.

    ATS parsers and legacy systems often fail on em-dashes, smart quotes,
    zero-width characters, and non-breaking spaces. These cause mojibake,
    parsing errors, or display issues.

    Only touches body text - preserves CSS, JS, tag attributes, and URLs.
    Returns (normalized_html, replacement_counts).
    """
    replacements: dict[str, int] = {}

    def bump(key: str, count: int = 1):
        replacements[key] = replacements.get(key, 0) + count

    # Mask <style> and <script> blocks
    masks: list[str] = []

    def mask_block(match):
        token = f"\x00MASK{len(masks)}\x00"
        masks.append(match.group(0))
        return token

    masked = re.sub(r'<(style|script)\b[^>]*>[\s\S]*?</\1>', mask_block, html, flags=re.IGNORECASE)

    # Process text between tags only
    result = []
    i = 0
    while i < len(masked):
        lt = masked.find('<', i)
        if lt == -1:
            result.append(sanitize_text(masked[i:], bump))
            break
        result.append(sanitize_text(masked[i:lt], bump))
        gt = masked.find('>', lt)
        if gt == -1:
            result.append(masked[lt:])
            break
        result.append(masked[lt:gt + 1])
        i = gt + 1

    out = ''.join(result)

    # Restore masked blocks
    for idx, block in enumerate(masks):
        out = out.replace(f"\x00MASK{idx}\x00", block)

    return out, replacements


def sanitize_text(text: str, bump) -> str:
    """Replace problematic Unicode characters with ASCII equivalents."""
    if not text:
        return text

    t = text
    # Em-dash
    count = t.count('\u2014')
    if count:
        bump('em-dash', count)
        t = t.replace('\u2014', '-')
    # En-dash
    count = t.count('\u2013')
    if count:
        bump('en-dash', count)
        t = t.replace('\u2013', '-')
    # Smart double quotes
    for ch in '\u201c\u201d\u201e\u201f':
        count = t.count(ch)
        if count:
            bump('smart-double-quote', count)
            t = t.replace(ch, '"')
    # Smart single quotes
    for ch in '\u2018\u2019\u201a\u201b':
        count = t.count(ch)
        if count:
            bump('smart-single-quote', count)
            t = t.replace(ch, "'")
    # Ellipsis
    count = t.count('\u2026')
    if count:
        bump('ellipsis', count)
        t = t.replace('\u2026', '...')
    # Zero-width characters
    for ch in '\u200b\u200c\u200d\u2060\ufeff':
        count = t.count(ch)
        if count:
            bump('zero-width', count)
            t = t.replace(ch, '')
    # Non-breaking space
    count = t.count('\u00a0')
    if count:
        bump('nbsp', count)
        t = t.replace('\u00a0', ' ')

    return t


def generate_pdf():
    args = sys.argv[1:]

    input_path = None
    output_path = None
    fmt = 'a4'

    for arg in args:
        if arg.startswith('--format='):
            fmt = arg.split('=', 1)[1].lower()
        elif input_path is None:
            input_path = arg
        elif output_path is None:
            output_path = arg

    if not input_path or not output_path:
        print('Usage: python generate-pdf.py <input.html> <output.pdf> [--format=letter|a4]', file=sys.stderr)
        sys.exit(1)

    input_path = Path(input_path).resolve()
    output_path = Path(output_path).resolve()

    valid_formats = ('a4', 'letter')
    if fmt not in valid_formats:
        print(f'Invalid format "{fmt}". Use: {", ".join(valid_formats)}', file=sys.stderr)
        sys.exit(1)

    print(f'Input:  {input_path}')
    print(f'Output: {output_path}')
    print(f'Format: {fmt.upper()}')

    # Read HTML
    html = input_path.read_text(encoding='utf-8')

    # Resolve font paths relative to this script's fonts/ directory
    script_dir = Path(__file__).resolve().parent
    fonts_dir = script_dir / 'fonts'
    fonts_uri = fonts_dir.as_uri()

    # Replace relative font paths with absolute file:// URIs
    html = re.sub(
        r"url\(['\"]?\./fonts/",
        f"url('{fonts_uri}/",
        html
    )

    # ATS text normalization
    html, replacements = normalize_text_for_ats(html)
    total_replacements = sum(replacements.values())
    if total_replacements > 0:
        breakdown = ', '.join(f'{k}={v}' for k, v in replacements.items())
        print(f'ATS normalization: {total_replacements} replacements ({breakdown})')

    # Inject @page CSS for format and margins
    if fmt == 'letter':
        page_size = '8.5in 11in'
    else:
        page_size = 'A4'

    page_css = f"""
    @page {{
        size: {page_size};
        margin: 0.6in;
    }}
    """

    # Create output directory if needed
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Generate PDF with WeasyPrint
    # base_url set to input file's directory for any relative resources
    html_doc = weasyprint.HTML(
        string=html,
        base_url=str(input_path.parent)
    )

    css = weasyprint.CSS(string=page_css)

    pdf_bytes = html_doc.write_pdf(stylesheets=[css])

    # Write PDF
    output_path.write_bytes(pdf_bytes)

    # Count pages (approximate from PDF structure)
    pdf_text = pdf_bytes.decode('latin-1', errors='replace')
    page_count = len(re.findall(r'/Type\s*/Page[^s]', pdf_text))

    size_kb = len(pdf_bytes) / 1024

    print(f'PDF generated: {output_path}')
    print(f'Pages: {page_count}')
    print(f'Size: {size_kb:.1f} KB')


if __name__ == '__main__':
    generate_pdf()
