# Domain Expertise Skills Assessment

**Assessment Area**: Legal Tech, Compliance, and Financial Data
**Target Role**: Principal AI Engineer at Thomson Reuters
**Date**: November 2025

## Purpose

This assessment evaluates your domain knowledge across Thomson Reuters' core markets: legal, compliance, tax/accounting, and financial services. While deep domain expertise isn't required for the role, demonstrating curiosity and foundational knowledge shows you can partner effectively with domain experts.

---

## Assessment Framework

**Scoring Guide:**
- **5 - Expert**: Deep domain knowledge, could consult on domain problems
- **4 - Advanced**: Strong working knowledge, understands nuances
- **3 - Proficient**: Solid fundamentals, can have informed conversations
- **2 - Developing**: Basic awareness, learning actively
- **1 - Awareness**: Minimal knowledge, but interested to learn

**Note**: For Principal AI Engineer, scores of 2-3 are perfectly acceptable. What matters is learning agility and ability to collaborate with domain experts.

---

## Part 1: Legal Technology

### 1.1 Legal Industry Fundamentals

**Self-Assessment Questions:**

1. **Legal Practice Basics** (Score: ___/5)
   - Do you understand how law firms operate (billing, caseload, practice areas)?
   - Can you explain the difference between litigation and transactional work?
   - Do you know common legal workflows (discovery, contract review, research)?
   - Can you name major practice areas (corporate, IP, tax, litigation)?

2. **Legal Documents** (Score: ___/5)
   - Can you identify common legal document types (contracts, briefs, pleadings)?
   - Do you understand basic contract structure (parties, terms, signatures)?
   - Can you recognize key clauses (indemnification, confidentiality, termination)?
   - Do you know what makes legal writing unique (citations, precision, structure)?

3. **Legal Research** (Score: ___/5)
   - Do you understand how legal research works (cases, statutes, regulations)?
   - Can you explain legal precedent and stare decisis?
   - Do you know what citations are for (Blue Book format)?
   - Can you explain primary vs. secondary legal sources?

**Knowledge Check:**

1. What's the difference between a statute and a case law?
   - Your answer: _______________
   - Reference: Statutes are laws passed by legislatures; case law is from court decisions

2. What is legal discovery?
   - Your answer: _______________
   - Reference: Pre-trial process where parties exchange evidence and information

3. What does "legal precedent" mean?
   - Your answer: _______________
   - Reference: Prior court decisions that establish principles for future similar cases

4. Name 3 types of legal contracts:
   - 1. _______________
   - 2. _______________
   - 3. _______________
   - Reference: NDAs, employment agreements, vendor contracts, M&A agreements, leases

**Learning Resources:**
- Take Westlaw or LexisNexis tutorial
- Read "Law 101" by Jay Feinman
- Browse CoCounsel demo and documentation
- Watch legal tech webinars

---

### 1.2 Legal Technology Landscape

**Self-Assessment Questions:**

1. **Legal Tech Categories** (Score: ___/5)
   - Can you name major legal tech categories (research, practice mgmt, e-discovery)?
   - Do you know key players in legal AI (TR, LexisNexis, Casetext, Harvey)?
   - Can you explain different legal tech use cases?
   - Do you understand legal tech adoption challenges?

2. **Thomson Reuters Legal Products** (Score: ___/5)
   - Can you explain what Westlaw does?
   - Do you know CoCounsel's core capabilities?
   - Can you describe Practical Law and its value?
   - Do you understand how these products fit together?

3. **AI in Legal** (Score: ___/5)
   - Can you explain how AI is used in legal research?
   - Do you understand AI applications in contract analysis?
   - Can you discuss ethical concerns with legal AI?
   - Do you know regulatory constraints on legal AI?

**Product Knowledge Check:**

**Westlaw** (see: westlaw-study-guide.md)
- Primary purpose: _______________
- Key features: _______________
- Differentiators: _______________

**CoCounsel** (see: cocounsel-study-guide.md)
- Primary purpose: _______________
- Core skills (name 3): _______________
- AI models used: _______________

**Practical Law**
- Primary purpose: _______________
- Target users: _______________

**Integration Question:**
How do Westlaw and CoCounsel work together?
- Your answer: _______________

---

### 1.3 Legal AI Challenges

**Self-Assessment Questions:**

