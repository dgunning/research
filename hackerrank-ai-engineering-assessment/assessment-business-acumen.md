# Business Acumen Skills Assessment

**Assessment Area**: ROI, Strategic Planning, and Business Impact
**Target Role**: Principal AI Engineer at Thomson Reuters
**Date**: November 2025

## Purpose

This assessment evaluates your business acumen - your ability to connect technical work to business outcomes, think strategically about technology investments, and communicate value to stakeholders. At the Principal level, you're expected to influence not just technical decisions but business strategy.

---

## Assessment Framework

**Scoring Guide:**
- **5 - Expert**: Drives business strategy, quantifies impact, shapes roadmaps
- **4 - Advanced**: Strong business sense, influences decisions, ties work to outcomes
- **3 - Proficient**: Understands business context, can articulate value
- **2 - Developing**: Growing awareness, learning business thinking
- **1 - Awareness**: Primarily technical focus, limited business perspective

---

## Part 1: Understanding Business Value

### 1.1 ROI & Value Creation

**Self-Assessment Questions:**

1. **Financial Metrics** (Score: ___/5)
   - Can you calculate ROI for technology investments?
   - Do you understand revenue, profit, margin, CAC, LTV?
   - Can you build business cases for technical projects?
   - Do you know how to measure AI/ML ROI?

2. **Value Drivers** (Score: ___/5)
   - Can you identify what drives value in a business?
   - Do you understand cost reduction vs. revenue growth?
   - Can you explain time-to-market importance?
   - Do you know how to quantify quality improvements?

3. **Cost-Benefit Analysis** (Score: ___/5)
   - How do you evaluate build vs. buy decisions?
   - Can you assess total cost of ownership (TCO)?
   - Do you understand opportunity cost?
   - Can you prioritize investments by ROI?

**Business Fundamentals Check:**

**ROI Calculation:**
```
ROI = (Benefit - Cost) / Cost × 100%

Example: ML project costs $500K, saves $2M/year
ROI = ($2M - $500K) / $500K = 300%
Payback period = 3 months
```

**Calculate ROI for this scenario:**
```
Scenario: CoCounsel contract review feature
- Development cost: $1M (5 engineers, 6 months)
- Infrastructure: $200K/year
- Expected impact: 500 law firms × $10K/year subscription = $5M/year
- Customer acquisition cost: $100K
- Gross margin: 70%

Year 1 ROI: _______________
3-Year ROI: _______________
```

**Your Calculation:**
[Show your work]

**Expected Answer:**
```
Year 1:
- Cost: $1M dev + $200K infra + $100K CAC = $1.3M
- Revenue: $5M × 70% margin = $3.5M
- ROI: ($3.5M - $1.3M) / $1.3M = 169%

3-Year:
- Cost: $1M + ($200K × 3) = $1.6M
- Revenue: ($5M × 70%) × 3 = $10.5M
- ROI: ($10.5M - $1.6M) / $1.6M = 556%
```

---

### 1.2 Business Models

**Self-Assessment Questions:**

1. **Revenue Models** (Score: ___/5)
   - Do you understand SaaS business model?
   - Can you explain subscription vs. usage-based pricing?
   - Do you know about enterprise vs. self-serve models?
   - Can you discuss unit economics?

2. **Pricing Strategy** (Score: ___/5)
   - How do you price AI/ML features?
   - What's value-based vs. cost-plus pricing?
   - How do you think about freemium models?
   - What's the role of price experimentation?

3. **Customer Economics** (Score: ___/5)
   - Can you explain CAC (Customer Acquisition Cost)?
   - Do you understand LTV (Lifetime Value)?
   - Can you calculate LTV:CAC ratio?
   - Do you know churn and retention metrics?

**Thomson Reuters Business Model:**

**Westlaw (Core Product):**
- Model: _______________
- Pricing: _______________
- Key metrics: _______________
- Moat: _______________

**CoCounsel (New Product):**
- Model: _______________
- Pricing: _______________
- Go-to-market: _______________
- Differentiation: _______________

**Reference Answers:**
- Westlaw: SaaS subscriptions, seat-based + usage, renewal rate, content & network effects
- CoCounsel: Add-on to Westlaw, query-based pricing, existing customer upsell, AI capabilities

---

### 1.3 Metrics & KPIs

**Self-Assessment Questions:**

