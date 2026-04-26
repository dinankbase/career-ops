# Mode: interview -- Interview Preparation System

When the candidate says `/career-ops interview [company]`, generate a complete interview preparation package.

**Input:** Company name (required), role title (optional), interview round (optional: `recruiter`, `hm`, `cd`, `vp`, `mock`, `debrief`)

**Sub-modes:**
- No round specified: generate FULL prep package (Steps 1-5)
- `recruiter` / `hm` / `cd` / `vp`: generate round-specific Q&A only (Step 5)
- `mock`: run mock interview simulation (Step 6)
- `debrief`: run post-interview debrief (Step 7)

---

## Step 1: Load Context

Read these files before generating anything:
1. `cv.md` -- candidate background and portfolio
2. `modes/_profile.md` -- archetypes, reframe bank, exit narrative
3. `config/profile.yml` -- personal details, comp targets, gap framing
4. `interview-prep/story-bank.md` -- accumulated stories (if exists)
5. `interview-prep/reframe-bank.md` -- career transition reframes (if exists)
6. Search `reports/` for existing report on this company (if any)

---

## Step 2: Company Research

### 2a. General Research (WebSearch)
- Company overview: what they do, size, funding, revenue
- Recent news (last 6 months): hires, launches, pivots, funding
- Culture signals: Glassdoor reviews, remote policy, team structure
- Growth strategy: where are they investing, expanding, hiring

### 2b. Creative-Specific Research

**If the company is DTC/ecom/agency (most target roles):**
- Use `/browser` skill to check Meta Ad Library for their current ads
  - What formats are they running? (static, video, UGC, carousel)
  - What hooks are they using?
  - How many active ads? (signals creative testing velocity)
  - What's the visual style? (polished vs raw/UGC)
- Check TikTok Creative Center if relevant
- Look for their landing pages, funnels, email sequences (sign up for their list if DTC)

**If the company is an agency:**
- Who are their clients? What verticals?
- What case studies do they publish?
- What's their creative philosophy? (check their site, blog, social)

### 2c. Growth Strategy Research (for VP/CMO rounds)
- If public: check 10-K filing or investor presentations for growth levers
- If funded: check Crunchbase for funding stage, investors, growth trajectory
- Identify: where is most revenue coming from? Where are they deploying money?
- How does the role being hired for fit into their growth strategy?

### 2d. Creative Team Structure
- WebSearch + LinkedIn: who leads creative? Creative Director, Head of Growth, CMO?
- How big is the creative team?
- In-house vs agency vs hybrid?
- Who would the candidate likely report to?

---

## Step 3: Creative Audit

Generate a structured Creative Audit of the company's current ad creative. This is interview collateral the candidate can reference or present.

**NOTE:** This is scaffolding. The automated analysis covers structural elements and strategic gaps. For high-priority targets, the candidate should layer their own DR judgment on top (hook quality, angle freshness, pacing, niche-specific insights).