1. **Accuracy Requirements** (Score: ___/5)
   - Do you understand why legal accuracy is critical (liability, ethics)?
   - Can you explain "hallucination" risk in legal AI?
   - Do you know how to verify AI-generated legal content?
   - Can you discuss acceptable error rates for legal AI?

2. **Ethics & Professional Responsibility** (Score: ___/5)
   - Do you know about attorney-client privilege?
   - Can you explain unauthorized practice of law (UPL)?
   - Do you understand confidentiality requirements?
   - Can you discuss conflicts of interest in legal AI?

3. **Regulatory Compliance** (Score: ___/5)
   - Do you know about bar association AI guidelines?
   - Can you discuss transparency requirements for legal AI?
   - Do you understand data privacy in legal context (GDPR, attorney-client)?
   - Can you explain audit trail requirements?

**Scenario 1: Legal AI Ethics**

```
Situation: CoCounsel generates contract language that looks good but
includes a subtle error that could cost a client millions if not caught.

Questions:
1. Who is liable - the law firm, the lawyer, TR, or the AI vendor?
2. What safeguards should be in place?
3. How should this be disclosed to clients?
4. What are the product implications?
```

**Your Analysis:**
[Write here]

**Expected Considerations:**
- Lawyers have ultimate responsibility (cannot delegate judgment)
- AI should be positioned as "assistant" not "advisor"
- Need human review at critical points
- Clear disclaimers about AI limitations
- Audit trails for accountability
- Training lawyers on AI limitations

---

### 1.4 Legal Domain Applications

**Scenario 2: Contract Analysis**

```
You're designing AI feature to analyze M&A contracts (100+ pages).

Requirements from legal team:
- Identify key terms (price, date, conditions)
- Flag unusual or risky clauses
- Compare to standard precedents
- Extract obligations and deadlines
- Maintain privilege and confidentiality

What are the challenges and considerations?
```

**Your Analysis:**
[Write here]

**Expected Challenges:**
- Long context (100+ pages exceeds most LLM context windows)
- Legal language ambiguity
- Domain-specific terminology
- Importance of not missing anything
- Explaining AI reasoning
- Verifying extracted information
- Handling redlines and versions

---

**Scenario 3: Legal Research**

```
Design AI to help lawyers research case law.

User query: "What are recent cases about AI copyright infringement?"

What makes this challenging?
```

**Your Analysis:**
[Write here]

**Expected Challenges:**
- "Recent" is ambiguous (last month? year? 3 years?)
- Need to understand legal concepts (copyright, infringement)
- Cases cite other cases (citation graph)
- Jurisdiction matters (federal vs. state, circuit differences)
- Need accurate citations (Blue Book format)
- Must rank by relevance and precedential value
- Can't hallucinate cases (serious ethics violation)

---

## Part 2: Compliance & Risk

### 2.1 Regulatory Compliance Basics

**Self-Assessment Questions:**

1. **Compliance Fundamentals** (Score: ___/5)
   - Do you understand what regulatory compliance means?
   - Can you name major regulatory frameworks (SOX, GDPR, SOC 2)?
   - Do you know different types of compliance (financial, data, industry)?
   - Can you explain compliance vs. risk management?

2. **Data Privacy** (Score: ___/5)
   - Can you explain GDPR key principles?
   - Do you understand CCPA requirements?
   - Can you discuss data subject rights (access, deletion, portability)?
   - Do you know data retention and deletion requirements?

3. **Information Security** (Score: ___/5)
   - Can you explain SOC 2 trust principles?
   - Do you understand ISO 27001 basics?
   - Can you discuss access controls and audit trails?
   - Do you know encryption requirements (at rest, in transit)?

**Knowledge Check:**

**GDPR (General Data Protection Regulation)**
- Applies to: _______________
- Key principles: _______________
- Data subject rights: _______________
- Penalties: _______________

**SOX (Sarbanes-Oxley)**
- Applies to: _______________
- Key requirements: _______________
- AI implications: _______________

**SOC 2**
- Purpose: _______________
- Trust principles: _______________
- Relevance to AI: _______________

---

### 2.2 Compliance in AI Systems

**Self-Assessment Questions:**

1. **AI Governance** (Score: ___/5)
   - Do you understand AI regulatory landscape (EU AI Act, US state laws)?
   - Can you explain model governance requirements?
   - Do you know documentation requirements for AI systems?
   - Can you discuss AI bias and fairness regulations?