1. **Product Metrics** (Score: ___/5)
   - What metrics matter for SaaS products?
   - How do you measure user engagement?
   - What are leading vs. lagging indicators?
   - How do you define success for AI features?

2. **AI-Specific Metrics** (Score: ___/5)
   - How do you measure AI feature adoption?
   - What's the relationship between model quality and business outcomes?
   - How do you quantify AI's impact on user productivity?
   - How do you measure AI ROI over time?

**Scenario 1: Define Success Metrics**

```
You're launching CoCounsel's new "Contract Analysis" feature.

Define metrics for:
1. Product success
2. Technical success
3. Business success
4. User success
```

**Your Metrics:**

**Product Metrics:**
- _______________
- _______________
- _______________

**Technical Metrics:**
- _______________
- _______________
- _______________

**Business Metrics:**
- _______________
- _______________
- _______________

**User Metrics:**
- _______________
- _______________
- _______________

**Expected Metrics:**

**Product:**
- Adoption rate (% of users trying feature)
- Engagement (queries per user per week)
- Retention (D7, D30 return rates)
- Feature satisfaction (NPS, CSAT)

**Technical:**
- Latency (p95 response time)
- Accuracy (precision, recall, F1)
- Availability (uptime %)
- Error rate

**Business:**
- Revenue impact (incremental ARR)
- Cost per query
- Conversion rate (trial → paid)
- Expansion revenue

**User:**
- Time saved per contract
- User satisfaction score
- Task completion rate
- Accuracy of AI outputs (user validation)

---

## Part 2: Strategic Thinking

### 2.1 Technical Strategy

**Self-Assessment Questions:**

1. **Vision & Roadmap** (Score: ___/5)
   - Can you develop multi-year technical strategy?
   - How do you align technical roadmap with business goals?
   - How do you balance innovation with execution?
   - How do you communicate strategy to stakeholders?

2. **Prioritization** (Score: ___/5)
   - How do you prioritize technical investments?
   - What frameworks do you use (RICE, impact/effort, etc.)?
   - How do you say no to good ideas?
   - How do you balance short-term vs. long-term?

3. **Make vs. Buy** (Score: ___/5)
   - How do you evaluate build vs. buy vs. partner?
   - What factors drive the decision?
   - How do you assess strategic value vs. commodity?
   - How do you handle technical debt in strategy?

**Scenario 2: Strategic Decision**

```
Thomson Reuters AI Team: Strategic Choice

Background:
- Currently using OpenAI, Anthropic, Google LLMs via APIs
- Cost: $10M/year and growing
- Quality: Good but limited control
- Latency: Dependent on vendor SLAs

Options:
A) Status quo (continue with API providers)
B) Build own LLM from scratch (Llama base, fine-tune)
C) Hybrid (self-host open models for some use cases, APIs for others)
D) Exclusive partnership with one provider (negotiate better terms)

Evaluate each option strategically.
```

**Your Analysis:**

**Option A: Status Quo**
- Pros: _______________
- Cons: _______________
- Cost: _______________
- Risk: _______________
- Strategic fit: _______________

**Option B: Build Own LLM**
- Pros: _______________
- Cons: _______________
- Cost: _______________
- Risk: _______________
- Strategic fit: _______________

**Option C: Hybrid**
- Pros: _______________
- Cons: _______________
- Cost: _______________
- Risk: _______________
- Strategic fit: _______________

**Option D: Exclusive Partnership**
- Pros: _______________
- Cons: _______________
- Cost: _______________
- Risk: _______________
- Strategic fit: _______________

**Recommendation:** _______________

**Expected Strategic Analysis:**

**Option A (Status Quo):**
- Pros: No change, proven, access to best models
- Cons: High cost, vendor lock-in, limited differentiation
- Strategic: Acceptable short-term, risky long-term

**Option B (Build Own):**
- Pros: Control, cost savings at scale, differentiation, IP
- Cons: High upfront cost ($10M+), 12-18 month timeline, expertise needed, may lag SOTA
- Strategic: Only if LLM is core differentiator and at massive scale

**Option C (Hybrid):**
- Pros: Optimize cost/quality tradeoff, flexibility, reduce vendor risk
- Cons: Complexity, need to manage both, routing logic
- Strategic: Best balance for current stage