### A. Audience
- Who does the company target? (demographics, psychographics)
- What buyer personas appear in their marketing?
- What awareness level are they targeting? (Schwartz's 5 levels: Unaware, Problem-Aware, Solution-Aware, Product-Aware, Most Aware)

### B. Problem
- What pain does the product/service solve?
- How do customers describe the problem in their own words? (check reviews, testimonials)
- What's the emotional trigger behind the purchase?

### C. Current Creative (from Ad Library research)
- **Formats:** What are they running? (static, video, UGC, carousel, story)
- **Hooks:** What hook types? (pattern interrupt, bold claim, story, question, demonstration, problem call-out)
- **Mechanism:** Do they articulate a unique mechanism? Is it differentiated?
- **Proof stack:** Testimonials, data, authority, before/after, demonstration?
- **CTA:** Clear? Urgent? What's the offer structure?
- **Volume:** How many active ads? (low = not testing enough, high = serious about creative)

### D. Strategic Gaps (what's missing or weak)
- What angles are they NOT exploring?
- What formats are they not using? (if no video, that's a gap. If no UGC, that's a gap.)
- Are they only targeting one awareness level?
- Is the proof stack thin?
- Compliance issues? (especially for health/supplement/finance)

### E. Your Hypothesis
Draft 2-3 spec ad concepts the candidate would test:

For each concept:
1. **Angle:** What's the story/perspective?
2. **Hook:** First 3 seconds (video) or headline (static)
3. **Body:** Key proof points and mechanism
4. **CTA:** What action, what offer
5. **Why this would work:** Tie to a gap identified in section D
6. **Format:** Static, video, UGC-style, carousel

**Present as a brief, not finished copy.** The candidate produces the actual creative assets.

### F. DR Analysis Checklist
Flag for the candidate to assess manually on high-priority targets:

- [ ] Awareness level targeting correct for the funnel stage?
- [ ] Hook is stopping thumbs in the first 1-3 seconds?
- [ ] Mechanism is unique and differentiated?
- [ ] Proof stack is sufficient (3+ types of proof)?
- [ ] CTA matches the awareness level (not asking for too much too soon)?
- [ ] Compliance clean? (no illegal health/financial claims)
- [ ] Testing velocity sufficient? (enough variations to learn)
- [ ] Platform-specific best practices followed? (aspect ratios, safe zones, captions)

---

## Step 4: 90-Day Creative Plan

Generate a 90-Day Creative Plan the candidate can present in interviews. Adapted from the Territory Plan framework, customized for the specific company and role.

### Month 1: Learn & Audit (Days 1-30)
1. **Company deep dive:** Product knowledge, brand guidelines, existing creative library, past performance data
2. **Creative audit:** Review all active ads, identify top performers, understand what's working and why
3. **Customer research:** Review mining (Amazon, Reddit, Trustpilot), customer interviews/surveys, competitor analysis
4. **Tool proficiency:** Get up to speed on company's creative stack (Motion, Triple Whale, Foreplay, internal tools)
5. **First tests:** Launch 3-5 initial creative tests based on audit findings
   - Target: [X] hooks x [Y] body variations x [Z] CTAs = [total] ad combinations
   - Establish baseline metrics (hook rate, CTR, CPA)

### Month 2: Test & Scale (Days 31-60)
1. **Scale winners:** Take top-performing concepts from Month 1, create variations
2. **Modular production:** Build a system for rapid creative iteration (hook libraries, body templates, CTA variations)
3. **New angles:** Introduce 2-3 new angles based on deeper customer research
4. **Platform expansion:** If only on Meta, test TikTok or YouTube. If only static, test video.
5. **Reporting:** Establish weekly creative performance reporting cadence
   - Target: [X] new creatives per week, [Y]% improvement in primary KPI

### Month 3: Systematize (Days 61-90)
1. **Creative testing system:** Documented process from hypothesis to launch to analysis
2. **Brief templates:** Standardized creative briefs for internal team or external creators
3. **Performance dashboard:** Clear visibility into creative-level ROAS, hook rates, fatigue signals
4. **Content pipeline:** Sustainable production calendar with testing velocity targets
5. **First case study:** Document one winning creative with before/after data
   - Target: demonstrable impact on [primary KPI], creative testing velocity of [X]/week

**Customize the plan for the specific role:**
- If SDR/junior: focus on execution velocity and learning
- If mid-level strategist: focus on owning the testing roadmap
- If senior/lead: focus on building the system and mentoring

---

## Step 5: Interview Q&A Preparation

Generate role-specific interview prep organized by round.

### Round 1: Recruiter Screen

**Format:** 15-30 min phone/video call. Screening for basics, culture fit, salary alignment.

**"Tell me about yourself" (2-3 min):**
Use Pull-Bridge-Proof from `_profile.md`. Structure:
1. Where I am now and what I'm focused on (Pull - 30 sec)
2. How I got here - the logical progression (Bridge - 60 sec)
3. What I've built that proves I can do this (Proof - 60 sec)

**"Why are you making this change?"**
> Read gap framing from `config/profile.yml`. Use the Pull-Bridge-Proof structure. Lead with what excites you about creative strategy. Mention the family situation briefly (one sentence). Pivot to portfolio and skills built. Never mention burnout, quota, or dissatisfaction.

**"What are your salary expectations?"**
> Read comp targets from `config/profile.yml`. Use the negotiation script from `_profile.md`.

**"What do you know about us?"**
> Use company research from Step 2. Find one original insight (CEO podcast, recent news, product angle). If you teach the interviewer something about their own company, they won't forget you.

**Questions to ask the recruiter:**
- "What does a typical week look like for this role?"
- "How is the creative team structured?"
- "What's the interview process from here?"

---

### Round 2: Hiring Manager / Creative Director

**Format:** 30-60 min. Portfolio review, creative thinking assessment, culture fit.

**Portfolio presentation (8-12 min):**
- Present 4-6 pieces using: one-line setup, idea, process, outcome
- Include spec work AND explain the strategic thinking behind it
- For each piece, articulate: "I chose this angle because [insight], and here's how I'd test it"
- Show the messy bits: research notes, rejected ideas, iteration process

**Introducing the Creative Audit:**
Two options (adapted from Cocoon 5-P Matrix delivery):
1. 2 hours before the call, email: "I put together some thoughts on your current creative. Mind if we take 5 min to go over it?"
2. During the interview: "I spent some time looking at your ads in Meta Ad Library. I have some observations if you're interested."

Then present the Creative Audit from Step 3. Keep it to 5 minutes. Ask for their reaction.

**Technical questions to prepare for:**

| Question | Framework for answering |
|----------|------------------------|
| "Walk me through your creative testing process" | Hypothesis > Brief > Produce > Launch > Analyze > Iterate. Reference the 7-step flywheel. |
| "How do you come up with new ad angles?" | Customer research (review mining, Reddit, competitor analysis) > insight extraction > angle development > hook variations |
| "What's the difference between brand creative and performance creative?" | Brand encodes meaning and memory. Performance converts intent into action. Both matter, but measurement is different. |
| "How do you know when an ad is fatigued vs audience is saturated?" | Fatigue: CTR drops while impressions stay stable. Saturation: frequency climbs, CPM increases. Different solutions for each. |
| "What metrics do you track?" | Hook rate (3-sec view %), hold rate (15-sec), CTR, CPA, ROAS. Priority depends on funnel stage. |
| "Why should we hire someone with no agency experience?" | Use reframe from _profile.md. Lead with what you bring that traditional candidates don't: buyer psychology depth, full-stack execution, analytical thinking. Don't be defensive. |

**The Soft Close (do this at the end of EVERY interview):**
> "When you think of your best-performing creative strategist, what qualities or traits do they have that consistently set them apart?"

Whatever they answer, follow up with:
> "I hope I've been able to demonstrate some of those today. Is there anything that gives you hesitation about my fit, or concerns I can address?"

This accomplishes 5 things:
1. Shows you ask hard questions
2. Primes them by associating you with their top performer
3. Shows you seek objections rather than avoid them
4. Treats the interview like a sales call (asking for next steps)
5. Executes a soft close

**Questions to ask the hiring manager:**
- "What would success look like in the first 90 days?"
- "What's your biggest creative challenge right now?"
- "How do you decide what to test next?"
- "What tools does the team use for creative analytics?"

---

### Round 3: VP / CMO / Head of Growth

**Format:** 30-45 min. Big picture thinking, strategic alignment, culture.

**Framework (adapted from Cocoon VP Talk Track):**

At the start, set the frame:
> "Before we start, would it be ok if we saved 10-15 minutes at the end? I want to make sure this is the right fit on both sides, so I have a few questions about where [Company] is heading."

Let them run their interview. Then 10-15 min before the end, take back control:

> "Usually when I speak with leaders in growth, they tell me their work is about orchestrating sustainable revenue. Is that fair here too?"

Then share your research:
> "I researched [Company] and learned [mission/market position]. Based on [10-K/funding/public data], it looks like the growth strategy has [X] main levers: [list them]. How am I doing so far?"

**Key questions to ask (growth-focused):**
1. "How much of growth is coming from new customer acquisition vs expansion?"
2. "Where does creative fit in that equation? Is it a primary growth lever or a support function?"
3. "Outside of the creative team, what other investments are you making to drive growth?"
4. "Where do you see the most opportunity over the next 2-3 years?"
5. "What would make you feel confident about the creative program 12 months from now?"

**Why this works for creative strategy candidates:**
- Shows you think like a business person, not just a creative
- Your MSc Finance background makes this natural and credible
- Demonstrates you understand where your work fits in the revenue model
- Positions you as someone who can speak to leadership, not just execute

---

### Universal Hard Questions (prepare for any round)

| Question | How to answer |
|----------|---------------|
| "Tell me about your biggest failure" | Pick a sales failure, extract 2-3 learnings, show how you applied them. Keep it brief. Don't pick something that makes you look incompetent. |
| "Why are you leaving sales?" | NEVER say you're "leaving" sales. Say you're "moving toward" creative strategy. Use Pull-Bridge-Proof. |
| "Where do you see yourself in 5 years?" | "Year 1: learn the craft at speed, prove I can ship winning creative. Year 2-3: own the creative testing roadmap for multiple brands/products. Year 4-5: creative leadership, building and mentoring a team." |
| "What makes you the right person?" | Skills (sales psychology + full-stack creative + analytical mind) + Attitude (self-starter, coachable, data-driven) + Proof (portfolio). |
| "You don't have agency/creative experience" | "I don't have the title yet, but I have the skills. [Reference reframe bank]. And I bring something most creative candidates don't: [unique value prop]." |

---

## Step 6: Mock Interview Simulation

**Trigger:** `/career-ops interview mock [company] [round]`

### How it works:
1. Load all context from Steps 1-5 (company research, Q&A prep, reframe bank)
2. Announce: "Starting mock interview. I'll play the [round type] interviewer for [Company]. Answer as you would in a real interview. I'll give feedback after each answer. Say 'stop' to end."
3. Ask questions appropriate to the round:
   - **Recruiter:** 5-7 questions, screening style, 2-3 min per answer max
   - **HM/CD:** 6-8 questions, deeper, include portfolio discussion, technical questions
   - **VP/CMO:** 4-6 questions, strategic, include the reverse interview segment
4. After each answer, provide feedback:
   - Was it too long or too short? (recruiter answers should be 30-90 sec, HM 1-3 min)
   - Did you use proof points? Which ones worked?
   - Did you sound defensive or confident?
   - Did you use the reframes naturally?
   - Specific improvements for next time
5. At the end, provide overall assessment:
   - Strongest answers
   - Weakest answers (drill these again)
   - Body language / energy notes (based on word choice and pacing)
   - Ready for real interview? Yes / Almost / Need more practice

### Curveball questions to throw:
- "I see you were in sales for 6 years. Isn't this just a career crisis?"
- "Your portfolio is all spec work. How do I know this works in the real world?"
- "We need someone who can start contributing day one. You'd need months of ramp-up."
- "Why didn't you just go into marketing at your sales company?"
- "Your gap is 6 months. What were you really doing?"

These are designed to pressure-test the candidate's composure and reframing ability.

---

## Step 7: Post-Interview Debrief

**Trigger:** `/career-ops interview debrief [company]`

### Capture:
Ask the candidate:
1. "What questions did they ask?"
2. "What went well? Which answers felt strong?"
3. "What stumped you or felt weak?"
4. "What was the vibe? Did they seem interested?"
5. "Did they mention next steps or timeline?"

### Process:
1. For each question asked: assess the candidate's reported answer, suggest improvements
2. If any new STAR/SOAR stories emerged, add them to `interview-prep/story-bank.md`
3. If any reframes worked well (or failed), note in `interview-prep/reframe-bank.md`
4. Update `data/applications.md` status if appropriate (Evaluated -> Interview)

### Generate follow-up email:
Draft a thank-you email within 24 hours:
- Reference something specific from the conversation (shows you were listening)
- Reinforce one key point about your fit
- Keep it short (3-4 sentences)
- If you presented the Creative Audit, reference it: "Happy to refine those concepts based on our conversation"

**Template:**
```
Subject: Thanks for the conversation, [Name]

Hi [Name],

Really enjoyed our conversation about [specific topic discussed]. Your point about [something they said] got me thinking about [relevant insight].

I'm excited about the opportunity to [specific contribution you'd make]. [Reference Creative Audit or portfolio piece if shared.]

Looking forward to next steps.

Best,
Daniel
```

---

## Output Format

### Full prep (no round specified):
Generate sections in this order, each clearly headed:
1. Company Research Summary (from Step 2)
2. Creative Audit (from Step 3) -- save to `interview-prep/{company-slug}-audit.md`
3. 90-Day Creative Plan (from Step 4)
4. Q&A Prep (from Step 5, all rounds)
5. "Next: run `/career-ops interview mock [company] [round]` to practice"

### Round-specific:
Generate only the Q&A for that round, with company context.

### Mock:
Interactive simulation, no file output.

### Debrief:
Capture + follow-up email + file updates.