2. **Explainability & Transparency** (Score: ___/5)
   - Do you understand "right to explanation" requirements?
   - Can you explain model interpretability techniques?
   - Do you know when AI usage must be disclosed?
   - Can you discuss transparency in automated decisions?

3. **Data Governance** (Score: ___/5)
   - Do you understand data lineage requirements?
   - Can you explain consent management for AI training?
   - Do you know data minimization principles?
   - Can you discuss cross-border data transfer restrictions?

**Scenario 4: GDPR Compliance**

```
CoCounsel processes legal documents that may contain:
- Personal data (names, addresses, SSNs)
- Sensitive data (health, criminal records)
- Data from EU citizens

GDPR requirements:
- Lawful basis for processing
- Data minimization
- Right to deletion
- Data portability
- Breach notification (72 hours)

Design compliance approach.
```

**Your Compliance Design:**
[Write here]

**Expected Approach:**
- Data classification and scanning
- PII detection and masking
- Consent management
- Data retention policies
- Deletion workflows
- Audit logging
- Breach detection and response
- Data processing agreements

---

### 2.3 Financial Compliance

**Self-Assessment Questions:**

1. **Financial Regulations** (Score: ___/5)
   - Can you explain AML (Anti-Money Laundering) basics?
   - Do you understand KYC (Know Your Customer)?
   - Can you discuss SEC regulations for financial services?
   - Do you know about FINRA rules?

2. **Tax Compliance** (Score: ___/5)
   - Do you understand tax reporting requirements?
   - Can you explain tax jurisdictions and complexity?
   - Do you know about transfer pricing?
   - Can you discuss international tax compliance?

**Knowledge Check:**

What is AML and why does it matter for AI?
- Your answer: _______________

What is a SAR (Suspicious Activity Report)?
- Your answer: _______________

Why is tax compliance complex?
- Your answer: _______________

---

### 2.4 Risk Management

**Self-Assessment Questions:**

1. **Risk Identification** (Score: ___/5)
   - Can you identify risks in AI systems (bias, errors, security)?
   - Do you understand operational risk?
   - Can you explain reputational risk?
   - Do you know regulatory risk?

2. **Risk Mitigation** (Score: ___/5)
   - How do you design controls for AI risk?
   - What's your approach to testing compliance?
   - How do you monitor ongoing compliance?
   - How do you respond to compliance failures?

**Scenario 5: Risk Assessment**

```
CoCounsel new feature: automated contract redlining

Potential risks:
- Legal: UPL (unauthorized practice of law)
- Accuracy: Wrong suggestions harm clients
- Security: Exposing confidential info
- Bias: Systematically bad advice for certain contract types
- Regulatory: Violating bar association rules

Conduct risk assessment and design mitigations.
```

**Your Risk Assessment:**

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| UPL | ___ | ___ | ___ |
| Accuracy | ___ | ___ | ___ |
| Security | ___ | ___ | ___ |
| Bias | ___ | ___ | ___ |
| Regulatory | ___ | ___ | ___ |

---

## Part 3: Financial Services & Data

### 3.1 Financial Services Basics

**Self-Assessment Questions:**

1. **Financial Markets** (Score: ___/5)
   - Do you understand major asset classes (equities, fixed income, derivatives)?
   - Can you explain market structure (exchanges, OTC, dark pools)?
   - Do you know key market participants (banks, hedge funds, retail)?
   - Can you discuss market data (quotes, trades, fundamentals)?

2. **Financial Products** (Score: ___/5)
   - Can you explain common financial instruments (stocks, bonds, options)?
   - Do you understand derivatives and their purposes?
   - Can you discuss structured products?
   - Do you know about ETFs and mutual funds?

3. **Financial Analysis** (Score: ___/5)
   - Do you understand financial statements (balance sheet, P&L, cash flow)?
   - Can you explain key metrics (PE ratio, EPS, ROE)?
   - Do you know about fundamental vs. technical analysis?
   - Can you discuss valuation methods?

**Knowledge Check:**

What is a derivative?
- Your answer: _______________

What's the difference between a stock and a bond?
- Your answer: _______________

What does P/E ratio measure?
- Your answer: _______________

Name 3 types of financial data:
1. _______________
2. _______________
3. _______________

---

### 3.2 Financial Data & Analytics

**Self-Assessment Questions:**

