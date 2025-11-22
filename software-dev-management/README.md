## Metrics, KPIs & Measuring Success

### Understanding Engineering KPIs

**Definition:**
Engineering key performance indicators (KPIs) are quantifiable metrics that tell leaders about the performance, efficiency, or impact of engineering. They help teams identify and resolve specific issues within the process.

**Core Principle:**
Use metrics for improvement, not punishment. The goal should be continuous improvement, not penalizing individuals or teams.

### DORA Metrics: The Industry Standard

**The Four Key Metrics:**

1. **Deployment Frequency**
   - How often code is deployed to production
   - Higher frequency indicates better continuous delivery
   - Elite performers: Multiple times per day
   - High performers: Once per day to once per week

2. **Lead Time for Changes**
   - Time from code commit to running in production
   - Measures efficiency of delivery pipeline
   - Elite performers: Less than one hour
   - High performers: Less than one day

3. **Mean Time to Recovery (MTTR)**
   - How quickly service is restored after incident
   - Measures resilience and incident response
   - Elite performers: Less than one hour
   - High performers: Less than one day

4. **Change Failure Rate**
   - Percentage of deployments causing failure
   - Measures quality and testing effectiveness
   - Elite performers: 0-15%
   - High performers: 16-30%

**Why DORA Metrics Matter:**
These metrics reveal how quickly engineering can turn ideas into impact. Teams with high psychological safety demonstrate 43% higher deployment frequency and 65% faster MTTR.

### Categories of Engineering KPIs

**Output KPIs (Results):**
- Number of features delivered
- Bugs fixed
- Technical debt reduced
- Documentation created

**Process KPIs (Efficiency):**
- Time taken to deliver features
- Code review turnaround time
- Build and test duration
- Deployment frequency

**People KPIs (Team Health):**
- Team member satisfaction
- Engagement levels
- Retention and turnover rate
- Skill development progress

### Essential Team Performance Metrics

**Productivity & Delivery:**