**Option D (Partnership):**
- Pros: Better pricing, closer relationship, roadmap influence
- Cons: All eggs in one basket, vendor leverage
- Strategic: Only if vendor's roadmap aligns perfectly

**Likely Best Choice: Option C (Hybrid)**
- Immediate cost savings (30-40%)
- Maintain quality for critical use cases
- Build expertise gradually
- Reduce strategic risk

---

### 2.2 Competitive Strategy

**Self-Assessment Questions:**

1. **Competitive Analysis** (Score: ___/5)
   - Do you understand Thomson Reuters' competitive landscape?
   - Can you analyze competitors' technical strategies?
   - How do you identify competitive advantages?
   - How do you track competitive threats?

2. **Differentiation** (Score: ___/5)
   - What makes TR's AI unique?
   - How do you build sustainable competitive advantages?
   - What's the role of data moats?
   - How do you think about defensibility?

3. **Market Positioning** (Score: ___/5)
   - Do you understand different market positions (leader, challenger, niche)?
   - How does market position affect strategy?
   - What's first-mover vs. fast-follower?
   - How do you assess market timing?

**Competitive Landscape Check:**

**CoCounsel Competitors:**

| Competitor | Strengths | Weaknesses | TR Advantages |
|------------|-----------|------------|---------------|
| Harvey AI | ___ | ___ | ___ |
| Casetext/Legal AI | ___ | ___ | ___ |
| LexisNexis | ___ | ___ | ___ |
| Custom in-house | ___ | ___ | ___ |

**Expected Analysis:**

**Harvey:**
- Strengths: AI-native, fast-moving, VC-funded
- Weaknesses: Limited content, new entrant, unproven at scale
- TR Advantages: Westlaw integration, 100+ years content, trust

**Casetext:**
- Strengths: Legal-specific AI, good UX
- Weaknesses: Acquired by Thomson Reuters (actually a TR product now!)

**LexisNexis:**
- Strengths: Similar to TR (content, relationships)
- Weaknesses: Slower to AI
- TR Advantages: Better AI execution, CoCounsel lead

**In-house:**
- Strengths: Customized, data control
- Weaknesses: Expensive, slow, expertise required
- TR Advantages: Best-in-class AI, faster time to value

---

### 2.3 Market & Customer Understanding

**Self-Assessment Questions:**

1. **Customer Insights** (Score: ___/5)
   - Do you understand Thomson Reuters' customer segments?
   - Can you articulate customer pain points?
   - How do you gather customer insights?
   - How do you validate assumptions with customers?

2. **Market Dynamics** (Score: ___/5)
   - Do you understand legal tech market trends?
   - Can you assess market size and growth?
   - How do you identify emerging opportunities?
   - How do you track market shifts?

**Customer Segmentation:**

**Law Firms:**
- Size range: _______________
- Key needs: _______________
- Buying process: _______________
- Value drivers: _______________

**Corporate Legal Departments:**
- Characteristics: _______________
- Key needs: _______________
- Buying process: _______________
- Value drivers: _______________

**Government:**
- Characteristics: _______________
- Key needs: _______________
- Buying process: _______________
- Value drivers: _______________

**Expected Answers:**

**Law Firms:**
- Range: Solo → AmLaw 100 (thousands of lawyers)
- Needs: Billable hour efficiency, quality, client service
- Buying: Partners, IT committee, long sales cycles
- Value: Time savings (= more billable hours), quality

**Corporate:**
- In-house legal teams (10-1000+ lawyers)
- Needs: Cost reduction, compliance, efficiency
- Buying: GC, procurement, budget-conscious
- Value: Do more with less, risk mitigation

**Government:**
- Federal, state, local agencies
- Needs: Compliance, transparency, budget constraints
- Buying: RFP process, long cycles, security requirements
- Value: Cost savings, better outcomes for citizens

---

## Part 3: Communication & Influence

### 3.1 Executive Communication

**Self-Assessment Questions:**

1. **Communicating to Leadership** (Score: ___/5)
   - Can you present technical topics to non-technical executives?
   - How do you tailor message to audience?
   - Can you tell compelling stories with data?
   - How do you handle tough questions?

2. **Business Writing** (Score: ___/5)
   - Can you write clear, concise business documents?
   - Do you write effective email to executives?
   - Can you create executive summaries?
   - Do you structure arguments persuasively?