1. **Market Data** (Score: ___/5)
   - Do you understand real-time vs. delayed data?
   - Can you explain tick data and aggregation?
   - Do you know about reference data?
   - Can you discuss data quality in financial markets?

2. **Financial News & Sentiment** (Score: ___/5)
   - Do you understand how news moves markets?
   - Can you explain sentiment analysis for finance?
   - Do you know about event detection?
   - Can you discuss challenges of financial NLP?

3. **Alternative Data** (Score: ___/5)
   - Can you explain what alternative data means?
   - Do you know examples (satellite, web scraping, credit cards)?
   - Can you discuss alpha generation from alt data?
   - Do you understand ethical concerns with alt data?

**Scenario 6: Financial News Analysis**

```
Design AI system to analyze financial news for Thomson Reuters clients.

Requirements:
- Extract key entities (companies, people, products)
- Classify event types (M&A, earnings, regulatory, etc.)
- Assess sentiment and market impact
- Link to relevant financial instruments
- Real-time processing (low latency)

What are the challenges?
```

**Your Analysis:**
[Write here]

**Expected Challenges:**
- Speed (news breaks fast, need real-time)
- Accuracy (false positives costly)
- Entity disambiguation (multiple companies with similar names)
- Domain-specific language
- Detecting sarcasm and nuance
- Market context awareness
- Handling rumors vs. facts
- Multi-language support

---

### 3.3 Thomson Reuters Financial Products

**Self-Assessment Questions:**

1. **Refinitiv Products** (Score: ___/5)
   - Do you know what Refinitiv is (TR financial data business)?
   - Can you name key products (Eikon, Workspace, Data feeds)?
   - Do you understand the customer base (traders, analysts, quants)?
   - Can you explain competitive landscape (Bloomberg, FactSet)?

2. **Financial Data Services** (Score: ___/5)
   - Do you know what market data feeds are?
   - Can you explain data licensing and redistribution?
   - Do you understand exchange data vs. vendor data?
   - Can you discuss data governance for financial data?

**Knowledge Check:**

What is Thomson Reuters Workspace?
- Your answer: _______________

How does it compete with Bloomberg Terminal?
- Your answer: _______________

What types of financial data does TR provide?
- Your answer: _______________

---

### 3.4 AI in Financial Services

**Self-Assessment Questions:**

1. **Trading & Investment** (Score: ___/5)
   - Do you understand algorithmic trading basics?
   - Can you explain robo-advisors?
   - Do you know about portfolio optimization?
   - Can you discuss market prediction challenges?

2. **Risk Management** (Score: ___/5)
   - Do you understand credit risk modeling?
   - Can you explain fraud detection systems?
   - Do you know about stress testing?
   - Can you discuss model risk management?

3. **Regulatory Technology (RegTech)** (Score: ___/5)
   - Do you understand compliance automation?
   - Can you explain transaction monitoring?
   - Do you know about regulatory reporting?
   - Can you discuss AI for KYC/AML?

**Scenario 7: Fraud Detection**

```
Design ML system to detect fraudulent transactions for financial institution.

Data available:
- Transaction history
- Customer profiles
- Merchant data
- Device fingerprints
- Behavioral patterns

Requirements:
- Real-time scoring (<100ms)
- Low false positives (customer friction)
- Catch sophisticated fraud patterns
- Explainable decisions (regulatory requirement)

Design your approach.
```

**Your Design:**
[Write here]

**Expected Approach:**
- Feature engineering (velocity, anomaly, network features)
- Model selection (trees, neural nets, ensemble)
- Real-time inference architecture
- Explainability (SHAP, LIME, rule extraction)
- Feedback loop (fraud confirmed/false positive)
- Model monitoring (drift, performance)
- Compliance documentation

---

## Part 4: Cross-Domain Knowledge

### 4.1 Tax & Accounting

**Self-Assessment Questions:**

1. **Tax Basics** (Score: ___/5)
   - Do you understand different tax types (income, corporate, sales, etc.)?
   - Can you explain tax compliance challenges?
   - Do you know about tax research and planning?
   - Can you discuss international tax complexity?

2. **Accounting Fundamentals** (Score: ___/5)
   - Do you understand GAAP basics?
   - Can you explain auditing process?
   - Do you know about accounting standards (US vs. IFRS)?
   - Can you discuss financial controls?

**Thomson Reuters Tax Products:**
- Checkpoint (tax research)
- ONESOURCE (tax compliance software)
- AI applications in tax