**On-Time Delivery Rate:**
- Formula: (# of Projects Delivered on-Time / Total # of Projects Delivered) × 100
- Measures reliability and estimation accuracy
- Helps identify planning issues

**Velocity:**
- Amount of work completed in a sprint
- Used to predict capacity for future sprints
- Should be stable over time for mature teams
- Don't compare velocity across teams

**Throughput:**
- Number of items completed per time period
- More objective than story points
- Helps identify bottlenecks

**Cost & Budget:**

**Cost Performance Indicator (CPI):**
- Calculated after project completion
- Compares budgeted cost to actual cost
- Determines project efficiency

**Team Efficiency:**
- Cost of engineering team vs. number of projects handled
- Helps optimize resource allocation
- Consider in context of business value delivered

**Quality Metrics:**

**Code Quality:**
- Code review findings
- Technical debt ratio
- Test coverage
- Static analysis results

**Defect Metrics:**
- Bugs found in production
- Bug fix time
- Regression rate
- Severity distribution

**Team Health Metrics:**

**Team Satisfaction:**
- Regular surveys (e.g., quarterly)
- Engagement levels
- Psychological safety measures
- Work-life balance indicators

**Retention:**
- Turnover rate
- Time to fill positions
- Regretted vs. non-regretted attrition

### Best Practices for Using Metrics

**Balance Multiple Perspectives:**
At top companies like Google, no single metric is treated as sufficient. Google's Developer Intelligence team measures code reviews not just for speed, but also ease and quality.

**Avoid These Pitfalls:**

**Vanity Metrics to Avoid:**
- **Story points shipped**: Doesn't measure actual progress or complexity
- **Lines of code**: Doesn't indicate better code (often the opposite)
- **Hours worked**: Doesn't reflect productivity or value
- **Retention alone**: Tracks satisfaction but doesn't reflect engineering efficiency

**The Goodhart Trap:**
"When a measure becomes a target, it ceases to be a good measure."
- Don't over-optimize single metrics
- Teams will game metrics if incentivized poorly
- Focus on outcomes, not just outputs

**Balance Quantitative and Qualitative:**
Quantitative indicators include:
- Number of commits
- Development cycle time
- DORA metrics

Qualitative indicators include:
- Code quality assessments
- Customer satisfaction surveys
- Team morale and feedback

Both are necessary for complete picture.

### Creating Your Metrics Dashboard

**Key Principles:**

**Consistency:**
Ensure consistency between high-level KPIs and more granular team/individual metrics. Align team metrics with organizational goals.

**Actionability:**
Every metric should drive action. If you can't act on it, don't measure it.

**Visibility:**
Make metrics visible to the team. Transparency builds ownership and drives improvement.

**Example Dashboard Structure:**

**Delivery Health:**
- Deployment frequency (DORA)
- Lead time for changes (DORA)
- On-time delivery rate
- Velocity trend

**Quality Health:**
- Change failure rate (DORA)
- Production incidents
- Mean time to recovery (DORA)
- Test coverage

**Team Health:**
- Team satisfaction score
- Retention rate
- Sprint commitment reliability
- Unplanned work ratio

**Business Impact:**
- Features delivered
- User-facing value
- Technical debt ratio
- Cost per story point/feature

### Metrics-Driven Improvement

**The Cycle:**

1. **Measure**: Collect data consistently
2. **Analyze**: Identify trends and patterns
3. **Discuss**: Review with team in retrospectives
4. **Act**: Implement improvements
5. **Validate**: Measure impact of changes
6. **Iterate**: Continuous improvement

**Example:**
- Observe: MTTR increasing over past 3 sprints
- Analyze: Root cause is incomplete monitoring
- Discuss: Team retrospective on incident response
- Act: Implement better monitoring and runbooks
- Validate: Measure MTTR improvement
- Iterate: Refine monitoring based on learnings

### Communicating Metrics to Stakeholders

**For Engineering Teams:**
- Focus on actionable insights
- Celebrate improvements
- Discuss how to move metrics
- Make it collaborative, not punitive

**For Leadership:**
- Connect to business outcomes
- Show trends over time
- Highlight both successes and concerns
- Provide context for the numbers

**For Product Partners:**
- Emphasize delivery and quality
- Show impact on customer experience
- Discuss trade-offs and capacity
- Build shared understanding

---
## Team Culture & Psychological Safety

### The State of Remote Work in 2025

**Current Reality:**
- 72% of engineering teams now operate in a fully distributed model (Stack Overflow 2024 Developer Survey)
- 68% of technical leaders identify building a strong remote engineering culture as their top priority (GitLab 2025 Remote Work Report)

**The Challenge:**
Distributed, remote, and virtual teams have fewer opportunities for spontaneous, casual conversation, which can mean people are more likely to feel alone, anxious, or unsure of what to do.

### Understanding Psychological Safety

**What It Is:**
Psychological safety is the belief that you can speak up, take risks, and make mistakes without fear of punishment or humiliation.

**Why It Matters:**
Google's Project Aristotle showed that co-location of teams had no impact on their performance as long as they possessed psychological safety. Virtual teams can perform just as highly, if not even more so, than teams in the same place.

**The Impact:**
Teams reporting high psychological safety demonstrate:
- 43% higher deployment frequency
- 65% faster mean time to recovery (MTTR)
- 72% improvement in team cohesion
- 68% increase in code quality metrics

### Building Psychological Safety

**Core Practices:**

**1. Make It Safe to Speak Up**
- Welcome questions, even basic ones
- Thank people for raising concerns
- Never punish messengers of bad news
- Model vulnerability by admitting your own mistakes

**2. Encourage Productive Conflict**
- Frame disagreement as problem-solving
- Focus on ideas, not people
- Establish norms for respectful debate
- Celebrate when team members challenge ideas constructively

**3. Embrace Failure as Learning**
- Conduct blameless postmortems
- Focus on systems, not individuals
- Share lessons learned openly
- Celebrate intelligent failures

**4. Be Inclusive and Accessible**
- Create multiple channels for input
- Actively seek diverse perspectives
- Notice who's not speaking and invite them in
- Address exclusionary behavior immediately

### Remote Work Considerations

**The Remote Challenge:**
Creating psychological safety within remote teams requires organizations to rethink the way they communicate and manage expectations. Leaders must view remote work as a reason to be more deliberate about culture, trust, and accountability.

**Deliberate Practices for Remote Teams:**

**Structured Connection:**
- Regular team meetings with clear purposes
- Virtual coffee chats and social time
- Async standups for different time zones
- Team bonding activities adapted for remote

**Over-Communication:**
- Document decisions and context
- Use video when possible for nuanced conversations
- Create space for casual conversation
- Share context liberally

**Inclusive Meetings:**
- Send agendas in advance
- Use collaborative tools (shared docs, virtual whiteboards)
- Ensure everyone can contribute (chat, reactions, speaking)
- Record for those who can't attend

**Visibility Without Surveillance:**
- Focus on outcomes, not activity
- Trust by default
- Async updates instead of constant check-ins
- Respect boundaries and time zones

### Building Strong Engineering Culture

**Core Elements:**

**1. Shared Values**
Define what matters to your team:
- Technical excellence
- Continuous learning
- Collaboration and support
- Customer focus
- Innovation and experimentation
- Work-life balance

**2. Rituals and Practices**
Create consistent experiences:
- Code review standards and norms
- Demo days or show-and-tells
- Retrospectives with real action items
- Celebration of wins and milestones
- Knowledge sharing sessions

**3. Stories and Heroes**
Build culture through narratives:
- Share stories of overcoming challenges
- Recognize exemplary behavior
- Celebrate diverse contributions
- Make heroes of culture carriers

**4. Artifacts and Symbols**
Make culture visible:
- Team principles or values documentation
- Architecture decision records
- Engineering blog posts
- Internal tech talks and presentations

### Fostering Collaboration

**Cross-functional Collaboration:**
- Embed engineers in product discussions early
- Create shared goals with product and design
- Joint retrospectives across disciplines
- Mutual respect and understanding

**Peer Collaboration:**
- Pair programming opportunities
- Code review as dialogue, not gatekeeping
- Mob programming for complex problems
- Cross-team knowledge sharing

**Knowledge Sharing:**
- Internal tech talks and brown bags
- Documentation culture
- Architecture decision records
- Post-mortems and lessons learned

### Maintaining Culture at Scale

**As Teams Grow:**

**Preserve What Matters:**
- Document culture and values explicitly
- Onboard new members into culture
- Tell stories that illustrate values
- Reinforce through recognition and decisions

**Adapt What Doesn't:**
- Some practices don't scale (all-hands standups)
- Create new rituals for larger teams
- Maintain small team feel through subgroups
- Balance consistency with team autonomy

**Leadership Alignment:**
- All managers must model values
- Consistent messaging across teams
- Address culture violations quickly
- Hire and promote for culture fit and add

### Measuring Culture and Psychological Safety

**Survey Questions:**
- "I feel safe taking risks on this team"
- "Team members value my unique skills and talents"
- "When I make a mistake, it's not held against me"
- "I can bring up problems and tough issues"
- "People on this team support each other"

**Observable Indicators:**
- People speak up in meetings
- Healthy debate and disagreement
- People admit mistakes openly
- New ideas are welcomed and tried
- Diverse viewpoints are sought
- Team members help each other

**Action Items from Results:**
- Share results transparently
- Discuss as team what to improve
- Create concrete action items
- Follow up and measure progress
- Celebrate improvements

### Addressing Culture Issues

**Warning Signs:**
- Low engagement in meetings
- Lack of collaboration
- High turnover
- Conflicts unresolved or swept under rug
- Blame culture emerging
- People afraid to share bad news

**Intervention Strategies:**
- Address issues promptly
- Have explicit conversations about culture
- Model desired behaviors consistently
- Reset norms if needed
- Bring in external facilitation if helpful
- Make hard decisions about culture fit

---
## Project Planning & Estimation

### The Reality of Software Estimation

**The Challenge:**
A McKinsey study found that 66% of software projects have cost overruns, with a third going beyond estimated schedules and almost 20% falling short of promised benefits.

**Why Estimation Is Hard:**
- Requirements change during development
- Unknown unknowns emerge
- Technical complexity is hard to predict
- Team capacity varies
- Dependencies and blockers arise

**The Goal:**
Project estimation means making a realistic prediction about the time, effort, and resources needed to bring a software project to life—not perfect predictions, but reasonable ones that enable good decisions.

### Estimation for Different Contexts

**Roadmap-Level Planning:**

**The Key Insight:**
Estimating is perhaps the biggest issue facing product managers regarding product and portfolio roadmaps. For roadmap-level planning, you don't need person-hour estimates; you just need an idea of whether it's a month or a year.

**Practical Approach:**
- Experienced teams can quickly estimate roadmap items by fiscal quarters
- Use "shirt sizes" (S, M, L, XL) for rough magnitude
- Focus on relative sizing, not absolute precision
- Re-estimate as you get closer and learn more

**Sprint/Feature-Level Planning:**

**More Precision Needed:**
- Fibonacci numbering (1, 2, 3, 5, 8, 13, 21) for story points
- Planning poker for team alignment
- Break down into smaller, estimable pieces
- Track actual vs. estimated to improve

### Common Estimation Techniques

**Planning Poker:**
- Team-based estimation approach
- Each person estimates independently
- Reveal simultaneously to avoid anchoring
- Discuss differences and converge
- Builds shared understanding

**T-Shirt Sizing:**
- Quick, rough estimates (XS, S, M, L, XL)
- Good for initial roadmap planning
- Easy for non-technical stakeholders
- Convert to time ranges as needed

**Work Breakdown Structure (WBS):**
- Create hierarchy of deliverables
- Break down to tasks and subtasks
- Estimate at granular level
- Roll up to project total
- Helps identify forgotten work

**Three-Point Estimation:**
- Optimistic scenario (best case)
- Pessimistic scenario (worst case)
- Most likely scenario
- Calculate weighted average
- Provides range, not single number

### Building Accurate Estimates

**The Planning Phase:**
Typically 40% of total estimation effort should focus on:
- Defining product scope
- Creating project charters
- Communicating with stakeholders
- Outlining the project roadmap
- Identifying dependencies and risks

**Strategies for Accuracy:**

**1. Break Work Down**
- Smaller pieces are easier to estimate
- Reduces unknown unknowns
- Easier to identify dependencies
- Better visibility into progress

**2. Incorporate Buffer Time**
- Add padding for uncertainty
- Don't pad every estimate (creates inflation)
- Use project-level buffers instead
- Be transparent about confidence levels

**3. Use Historical Data**
- Track actual vs. estimated
- Learn from past projects
- Build estimation database
- Improve over time

**4. Include the Team**
- People doing the work should estimate
- Builds commitment and buy-in
- Leverages diverse perspectives
- Catches assumptions and gaps

**5. Regular Progress Tracking**
- Monitor actual vs. estimated frequently
- Adjust forecasts as you learn
- Communicate changes proactively
- Learn from variances

### Creating and Managing Roadmaps

**What Roadmaps Should Contain:**

**Goals:**
- Business objectives driving the work
- Success criteria
- Strategic alignment

**Functionality:**
- Key components and features
- Prioritized by value and dependencies
- Enough detail for understanding, not implementation

**Timelines:**
- Estimated timeframes for features or milestones
- Quarters or months, not days
- Show dependencies and sequencing
- Include flexibility and buffers

**Prioritization:**
- Based on customer demands
- Business value assessment
- Technical complexity and risk
- Dependencies and sequencing

### Agile Quarterly Planning

**Long-Term Planning in Agile:**
Balance agility with predictability through quarterly planning:

**The Process:**

**1. Vision and Goals**
- What are we trying to achieve?
- How does it align with company objectives?
- What outcomes define success?

**2. Capacity Planning**
- How much team capacity available?
- Account for vacations, holidays, meetings
- Consider technical debt and maintenance
- Buffer for unexpected work

**3. Feature Prioritization**
- Stack rank by value and urgency
- Consider dependencies and risks
- Balance new features with tech debt
- Get stakeholder alignment

**4. Rough Sizing**
- T-shirt sizes or quarters
- Identify big vs. small initiatives
- Flag high-uncertainty items
- Create confidence levels

**5. Create Roadmap**
- Map features to quarters
- Show dependencies
- Communicate assumptions
- Provide ranges, not commitments

**6. Review and Adjust**
- Monthly or bi-monthly roadmap reviews
- Adjust based on learnings
- Communicate changes
- Maintain flexibility

### Managing Scope and Changes

**The Iron Triangle:**
Balance three constraints:
- Scope (features and quality)
- Time (schedule)
- Resources (people and budget)

**Trade-off Discussions:**
When something changes, discuss impact on all three:
- Add scope → extend time or add resources
- Compress time → reduce scope or add resources
- Fixed resources → adjust scope or timeline

**Change Management:**
- Establish change request process
- Assess impact before agreeing
- Communicate changes to stakeholders
- Update estimates and roadmap
- Learn from changes for future planning

### Communicating Estimates and Plans

**To Executives:**
- Focus on business outcomes and timelines
- Provide ranges, not single dates
- Explain key dependencies and risks
- Show how scope affects delivery
- Regular updates on changes

**To Product Partners:**
- Collaborative prioritization
- Transparent about capacity
- Clear about trade-offs
- Explain technical constraints
- Joint ownership of roadmap

**To Engineering Team:**
- Context for priorities
- Involvement in estimation
- Clarity on scope and goals
- Space for technical needs
- Realistic expectations

### Common Pitfalls

**Estimation Anti-patterns:**

**The "Pad Everything" Trap:**
- Every estimate gets doubled "to be safe"
- Creates loss of credibility
- Stakeholders learn to divide by 2
- Better to provide ranges

**The "Commitment Over Estimate" Trap:**
- Treating estimates as promises
- Removes learning and adjustment
- Creates pressure to hide problems
- Better to update forecasts as you learn

**The "False Precision" Trap:**
- "This will take 37.5 hours"
- Implies certainty that doesn't exist
- Better to provide ranges and confidence levels

**The "Planning Theater" Trap:**
- Spending weeks on detailed plans
- Plans immediately become outdated
- Better to plan iteratively

---
## Common Pitfalls & How to Avoid Them

Leadership is a learned skill, not something that comes naturally, and is uniquely challenging in any industry. Here are the most common mistakes engineering managers make and how to avoid them.

### 1. Doing Too Much Technical Work

**The Problem:**
This is identified as the #1 mistake of new engineering managers. The 'tech lead manager' concept often doesn't work well in the long run. Many managers try to go back to coding every chance they get, but coding and leadership require different parts of the brain and different mindsets.

**Why It Happens:**
- Comfort zone—you're good at coding
- Imposter syndrome about management skills
- Desire to "stay technical"
- Belief that you need to code to maintain credibility

**The Impact:**
- Prevents development of crucial management skills
- Creates bottlenecks in the team
- Reduces team autonomy
- You become a single point of failure
- Management responsibilities suffer

**The Solution:**
- Stay technical enough to make informed decisions
- Review code and architecture, but don't be on the critical path
- Focus on strategy, standards, and mentoring
- Trust your team to implement
- Measure your value by team output, not your code output
- Deliberately practice management skills

### 2. Neglecting One-on-One Meetings

**The Problem:**
Common mistakes include not having one-on-one sessions or having them only sporadically because new managers think they are not important. Another mistake is turning these sessions into status reports about ongoing projects.

**Why It Happens:**
- Feels less urgent than tactical work
- Unclear on what to discuss
- Uncomfortable with personal conversations
- "We talk all day anyway"

**The Impact:**
- Miss early warning signs of problems
- Team members feel unsupported
- No space for career development
- Issues fester until they explode
- Loss of trust

**The Solution:**
- Schedule weekly or bi-weekly 1:1s
- Protect this time—don't cancel
- Let direct reports drive agenda
- Focus on them, not status updates
- Ask about challenges, growth, well-being
- Take notes and follow through

### 3. Not Seeking Feedback

**The Problem:**
New managers often fail to dive into studying management the way they might learn a new framework or language. Not asking for feedback is a key mistake—managers should ask for performance reviews from people within and outside their team.

**Why It Happens:**
- Fear of negative feedback
- Belief that managers should have all answers
- Not knowing how to ask
- Organizational culture doesn't encourage it

**The Impact:**
- Blindspots persist and grow
- No improvement in management skills
- Team suffers from repeated mistakes
- Miss opportunities to build trust

**The Solution:**
- Regularly ask team: "What could I do better to support you?"
- Seek feedback from peers and manager
- Use anonymous surveys for honesty
- Thank people for feedback
- Act on feedback received
- Treat management as a skill to develop, like any other

### 4. Poor Communication

**The Problem:**
It's crucial to over-communicate what you're doing; otherwise, your team might feel like they don't know what's going on and wonder if you're leading them properly.

**Why It Happens:**
- Assume everyone knows what you know
- Too busy to communicate
- Unclear on what to share
- Fear of over-sharing

**The Impact:**
- Team uncertainty and anxiety
- Misalignment on priorities
- Decisions seem arbitrary
- Loss of trust and confidence

**The Solution:**
- Over-communicate rather than under-communicate
- Repeat important information
- Use multiple channels (meetings, email, Slack, docs)
- Explain the "why" behind decisions
- Provide context regularly
- Ask "what's unclear?" frequently

### 5. Avoiding Difficult Feedback

**The Problem:**
"In the moment, it's usually easier to let bad work slide than to address it, but this is a recipe for disaster." First-time managers may have anxiety delivering constructive criticism and might be tempted to avoid confrontation, which feels comfortable in the moment but is worse for the team in the long run.

**Why It Happens:**
- Want to be liked
- Fear of confrontation
- Uncomfortable with difficult conversations
- Hope problems will resolve themselves

**The Impact:**
- Poor performance continues
- Team morale suffers
- Good performers get frustrated
- Problems compound over time
- Eventually forced into more difficult conversations

**The Solution:**
- Address issues promptly, not months later
- Be direct but kind (Radical Candor)
- Focus on behavior and impact
- Provide specific examples
- Offer support for improvement
- Remember: clarity is kindness

### 6. Micromanaging

**The Problem:**
Micromanaging is a common mistake—you need to let people make their own mistakes while also providing a clear path forward with checkpoints.

**Why It Happens:**
- Lack of trust in team
- High stakes and anxiety
- Perfectionistic tendencies
- Unclear delegation
- Loss of control anxiety

**The Impact:**
- Team lacks autonomy
- Stifles creativity and growth
- Demotivates team members
- Creates dependency on you
- Limits scalability
- Talent leaves for better opportunities

**The Solution:**
- Define clear outcomes, not processes
- Set checkpoints without hovering
- Trust and verify
- Let people make mistakes (within bounds)
- Focus on developing people, not controlling work
- Coach, don't dictate

### 7. Lack of Empathy

**The Problem:**
Three things to look for in a person are authenticity, logic, and empathy, and with engineers, it's usually empathy where they're weakest.

**Why It Happens:**
- Technical background prioritizes logic
- Not taught or modeled
- Seen as "soft" or less important
- Discomfort with emotions

**The Impact:**
- Can't build trust
- Miss burnout signals
- Ineffective feedback
- Poor team culture
- High turnover

**The Solution:**
- Actively develop emotional intelligence
- Practice active listening
- Consider impact on individuals
- Recognize everyone's unique situation
- Balance logic with human considerations
- Model vulnerability

### 8. Trying to Do Everything Yourself

**The Problem:**
Not delegating effectively and trying to maintain control of all work.

**Why It Happens:**
- "It's faster if I do it"
- Don't want to burden team
- Lack of trust
- Unclear how to delegate

**The Impact:**
- Burnout
- Team doesn't develop
- Bottleneck in the organization
- Can't scale

**The Solution:**
- Delegate work that develops others
- Provide context and support
- Accept 80% solutions
- Build team capability
- Focus on your unique value

### 9. Ignoring Technical Debt

**The Problem:**
Always prioritizing new features over technical health and infrastructure improvements.

**Why It Happens:**
- Pressure from stakeholders
- Visible vs. invisible work
- Short-term thinking
- Difficulty explaining value

**The Impact:**
- Velocity slows over time
- Quality degrades
- Team morale suffers
- Eventually forced to stop and fix

**The Solution:**
- Make technical debt visible
- Allocate regular time (e.g., 20% of capacity)
- Connect tech debt to business impact
- Balance new work with sustainability
- Educate stakeholders on long-term costs

### 10. Not Managing Up

**The Problem:**
Failing to keep your manager and stakeholders informed and aligned.

**Why It Happens:**
- Focus all energy on team
- Assume manager knows what you're doing
- Uncomfortable with "politics"
- Don't see it as important

**The Impact:**
- Lack of support when needed
- Misalignment on priorities
- Missed opportunities
- Manager surprised by problems
- Limited career growth

**The Solution:**
- Regular updates to your manager
- Proactively communicate risks and issues
- Seek guidance on priorities
- Build relationships with stakeholders
- Make your work and team visible
- Advocate for your team's needs

### Self-Reflection Questions

Regularly ask yourself:

**On Technical Work:**
- Am I coding more than leading?
- Is my coding creating dependencies?
- Could someone else do this work?

**On People:**
- When did I last have meaningful 1:1s?
- Am I avoiding any difficult conversations?
- Do I know what motivates each team member?

**On Communication:**
- Does my team know my priorities?
- Am I explaining the "why"?
- Have I over-communicated recently?

**On Growth:**
- What management skill am I developing?
- When did I last seek feedback?
- What's my biggest blindspot?

**On Impact:**
- Is my team more effective because of me?
- What blockers have I removed recently?
- Am I enabling or constraining my team?

---
## Resources & Further Learning

### Books

**Engineering Management:**
- "The Manager's Path" by Camille Fournier
- "An Elegant Puzzle: Systems of Engineering Management" by Will Larson
- "The Making of a Manager" by Julie Zhuo
- "Radical Candor" by Kim Scott
- "Turn the Ship Around!" by L. David Marquet

**Leadership & People:**
- "Drive" by Daniel Pink
- "Leaders Eat Last" by Simon Sinek
- "Crucial Conversations" by Kerry Patterson
- "Thanks for the Feedback" by Douglas Stone & Sheila Heen

**Technical & Agile:**
- "Accelerate" by Nicole Forsgren, Jez Humble, and Gene Kim
- "The Phoenix Project" by Gene Kim
- "Team Topologies" by Matthew Skelton and Manuel Pais
- "Scrum: The Art of Doing Twice the Work in Half the Time" by Jeff Sutherland

### Online Resources

**Blogs & Publications:**
- LeadDev (leaddev.com)
- The Pragmatic Engineer (blog.pragmaticengineer.com)
- Lara Hogan (larahogan.me)
- Charity Majors (charity.wtf)
- Will Larson (lethain.com)
- Engineering Management (medium.com/engineering-management)

**Newsletters:**
- Software Lead Weekly
- Level Up
- The Pragmatic Engineer Newsletter
- TLDR Newsletter (tech news)

**Podcasts:**
- Manager Tools
- Engineering Enablement
- The Engineering Leadership Podcast
- Software Engineering Daily

### Communities & Networks

**Online Communities:**
- Rands Leadership Slack
- Engineering Managers Slack groups
- Reddit: r/ExperiencedDevs, r/engineering_management
- LeadDev community
- CTO Craft community

**Professional Organizations:**
- IEEE Computer Society
- ACM (Association for Computing Machinery)
- Project Management Institute (PMI)
- Scrum Alliance

### Certifications

**Agile & Project Management:**
- Certified Scrum Master (CSM) - Scrum Alliance
- Professional Scrum Master (PSM) - Scrum.org
- SAFe certifications for scaled agile
- Project Management Professional (PMP) - PMI
- Agile Certified Practitioner (PMI-ACP)

**Cloud & Technical:**
- AWS Certified Solutions Architect
- Azure Administrator/Solutions Architect
- Google Cloud Professional Cloud Architect
- Kubernetes certifications (CKA, CKAD)

**Leadership:**
- Various MBA and executive education programs
- Leadership development programs from universities

### Conferences & Events

**Engineering Leadership:**
- LeadDev conferences (various locations)
- QCon (software development conference)
- Craft Conference
- Engineering Leadership Conference
- Local engineering manager meetups

**Technical:**
- KubeCon
- AWS re:Invent
- Google I/O
- Microsoft Build
- DevOps Enterprise Summit

**Agile:**
- Agile Alliance conferences
- Scrum Gatherings
- Regional agile conferences

### Courses & Training

**Online Learning Platforms:**
- Pluralsight (technical and leadership courses)
- LinkedIn Learning (management courses)
- Coursera (leadership and management specializations)
- Udemy (specific technical and management topics)
- Reforge (product and growth programs)

**Specialized Training:**
- Crucial Conversations training
- Radical Candor workshops
- Leadership development programs
- Executive coaching

### Tools & Software

**Team Management:**
- Jira (project tracking)
- Linear (modern project management)
- Asana (task management)
- Monday.com (work operating system)

**Communication:**
- Slack (team communication)
- Microsoft Teams
- Zoom (video conferencing)
- Loom (async video communication)

**Documentation:**
- Notion (knowledge management)
- Confluence (team documentation)
- GitBook (product docs)
- Coda (collaborative docs)

**Engineering Metrics:**
- LinearB (engineering metrics)
- Jellyfish (engineering analytics)
- Swarmia (developer productivity)
- Haystack (engineering effectiveness)

**Performance Management:**
- Lattice (performance reviews)
- Culture Amp (engagement surveys)
- 15Five (continuous feedback)
- Small Improvements (performance management)

### Research & Studies

**Key Studies to Read:**
- Google's Project Aristotle (team effectiveness)
- DORA State of DevOps reports (annual)
- Stack Overflow Developer Survey (annual)
- GitLab Remote Work Report (annual)
- Accelerate research (DevOps performance)

### Mental Models & Frameworks

**To Study:**
- DORA metrics framework
- Team Topologies patterns
- Situational Leadership model
- Radical Candor framework
- OKRs (Objectives and Key Results)
- Three P Model (People, Process, Purpose)
- STAR method (behavioral interviews)
- Eisenhower Matrix (prioritization)
- RACI matrix (responsibility assignment)

---

## Conclusion

Being a top-class software development manager is a journey of continuous learning and growth. Success requires balancing technical expertise with people leadership, maintaining strategic vision while supporting day-to-day execution, and creating environments where teams can do their best work.

**Key Takeaways:**

1. **Emotional intelligence and empathy** are as important as technical skills
2. **Trust and psychological safety** are the foundation of high-performing teams
3. **Communication must be intentional**, especially in remote environments
4. **Continuous feedback** is more effective than annual reviews
5. **Use metrics for improvement**, not punishment
6. **Delegate effectively** and avoid micromanaging
7. **Stay technical enough** to be credible without becoming a bottleneck
8. **Invest in people's growth** through mentoring, coaching, and sponsorship
9. **Avoid common pitfalls** through self-awareness and seeking feedback
10. **Keep learning and adapting** as technology and practices evolve

The most effective engineering managers create leverage by:
- Removing blockers rather than doing all the work
- Developing others rather than hoarding knowledge
- Building systems and culture rather than fighting fires
- Focusing on outcomes rather than activity
- Empowering teams rather than controlling them

Remember: your success is measured by your team's success. Focus on enabling, supporting, and growing the people around you, and the results will follow.

---

## About This Research

**Created:** November 22, 2025

**Research Sources:**
This comprehensive guide synthesizes information from over 50 current industry sources, including:
- Academic research (Google Project Aristotle, McKinsey studies)
- Industry reports (DORA, Stack Overflow, GitLab)
- Expert practitioners (LeadDev, The Pragmatic Engineer, Arc.dev)
- Leading tech companies (Google, Microsoft, Atlassian)
- Professional organizations (PMI, Scrum Alliance, IEEE)

All findings represent current best practices and trends as of 2025, with particular attention to the realities of distributed teams and modern software development practices.

## Research Sources

This research drew from the following sources:

### Leadership & Management Skills
- [Software Engineering Manager Skills in 2025 (Top + Most Underrated Skills)](https://www.tealhq.com/skills/software-engineering-manager)
- [7 essential software development leadership skills for success | Lumenalta](https://lumenalta.com/insights/7-essential-software-development-leadership-skills-for-success)
- [5 Skills Required from Every IT Leader [2025]](https://brainhub.eu/library/become-better-it-leader-five-skills)
- [10 Leadership Traits for Software Development Leaders - 3Pillar](https://www.3pillarglobal.com/insights/blog/10-leadership-traits-for-modern-software-development-leaders/)
- [12 Essential Skills Every Software Development Manager Needs](https://www.nucamp.co/blog/12-skills-for-software-development-manager)

### People Management
- [How to Be an Engineering Manager Your Company & Team Respects](https://arc.dev/employer-blog/how-to-be-a-great-engineering-manager/)
- [Engineering Manager Skills 101: Communication, Delegation, Strategy](https://medium.com/engineering-managers-journal/engineering-manager-skills-101-communication-delegation-strategy-723277e1ceec)
- [Effective Engineering Manager Tips To Keep In Mind | Built In](https://builtin.com/software-engineering-perspectives/career-advice-for-engineering-managers)
- [What Makes a Good Engineering Manager? 12 Traits You Need | LinearB Blog](https://linearb.io/blog/what-makes-a-good-engineering-manager-12-traits-you-need)

### Technical Competencies
- [15 Software Development Manager Skills For Your Resume - Zippia](https://www.zippia.com/software-development-manager-jobs/skills/)
- [5 Crucial Software Engineering Manager Skills to Have & Improve in 2022](https://arc.dev/developer-blog/software-engineering-manager-skills/)
- [The Ultimate Software Development Manager Career Guide](https://www.4cornerresources.com/career-guides/software-development-manager/)

### Agile & Scrum
- [Scrum | Atlassian](https://www.atlassian.com/agile/scrum)
- [Agile in 2025: 8 Trends Reshaping Software Development and Delivery | Easy Agile](https://www.easyagile.com/blog/agile-trends-predictions-2025)
- [What Is Scrum Methodology? Complete Guide For 2025](https://thedigitalprojectmanager.com/project-management/scrum-methodology-complete-guide/)
- [Agile Software Development 101: Principles and Practices for 2025](https://monday.com/blog/rnd/agile-software-development/)

### Hiring & Interviews
- [Software Engineer interviews: Everything you need to prepare | Tech Interview Handbook](https://www.techinterviewhandbook.org/software-engineering-interview-guide/)
- [Software engineering hiring best practices to find top talent - BrightHire](https://brighthire.com/blog/engineering-hiring-best-practices/)
- [The Ultimate Guide To A Smooth Software Engineer Interview Process](https://www.paraform.com/blog/software-engineer-interview-process)

### Metrics & KPIs
- [Top 40 Engineering KPIs and Metric Examples for 2025 Reporting](https://insightsoftware.com/blog/top-engineering-kpis-and-metric-examples/)
- [Engineering KPIs: A complete guide to measuring productivity and AI impact](https://getdx.com/blog/engineering-kpis/)
- [10 Engineering Metrics for Team Success in 2025](https://monday.com/blog/rnd/engineering-metrics/)
- [Engineering KPIs: How to Align Metrics with Team Performance](https://teamhood.com/engineering/engineering-kpis/)

### Communication & Stakeholder Management
- [4 strategies for effectively managing stakeholders - LeadDev](https://leaddev.com/communication/4-strategies-effectively-managing-stakeholders)
- [Mastering Stakeholder Management: A Guide for Engineering Leaders - Sundeep Teki](https://www.sundeepteki.org/blog/how-to-manage-stakeholders-effectively)
- [Stakeholder Management For Engineering Leads | by Nitin Dhar](https://medium.com/one-to-n/stakeholder-management-for-engineering-leads-733f2938fc6c)

### Performance Management & Feedback
- [Performance Reviews for Software Developers – How I Do Them In a (Hopefully) Fair Way - The Pragmatic Engineer](https://blog.pragmaticengineer.com/performance-reviews-for-software-engineers/)
- [Software Developer Performance Review: 6 Feedback Examples](https://echometerapp.com/en/software-developer-performance-review-6-feedback-examples/)
- [How To Conduct a Software Engineer Performance Review | Indeed.com](https://www.indeed.com/career-advice/career-development/software-engineer-performance-review)

### Career Development & Mentoring
- [Mentor, coach, sponsor: a guide to developing engineers | LeadDev](https://leaddev.com/mentoring-coaching-feedback/mentor-coach-sponsor-guide-developing-engineers)
- [How to start an engineering mentorship program | Together Mentoring Software](https://www.togetherplatform.com/blog/engineering-mentorship-program)
- [Key Components of an Engineering Growth Framework | Adeva](https://adevait.com/leadership/key-components-engineering-growth-framework)
- [Retain & Develop Engineers With Mentoring | Guider AI](https://guider-ai.com/blog/retain-and-develop-engineers-with-mentoring/)

### Team Culture & Psychological Safety
- [Psychological Safety Virtual Teams](https://www.leaderfactor.com/learn/psychological-safety-virtual-teams)
- [A Comprehensive Guide to Build A Strong Remote Engineering Culture](https://fullscale.io/blog/build-strong-remote-engineering-culture/)
- [Psychological Safety in Remote and Virtual Teams - Psych Safety](https://psychsafety.com/psychological-safety-in-remote-teams/)
- [How to maintain psychological safety in a hybrid workplace - Work Life by Atlassian](https://www.atlassian.com/blog/distributed-work/maintain-psychological-safety-in-a-hybrid-workplace)

### Project Planning & Estimation
- [Project Estimation: Process, Methods and Examples](https://www.upsilonit.com/blog/how-to-make-accurate-project-estimations)
- [Software Project Estimation Guide for Methods and Techniques](https://www.excellentwebworld.com/software-projects-estimation/)
- [How to Estimate Items on Your Roadmap - Applied Frameworks](https://appliedframeworks.com/blog/how-to-estimate-items-on-your-roadmap)
- [Effective Software Project Planning: The Ultimate Guide](https://www.netguru.com/blog/software-project-planning)
- [Agile quarterly planning: 8 steps to start long-term agile planning | Atlassian](https://www.atlassian.com/agile/agile-at-scale/long-term-agile-planning)

### Common Mistakes
- [The 5 Common Mistakes Of New Engineering Managers](https://leadership.garden/the-5-common-mistakes-of-new-engineering-managers/)
- [3 Common Pitfalls of New Engineering Managers…and How to Get Over Them — ManageBetter](https://managebetter.com/blog/3-common-pitfalls-of-new-engineering-managersand-how-to-get-over-them)
- [5 Mistakes That Engineering Managers Make | Tech Leadership Advice & Resources](https://eisabainyo.net/weblog/2020/10/15/5-mistakes-that-engineering-managers-make/)
- [Mistakes I've Made as an Engineering Manager | CSS-Tricks](https://css-tricks.com/mistakes-ive-made-as-an-engineering-manager/)
- [Software Engineering Management Mistakes to Avoid | Codility](https://www.codility.com/blog/the-top-mistakes-that-engineering-managers-make/)

---