3. **Presentations** (Score: ___/5)
   - Can you create compelling slide decks?
   - How do you use data visualization effectively?
   - Can you present confidently to large groups?
   - How do you handle Q&A?

**Exercise: Executive Email**

```
Situation: You need to request $2M budget for RAG quality initiative.
You have 3 minutes of VP's attention (they get 200 emails/day).

Write the email.
```

**Your Email:**

```
To: VP Engineering
Subject: _______________

[Your email here - aim for <200 words]
```

**Expected Structure:**

```
To: VP Engineering
Subject: Request: $2M investment in RAG Quality (3-month payback)

[CONTEXT - 1 sentence]
Our RAG systems serve 10K+ CoCounsel users but lack systematic quality measurement.

[PROBLEM - 1-2 sentences]
This has led to 3 quality regressions in Q4, increasing support tickets 40% and
risking our 99.95% SLA. We're flying blind on our most critical AI capability.

[PROPOSAL - 2-3 sentences]
Invest $2M (10 engineers, 3 months) to build comprehensive evaluation framework:
automated testing, quality metrics, and monitoring. This prevents regressions,
accelerates feature velocity 2x, and reduces support costs $800K/year.

[ROI - 1 sentence]
3-month payback via support cost savings, with ongoing quality and velocity benefits.

[ASK - 1 sentence]
Can we discuss this week? I've prepared detailed analysis and can start immediately.

[NAME]
```

---

### 3.2 Cross-Functional Communication

**Self-Assessment Questions:**

1. **Translating Technical to Business** (Score: ___/5)
   - Can you explain AI/ML to non-technical stakeholders?
   - How do you use analogies effectively?
   - Can you quantify technical improvements in business terms?
   - How do you avoid jargon?

2. **Stakeholder Management** (Score: ___/5)
   - How do you keep stakeholders aligned?
   - Can you manage conflicting priorities?
   - How do you build trust across functions?
   - How do you influence without authority?

**Exercise: Explain Technical Concept**

```
Explain "RAG (Retrieval-Augmented Generation)" to:

1. CEO (30 seconds)
2. VP Product (2 minutes)
3. Legal team (5 minutes)
```

**Your Explanations:**

**CEO (30 seconds):**
_______________

**VP Product (2 minutes):**
_______________

**Legal Team (5 minutes):**
_______________

**Expected Explanations:**

**CEO:**
"RAG gives our AI accurate, up-to-date answers by searching our legal database
first, then using that information to generate responses. Think of it like a
lawyer who looks up relevant cases before advising a client. This prevents
AI from making things up and lets us leverage our $1B content investment."

**VP Product:**
"RAG combines search and generation. When a user asks a question, we first
retrieve relevant documents from Westlaw using semantic search. Then we feed
those documents to the LLM as context to generate an answer with citations.
Benefits: (1) Accuracy - grounded in real content (2) Freshness - uses latest
data (3) Transparency - shows sources. Challenges: retrieval quality critical,
latency from two-step process, citation verification needed."

**Legal Team:**
"RAG is how we ensure CoCounsel's AI provides legally accurate, citable answers.
Here's how it works: When you ask a question, the system searches Westlaw to
find the most relevant cases, statutes, and commentary - just like you would
manually. It then provides these materials to the AI as reference material to
draft a response. The AI can only use information from these retrieved documents,
and it cites its sources. This prevents the AI from 'hallucinating' or making
up cases - a critical concern for legal work. You can verify every statement
by checking the cited sources. Think of it as an AI research assistant that
shows its work."

---

### 3.3 Negotiation & Persuasion

**Self-Assessment Questions:**

1. **Influencing Decisions** (Score: ___/5)
   - How do you build buy-in for your ideas?
   - Can you change minds through data and logic?
   - How do you handle objections?
   - How do you find win-win solutions?

2. **Negotiation** (Score: ___/5)
   - How do you negotiate timelines and scope?
   - Can you push back on unrealistic requests?
   - How do you negotiate resource allocation?
   - How do you handle vendor negotiations?

**Scenario 3: Pushback**

```
Situation: PM wants AI feature that you think is technically infeasible
in the proposed timeframe.

PM's ask: "Contract risk prediction - show % chance of losing lawsuit"
Timeline: 6 weeks
Your concern: This requires:
- Large labeled dataset (don't have)
- Complex model development (months)
- Legal/ethical review (weeks)
- Accuracy requirements unclear
- Liability concerns

How do you handle this conversation?
```