**Knowledge Check:**

Why is tax compliance complex?
- Your answer: _______________

How can AI help with tax?
- Your answer: _______________

---

### 4.2 Corporate & Commercial

**Self-Assessment Questions:**

1. **Corporate Law** (Score: ___/5)
   - Do you understand corporate structure (LLC, C-corp, etc.)?
   - Can you explain M&A process basics?
   - Do you know about corporate governance?
   - Can you discuss securities regulations?

2. **Intellectual Property** (Score: ___/5)
   - Do you understand IP types (patents, trademarks, copyright)?
   - Can you explain patent search and analysis?
   - Do you know about IP licensing?
   - Can you discuss AI and IP (who owns AI outputs)?

**Scenario 8: IP & AI**

```
Question: If CoCounsel generates a legal brief, who owns the copyright?

Consider:
- AI-generated content copyrightability
- Work-for-hire doctrine
- User agreements
- Professional ethics
- Product positioning

What's your analysis?
```

**Your Analysis:**
[Write here]

---

### 4.3 Industry-Specific Knowledge

**Self-Assessment Questions:**

1. **Healthcare** (Score: ___/5)
   - Do you understand HIPAA basics?
   - Can you explain healthcare compliance challenges?
   - Do you know about medical coding?
   - Can you discuss clinical vs. claims data?

2. **Government** (Score: ___/5)
   - Do you understand government procurement?
   - Can you explain FedRAMP for cloud services?
   - Do you know about FOIA (Freedom of Information Act)?
   - Can you discuss public records and transparency?

3. **Media & News** (Score: ___/5)
   - Do you understand news organizations?
   - Can you explain journalistic standards?
   - Do you know about content licensing?
   - Can you discuss AI in news (generation, personalization)?

---

## Part 5: Domain Learning Agility

### 5.1 Learning New Domains

**Self-Assessment:**

1. **Research Skills** (Score: ___/5)
   - How quickly can you ramp up in new domain?
   - What's your approach to learning domain knowledge?
   - How do you identify good information sources?
   - How do you validate understanding?

2. **Domain Expert Collaboration** (Score: ___/5)
   - How do you work effectively with domain experts?
   - How do you ask good questions?
   - How do you translate domain needs to technical requirements?
   - How do you build credibility in new domains?

**Reflection:**

Describe a time you learned a new domain quickly:
- Domain: _______________
- Learning approach: _______________
- Timeline: _______________
- How you validated understanding: _______________
- How you applied knowledge: _______________

---

### 5.2 Domain-Driven AI Design

**Questions:**

How do domain requirements influence AI system design?

**Legal AI:**
- Accuracy requirements: _______________
- Explainability needs: _______________
- Ethical considerations: _______________

**Financial AI:**
- Latency requirements: _______________
- Regulatory constraints: _______________
- Data governance: _______________

**Compliance AI:**
- Audit trail needs: _______________
- Transparency requirements: _______________
- Risk tolerance: _______________

---

## Scoring & Gap Analysis

### Total Scores by Category

| Category | Your Score | Max Score | Percentage |
|----------|-----------|-----------|------------|
| Legal Technology | ___/25 | 25 | ___% |
| Compliance & Risk | ___/20 | 20 | ___% |
| Financial Services | ___/20 | 20 | ___% |
| Cross-Domain | ___/15 | 15 | ___% |
| Learning Agility | ___/10 | 10 | ___% |
| **TOTAL** | ___/90 | 90 | ___% |

### Interpretation

**For Principal AI Engineer role:**
- **40-60%**: Good - Shows curiosity and basic domain awareness
- **60-75%**: Strong - Solid domain knowledge, can partner effectively
- **75-100%**: Excellent - Deep domain expertise (not expected but impressive)

**Note**: Domain expertise is less critical than technical depth for this role. Scores of 50-60% are perfectly acceptable if combined with strong learning agility.

---

## Domain Learning Plan

### Priority 1: Legal Technology (Most Critical)

**Week 1-2:**
- [ ] Review CoCounsel demo and documentation
- [ ] Complete Westlaw tutorial
- [ ] Read cocounsel-study-guide.md and westlaw-study-guide.md
- [ ] Watch legal tech webinars
- [ ] Read 3 legal AI blog posts

**Week 3-4:**
- [ ] Understand legal workflow (research, contract review, litigation)
- [ ] Learn legal document types
- [ ] Study legal AI ethics
- [ ] Practice discussing legal AI challenges

---

### Priority 2: Compliance & Risk

**Week 1:**
- [ ] Read GDPR overview
- [ ] Understand SOC 2 basics
- [ ] Learn AI governance principles
- [ ] Study data privacy in AI

**Week 2:**
- [ ] Review EU AI Act summary
- [ ] Understand model documentation requirements
- [ ] Learn about explainability regulations
- [ ] Study TR compliance approach

---

### Priority 3: Financial Services (If Time Permits)

**Optional:**
- [ ] Read "A Random Walk Down Wall Street"
- [ ] Browse Thomson Reuters Workspace demo
- [ ] Learn basic financial terminology
- [ ] Understand market data concepts

---

## Interview Preparation

### Domain Questions to Prepare

**Legal:**
- [ ] "What do you know about legal tech?"
- [ ] "How would you approach building AI for lawyers?"
- [ ] "What are the unique challenges in legal AI?"
- [ ] "How do you ensure accuracy in legal AI?"
- [ ] "What ethical concerns exist with legal AI?"

**Compliance:**
- [ ] "How do you design AI systems for compliance?"
- [ ] "What do you know about GDPR/AI regulation?"
- [ ] "How do you make AI systems explainable?"
- [ ] "How do you handle sensitive data in AI?"

**Financial:**
- [ ] "What experience do you have with financial data?"
- [ ] "How would you approach financial news analysis?"
- [ ] "What are challenges with financial AI?"

**General:**
- [ ] "How do you learn new domains?"
- [ ] "How do you work with domain experts?"
- [ ] "Why are you interested in legal tech?"

---

## Thomson Reuters Domain Focus

### Study Priorities for Interview

1. **CoCounsel** (MUST KNOW)
   - Core capabilities
   - Target users
   - Differentiators
   - Technical architecture

2. **Westlaw** (MUST KNOW)
   - Primary purpose
   - Key features
   - Market position
   - AI integration

3. **Legal AI Landscape** (SHOULD KNOW)
   - Key competitors (Harvey, Casetext, etc.)
   - Industry trends
   - Adoption challenges
   - Ethical concerns

4. **TR Strategy** (GOOD TO KNOW)
   - AI-first approach
   - Multi-model strategy
   - Product integration
   - Market differentiation

---

## Demonstrating Domain Interest

### In Interviews, Show:

**Curiosity:**
"I've been fascinated learning about legal tech. I spent time with Westlaw and CoCounsel demos, and I'm impressed by how AI is transforming legal research."

**Learning Agility:**
"While I don't have deep legal domain expertise, I have a track record of quickly ramping up in new domains. For example, [story about learning new domain]."

**Respect for Domain:**
"I understand that legal accuracy is paramount and there's zero tolerance for errors. I'd work closely with legal experts to understand requirements and validate outputs."

**Business Understanding:**
"Legal professionals bill by the hour, so any AI that saves time has clear ROI. But it must be trustworthy, or lawyers won't use it."

**User Empathy:**
"Lawyers are highly skilled professionals. AI should augment their expertise, not replace judgment. The UX needs to build trust and make it easy to verify outputs."

---

## Resources

### Legal Tech
- **Books**: "Tomorrow's Lawyers" by Richard Susskind
- **Websites**: LegalTech News, ABA Legal Technology Resource Center
- **Podcasts**: LawNext, Busy Lawyer Podcast
- **Reports**: TR Legal Tech Trends Report

### Compliance
- **Websites**: GDPR.eu, EU AI Act summaries
- **Courses**: GDPR Compliance (LinkedIn Learning)
- **Documents**: SOC 2 trust principles, ISO 27001 overview

### Financial Services
- **Books**: "A Random Walk Down Wall Street"
- **Websites**: Investopedia, TR financial blogs
- **Courses**: Finance for Non-Finance (Coursera)

---

## Notes & Reflections

**Date Completed**: _______________

**Overall Domain Confidence** (1-5): ___

**Strongest Domain Areas**:
1. _______________
2. _______________

**Areas to Study**:
1. _______________
2. _______________
3. _______________

**Questions for Interview**:
1. _______________
2. _______________
3. _______________

**Learning Plan** (Next 2 Weeks):
_______________

**Follow-up Date**: _______________