**Your Response:**
_______________

**Expected Approach:**
1. Acknowledge the underlying need
2. Ask clarifying questions (why? for whom? what's good enough?)
3. Explain constraints clearly with data
4. Propose alternatives (risk factors, comparable cases, expert consultation)
5. Offer phased approach (start simple, iterate)
6. Collaborate on solution
7. Document decisions

---

## Part 4: Business Planning & Execution

### 4.1 Project Planning

**Self-Assessment Questions:**

1. **Business Cases** (Score: ___/5)
   - Can you build compelling business cases?
   - How do you estimate costs and benefits?
   - Can you assess risks and mitigations?
   - How do you present investment proposals?

2. **Roadmap Planning** (Score: ___/5)
   - How do you create technical roadmaps?
   - Can you align roadmap with strategy?
   - How do you sequence initiatives?
   - How do you communicate roadmaps?

3. **Resource Planning** (Score: ___/5)
   - How do you estimate resource needs?
   - Can you build team staffing plans?
   - How do you plan budgets?
   - How do you track spend?

**Exercise: Business Case**

```
Create business case for: "Automated Legal Document Summarization"

Target: Corporate legal departments
Feature: AI-generated summaries of contracts, cases, regulations

Estimate:
- Development cost and timeline
- Infrastructure cost
- Expected adoption and revenue
- ROI and payback period
```

**Your Business Case:**

**Problem:**
_______________

**Solution:**
_______________

**Market Size:**
_______________

**Development Cost:**
_______________

**Infrastructure Cost:**
_______________

**Revenue Projection:**
_______________

**ROI Calculation:**
_______________

**Risks:**
_______________

**Go/No-Go Recommendation:**
_______________

---

### 4.2 Execution & Delivery

**Self-Assessment Questions:**

1. **Hitting Deadlines** (Score: ___/5)
   - How do you ensure on-time delivery?
   - Can you identify and resolve blockers?
   - How do you manage scope creep?
   - How do you communicate delays?

2. **Quality vs. Speed** (Score: ___/5)
   - How do you balance quality and velocity?
   - When do you cut scope vs. extend timeline?
   - How do you define "good enough"?
   - How do you handle pressure to ship fast?

3. **Measuring Success** (Score: ___/5)
   - How do you define success criteria upfront?
   - Can you measure impact after launch?
   - How do you iterate based on data?
   - How do you communicate results?

**Scenario 4: Tough Tradeoff**

```
Situation: CoCounsel launch in 2 weeks.

Problem discovered: AI accuracy on tax law queries is 75% (target: 90%)

Options:
A) Delay launch 6 weeks to improve accuracy
B) Launch as planned, disable tax law queries
C) Launch with disclaimer: "Beta - verify all tax advice"
D) Launch to subset of users first (pilot)

Each option has business implications. What do you recommend?
```

**Your Analysis:**

**Option A (Delay):**
- Business impact: _______________
- Pros/Cons: _______________

**Option B (Disable):**
- Business impact: _______________
- Pros/Cons: _______________

**Option C (Disclaimer):**
- Business impact: _______________
- Pros/Cons: _______________

**Option D (Pilot):**
- Business impact: _______________
- Pros/Cons: _______________

**Recommendation:** _______________

**Expected Analysis:**

**Option A (Delay):**
- Impact: Miss market window, competitor risk, revenue delay ($1M+)
- Pros: Launch with quality
- Cons: Opportunity cost, team morale

**Option B (Disable):**
- Impact: Reduced scope, customer disappointment
- Pros: Safe, on-time
- Cons: Missing key use case, marketing challenge

**Option C (Disclaimer):**
- Impact: Reputational risk if used wrong
- Pros: Full feature set, on-time
- Cons: Liability concerns, trust issues

**Option D (Pilot):**
- Impact: Limited revenue, slower rollout
- Pros: Real-world validation, safer
- Cons: Complex logistics

**Best: Probably D (Pilot) or B (Disable)**
- Legal accuracy is non-negotiable
- Reputational risk > revenue risk
- Better to launch strong than fix reputation later

---

### 4.3 Data-Driven Decision Making

**Self-Assessment Questions:**

1. **Using Data** (Score: ___/5)
   - Do you use data to drive decisions?
   - Can you analyze data and draw insights?
   - How do you avoid analysis paralysis?
   - How do you balance data with intuition?

2. **A/B Testing** (Score: ___/5)
   - How do you design experiments?
   - Can you calculate statistical significance?
   - How do you choose metrics to test?
   - How do you act on test results?

3. **Analytics** (Score: ___/5)
   - Can you build dashboards and reports?
   - How do you instrument products for measurement?
   - Can you identify trends and anomalies?
   - How do you make data accessible to stakeholders?

**Exercise: A/B Test Design**

```
You want to test two RAG approaches:

Approach A: Semantic search only (current)
Approach B: Hybrid search (semantic + keyword)

Design an A/B test:
1. Hypothesis
2. Metrics
3. Sample size
4. Success criteria
5. Duration
6. Analysis plan
```

**Your Test Design:**
_______________

---

## Part 5: Strategic Impact

### 5.1 Thinking Like a Business Leader

**Self-Assessment Questions:**

1. **Business Mindset** (Score: ___/5)
   - Do you think about P&L impact of your work?
   - Can you see beyond your immediate scope?
   - How do you identify business opportunities?
   - Do you understand investor/board perspectives?

2. **Strategic Thinking** (Score: ___/5)
   - Can you think 3-5 years ahead?
   - How do you anticipate market changes?
   - Can you identify existential threats?
   - How do you balance innovation and execution?

**Reflection:**

If you were Thomson Reuters CEO for a day:

**Top 3 priorities for AI strategy:**
1. _______________
2. _______________
3. _______________

**Biggest threats:**
1. _______________
2. _______________
3. _______________

**Biggest opportunities:**
1. _______________
2. _______________
3. _______________

**3-year AI vision:**
_______________

---

### 5.2 Measuring Your Impact

**Self-Assessment:**

**List your top 3 business impacts from technical work:**

**Impact 1:**
- What you built: _______________
- Business metric moved: _______________
- Magnitude: _______________
- Verification: _______________

**Impact 2:**
- What you built: _______________
- Business metric moved: _______________
- Magnitude: _______________
- Verification: _______________

**Impact 3:**
- What you built: _______________
- Business metric moved: _______________
- Magnitude: _______________
- Verification: _______________

**Questions:**
- Can you quantify impact in dollars?
- Did you track metrics before/after?
- Can you attribute impact to your work?
- How do you tell this story?

---

## Scoring & Gap Analysis

### Total Scores by Category

| Category | Your Score | Max Score | Percentage |
|----------|-----------|-----------|------------|
| Business Value | ___/15 | 15 | ___% |
| Strategic Thinking | ___/20 | 20 | ___% |
| Communication | ___/15 | 15 | ___% |
| Planning & Execution | ___/15 | 15 | ___% |
| Strategic Impact | ___/10 | 10 | ___% |
| **TOTAL** | ___/75 | 75 | ___% |

### Interpretation

- **75-100%**: Expert - Ready for principal-level business impact
- **60-74%**: Advanced - Strong business acumen
- **45-59%**: Proficient - Growing business skills
- **<45%**: Developing - Focus on business fundamentals

---

## Business Acumen Development

### For Scores <45% (Developing)

**Focus:** Build business fundamentals

**Resources:**
- "The Personal MBA" by Josh Kaufman
- "Cracking the PM Interview" (business thinking)
- Finance for non-finance course
- Thomson Reuters investor presentations

**Actions:**
- Ask to see P&L and understand drivers
- Shadow product manager for a week
- Attend customer calls
- Read quarterly earnings reports
- Practice ROI calculations

**Timeline:** 3-6 months

---

### For Scores 45-74% (Proficient/Advanced)

**Focus:** Sharpen strategic thinking

**Resources:**
- "Good Strategy, Bad Strategy" by Richard Rumelt
- "Playing to Win" by Lafley & Martin
- Harvard Business Review articles
- Thomson Reuters strategy presentations

**Actions:**
- Lead business case development
- Present to executives
- Analyze competitor strategies
- Practice executive communication
- Build dashboards tracking business metrics

**Timeline:** 1-3 months

---

### For Scores 75%+ (Expert)

**Focus:** Principal-level impact

**Actions:**
- Prepare business impact stories (STAR format)
- Quantify all past achievements
- Review Thomson Reuters strategy
- Practice executive presentations
- Prepare strategic recommendations for interview

**Timeline:** 2-4 weeks

---

## Interview Preparation

### Business Questions to Prepare

**Strategic Thinking:**
- [ ] "How do you prioritize technical investments?"
- [ ] "How do you measure AI ROI?"
- [ ] "What's your approach to build vs. buy?"
- [ ] "How do you align technical work with business goals?"
- [ ] "What's your vision for AI in legal tech?"

**Business Impact:**
- [ ] "Tell me about a time you delivered significant business value"
- [ ] "How do you quantify the impact of your work?"
- [ ] "Describe a tradeoff between quality and velocity"
- [ ] "How do you handle pressure to ship fast?"

**Communication:**
- [ ] "How do you communicate with executives?"
- [ ] "Tell me about a time you influenced a business decision"
- [ ] "How do you explain technical concepts to non-technical stakeholders?"

**Thomson Reuters Specific:**
- [ ] "How would you grow CoCounsel revenue 10x?"
- [ ] "What's the ROI of improving RAG quality?"
- [ ] "How should TR think about LLM strategy?"
- [ ] "What new AI products should TR build?"

---

## Business Impact Stories (STAR Format)

### Template

**Situation:** Business context and challenge
**Task:** Your role and objective
**Action:** What YOU did (focus on business thinking)
**Result:** Business outcome with metrics

### Prepare 5 Stories

**Story 1: Delivered Revenue**
_______________

**Story 2: Reduced Costs**
_______________

**Story 3: Strategic Decision**
_______________

**Story 4: Influenced Leadership**
_______________

**Story 5: Measured Impact**
_______________

---

## Thomson Reuters Business Context

### Key Facts to Know

**Financial:**
- Revenue: ~$7B annually
- AI investment: Significant (Open Arena, CoCounsel, acquisitions)
- Growth strategy: AI-first transformation
- Margin focus: Improving through automation

**Market Position:**
- Legal: Co-leader with LexisNexis
- Financial: Strong (Refinitiv)
- Tax: Major player
- News: Reuters brand

**Strategy:**
- Transform core products with AI
- Build new AI-native products (CoCounsel)
- Multi-model approach
- Content + AI moat

**Customers:**
- Law firms (all sizes)
- Corporate legal departments
- Accountants and tax professionals
- Financial services firms
- Governments

**Competitive Threats:**
- LexisNexis (traditional competitor)
- Harvey AI (AI-first startup)
- Bloomberg (financial)
- In-house AI (large law firms)

**Opportunities:**
- AI disruption of legal work
- Expanding TAM (make legal services accessible)
- New products and markets
- International expansion

---

## Practice Exercises

### Exercise 1: ROI Analysis
Calculate ROI for 5 different AI projects with varying costs and benefits.

### Exercise 2: Business Case
Write full business case for new AI feature (your choice).

### Exercise 3: Executive Presentation
Create 10-slide deck pitching strategic initiative to CEO.

### Exercise 4: Competitive Analysis
Analyze CoCounsel vs. 3 competitors across 5 dimensions.

### Exercise 5: Metrics Dashboard
Design executive dashboard for CoCounsel (15 key metrics).

---

## Resources

### Books
- "The Personal MBA" by Josh Kaufman
- "Good Strategy, Bad Strategy" by Richard Rumelt
- "Lean Analytics" by Croll & Yoskovitz
- "Measure What Matters" by John Doerr (OKRs)
- "The Hard Thing About Hard Things" by Ben Horowitz

### Courses
- "Finance for Non-Finance" (LinkedIn Learning)
- "Strategic Management" (Coursera)
- "Business Strategy" (edX)

### Thomson Reuters Materials
- Investor presentations (quarterly)
- Annual report (10-K)
- Earnings calls (transcripts)
- Product websites and demos
- Tech blog posts

---

## Notes & Reflections

**Date Completed**: _______________

**Overall Business Acumen** (1-5): ___

**Strongest Business Skills**:
1. _______________
2. _______________
3. _______________

**Areas to Develop**:
1. _______________
2. _______________
3. _______________

**Top 3 Business Impact Stories**:
1. _______________
2. _______________
3. _______________

**Questions for Interviewer About TR Business**:
1. _______________
2. _______________
3. _______________

**Action Plan** (Next 2 Weeks):
_______________

**Follow-up Date**: _______________
