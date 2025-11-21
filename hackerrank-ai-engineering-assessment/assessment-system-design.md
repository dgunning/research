# System Design Skills Assessment

**Assessment Area**: Scalability, Reliability, Observability
**Target Role**: Principal AI Engineer at Thomson Reuters
**Date**: November 2025

## Purpose

This assessment evaluates your system design capabilities for building large-scale, production-ready AI systems. As a Principal Engineer, you'll architect systems serving millions of users with strict SLAs.

---

## Assessment Framework

**Scoring Guide:**
- **5 - Expert**: Can architect complex distributed systems, anticipate edge cases, mentor others
- **4 - Advanced**: Strong system design skills, can lead architecture decisions
- **3 - Proficient**: Solid understanding, can design systems with guidance
- **2 - Developing**: Basic knowledge, needs significant support
- **1 - Awareness**: Familiar with concepts, limited practical experience

---

## Part 1: Scalability

### 1.1 Horizontal vs. Vertical Scaling

**Self-Assessment Questions:**

1. **Scaling Strategies** (Score: ___/5)
   - Can you design horizontally scalable ML inference services?
   - When would you choose vertical scaling over horizontal?
   - How do you handle stateful components in distributed systems?
   - Explain auto-scaling strategies for ML workloads

2. **Load Balancing** (Score: ___/5)
   - What load balancing algorithms work best for ML services?
   - How do you handle sticky sessions when needed?
   - How do you implement health checks for ML endpoints?
   - Explain blue-green and canary deployments

3. **Database Scaling** (Score: ___/5)
   - How do you scale relational databases for read-heavy workloads?
   - When would you use read replicas vs. sharding?
   - How do you handle distributed transactions?
   - Explain CAP theorem tradeoffs in practice

**System Design Challenge 1:**

```
Scenario: Design CoCounsel's document analysis service to handle:
- 10,000 concurrent users
- 100,000 documents/day
- <2s response time (p95)
- Documents range from 1 page to 1000+ pages
- Peak load: 10x average during business hours (9am-5pm EST)

Requirements:
1. Draw the system architecture
2. Explain scaling strategy
3. Calculate infrastructure requirements
4. Design for cost efficiency
```

**Your Architecture:**
[Diagram here - describe in text or draw]

**Components to Address:**
- Load balancer configuration
- Service tier (ECS/Fargate, Lambda, EC2)
- Auto-scaling policies
- Database architecture
- Caching strategy
- Queue system for async processing
- Cost optimization (spot instances, reserved capacity)

**Expected Capacity Planning:**
- Average: 100K docs / 24 hrs = ~70 docs/min
- Peak: 700 docs/min
- If each doc takes 5s to process: need ~60 concurrent workers
- With 10x peak buffer: 600 workers
- Right-size: containers vs. serverless tradeoff

---

### 1.2 Distributed Systems

**Self-Assessment Questions:**

1. **Consistency Models** (Score: ___/5)
   - Can you explain strong vs. eventual consistency?
   - How do you handle distributed transactions?
   - What's your approach to conflict resolution?
   - Explain consensus algorithms (Paxos, Raft)

2. **Data Partitioning** (Score: ___/5)
   - How do you design sharding strategies?
   - What's your approach to handling hot partitions?
   - How do you rebalance shards?
   - Explain consistent hashing

3. **Distributed Computing** (Score: ___/5)
   - How do you design MapReduce-style workflows?
   - What's your experience with Spark, EMR, Glue?
   - How do you handle stragglers in distributed jobs?
   - Explain backpressure and flow control

**System Design Challenge 2:**

```
Scenario: Design Westlaw's vector search system:
- 100M+ legal documents embedded
- 1M+ searches/day
- <500ms search latency (p95)
- Real-time index updates (1000 new docs/hour)
- Multi-tenant with data isolation

Requirements:
1. Design the indexing pipeline
2. Design the search architecture
3. Explain consistency guarantees
4. Handle tenant isolation
```

**Your Architecture:**
[Describe here]

**Key Decisions:**
- Vector database choice (OpenSearch, Pinecone, custom)
- Partitioning strategy (by tenant, by doc type, by date)
- Index update strategy (batch, streaming)
- Search routing and caching
- Consistency model (eventual vs. strong)
- Backup and disaster recovery

---

### 1.3 Performance Optimization

**Self-Assessment Questions:**

1. **Latency Optimization** (Score: ___/5)
   - How do you identify and fix performance bottlenecks?
   - What profiling tools do you use?
   - How do you optimize critical path latency?
   - Explain various caching strategies

2. **Throughput Optimization** (Score: ___/5)
   - How do you maximize system throughput?
   - What batching strategies work for ML workloads?
   - How do you optimize resource utilization?
   - How do you handle backlog and queuing?

3. **Resource Efficiency** (Score: ___/5)
   - How do you optimize CPU, memory, GPU usage?
   - What's your approach to rightsizing instances?
   - How do you identify waste and over-provisioning?
   - How do you balance cost and performance?

**Optimization Challenge:**

```
Scenario: RAG system performance issues:
- Current: 3s avg latency (target: 1s)
- Breakdown: 500ms retrieval, 2000ms LLM, 500ms overhead
- 10,000 requests/day
- Monthly cost: $50K (mostly LLM API)

Tasks:
1. Profile and identify bottlenecks
2. Propose optimizations for each component
3. Estimate impact on latency and cost
4. Design A/B testing approach
```

**Your Optimization Plan:**

**Retrieval (500ms → target: 200ms):**
- _______________
- _______________

**LLM (2000ms → target: 600ms):**
- _______________
- _______________

**Overhead (500ms → target: 200ms):**
- _______________
- _______________

**Expected Optimizations:**
- Retrieval: index optimization, caching, pre-filtering
- LLM: prompt compression, streaming, smaller models, caching
- Overhead: connection pooling, async processing, reduce hops

---

### 1.4 Caching Strategies

**Self-Assessment Questions:**

1. **Caching Patterns** (Score: ___/5)
   - Can you design multi-layer caching architectures?
   - How do you handle cache invalidation?
   - What's your approach to cache warming?
   - Explain different eviction policies

2. **Distributed Caching** (Score: ___/5)
   - How do you use Redis/Elasticache at scale?
   - What's your approach to cache consistency?
   - How do you handle cache stampede?
   - How do you partition cache across nodes?

**Caching Design Challenge:**

```
Scenario: CoCounsel queries are expensive but often repeated.
Analysis shows:
- 30% of queries are exact duplicates
- 50% are semantically similar (could use same retrieval)
- LLM costs dominate ($30K/month)

Tasks:
1. Design caching architecture
2. Define cache key strategy
3. Handle semantic similarity
4. Implement cache invalidation
```

**Your Caching Strategy:**
[Describe here]

---

## Part 2: Reliability

### 2.1 High Availability

**Self-Assessment Questions:**

1. **Availability Design** (Score: ___/5)
   - Can you design systems for 99.9%+ uptime?
   - How do you eliminate single points of failure?
   - What's your approach to multi-AZ/multi-region deployments?
   - How do you calculate availability SLAs?

2. **Failure Handling** (Score: ___/5)
   - How do you design for graceful degradation?
   - What's your circuit breaker strategy?
   - How do you implement retries and backoff?
   - How do you handle cascading failures?

3. **Disaster Recovery** (Score: ___/5)
   - What's your backup and restore strategy?
   - How do you implement active-active vs. active-passive DR?
   - How do you test disaster recovery?
   - What are your RPO and RTO targets?

**Reliability Challenge:**

```
Scenario: Design CoCounsel for 99.95% availability SLA.
Current architecture has single points of failure:
- Single-region deployment (us-east-1)
- Single database instance
- No fallback for LLM API outages

Requirements:
1. Design for 99.95% uptime
2. Eliminate SPOFs
3. Handle third-party service failures
4. Keep costs reasonable
```

**Your HA Architecture:**
[Describe here]

**Key Elements:**
- Multi-AZ deployment
- Database replication strategy
- LLM fallback (Bedrock → self-hosted)
- Health checks and auto-recovery
- Graceful degradation modes
- Chaos engineering tests

**Availability Calculation:**
```
Components:
- Load Balancer: 99.99% SLA
- ECS/Fargate: 99.99% (multi-AZ)
- Database: 99.95% (multi-AZ RDS)
- Bedrock: 99.9% SLA
- Overall: 99.99% × 99.99% × 99.95% × 99.9% = 99.83%

To reach 99.95%:
- Add database read replicas (failover)
- Add LLM fallback provider
- Implement circuit breakers
```

---

### 2.2 Fault Tolerance

**Self-Assessment Questions:**

1. **Error Handling** (Score: ___/5)
   - How do you design idempotent APIs?
   - What's your retry strategy for different failure modes?
   - How do you handle partial failures?
   - Explain saga pattern for distributed transactions

2. **Resilience Patterns** (Score: ___/5)
   - Can you implement bulkhead pattern?
   - How do you use circuit breakers effectively?
   - What's your approach to rate limiting?
   - How do you handle thundering herd?

3. **Data Integrity** (Score: ___/5)
   - How do you ensure data consistency during failures?
   - What's your approach to distributed transactions?
   - How do you handle split-brain scenarios?
   - How do you validate data integrity?

**Fault Tolerance Challenge:**

```
Scenario: CoCounsel document processing pipeline:
1. User uploads document → S3
2. Lambda triggers document parsing
3. Text extracted and chunked
4. Embeddings generated (SageMaker)
5. Stored in vector DB
6. User notified

Failures observed:
- Parsing fails on complex PDFs
- Embedding service times out occasionally
- Vector DB write failures
- Users not notified when process fails

Tasks:
1. Redesign for fault tolerance
2. Implement retry logic
3. Handle partial failures
4. Ensure user visibility
```

**Your Fault-Tolerant Design:**
[Describe here]

**Expected Patterns:**
- SQS/EventBridge for async processing
- Dead letter queues
- Exponential backoff with jitter
- Idempotent operations
- State machine (Step Functions)
- User notification system
- Manual retry interface

---

### 2.3 Testing for Reliability

**Self-Assessment Questions:**

1. **Chaos Engineering** (Score: ___/5)
   - How do you implement chaos testing?
   - What failure scenarios do you test?
   - How do you run chaos tests safely in production?
   - What tools do you use (Chaos Monkey, Gremlin)?

2. **Load Testing** (Score: ___/5)
   - How do you design realistic load tests?
   - What's your approach to stress testing?
   - How do you identify breaking points?
   - How do you test autoscaling?

3. **Resilience Testing** (Score: ___/5)
   - How do you test failover scenarios?
   - What's your disaster recovery testing strategy?
   - How do you validate backup/restore?
   - How do you test degraded modes?

**Testing Challenge:**

```
Scenario: Before launching new RAG feature, test reliability.

Design test plan covering:
1. Load testing (10x expected traffic)
2. Chaos testing (kill services, partition network)
3. Failover testing (region failure)
4. Performance testing under various conditions
```

**Your Test Plan:**
[Describe here]

---

## Part 3: Observability

### 3.1 Monitoring & Metrics

**Self-Assessment Questions:**

1. **Metrics Design** (Score: ___/5)
   - What metrics do you track for AI/ML systems?
   - How do you implement the Four Golden Signals?
   - What's your approach to custom business metrics?
   - How do you aggregate metrics across services?

2. **Monitoring Stack** (Score: ___/5)
   - Can you design monitoring architecture (CloudWatch, Prometheus, Datadog)?
   - How do you collect metrics at scale?
   - What's your metric retention strategy?
   - How do you handle metric cardinality?

3. **Visualization** (Score: ___/5)
   - How do you design effective dashboards?
   - What visualizations work best for different metrics?
   - How do you create role-specific views?
   - What tools do you use (Grafana, CloudWatch, Datadog)?

**Monitoring Challenge:**

```
Scenario: Design comprehensive monitoring for CoCounsel RAG system.

Required metrics:
- Latency (retrieval, LLM, total)
- Throughput (requests/sec)
- Error rates (by type)
- Model quality (relevance, accuracy)
- Cost (by component)
- User satisfaction

Tasks:
1. Define all metrics to track
2. Design collection architecture
3. Create dashboard layouts
4. Set up alerting (next section)
```

**Your Monitoring Strategy:**

**Infrastructure Metrics:**
- _______________

**Application Metrics:**
- _______________

**ML Metrics:**
- _______________

**Business Metrics:**
- _______________

**Expected Metrics:**

**Four Golden Signals:**
1. Latency: p50, p95, p99 response times
2. Traffic: requests/sec, documents/day
3. Errors: 4xx, 5xx rates, timeout rate
4. Saturation: CPU, memory, GPU utilization

**ML-Specific:**
- Retrieval quality (MRR, NDCG)
- Answer relevance scores
- Citation accuracy
- Hallucination rate
- Model drift indicators

**Business:**
- User engagement
- Query success rate
- Cost per query
- Revenue impact

---

### 3.2 Logging

**Self-Assessment Questions:**

1. **Logging Strategy** (Score: ___/5)
   - How do you design structured logging?
   - What log levels do you use and when?
   - How do you handle sensitive data in logs?
   - What's your log aggregation approach?

2. **Log Management** (Score: ___/5)
   - How do you collect logs at scale?
   - What's your log retention strategy?
   - How do you search logs efficiently?
   - How do you correlate logs across services?

3. **Audit Logging** (Score: ___/5)
   - How do you implement audit trails?
   - What events do you audit?
   - How do you ensure audit log integrity?
   - How do you make logs searchable for compliance?

**Logging Design Challenge:**

```
Scenario: CoCounsel must provide audit trail for legal compliance.

Requirements:
- Track all user queries and AI responses
- Log document access
- Record model versions used
- Support legal hold requests
- Retain for 7 years
- Search by user, time, document, query

Tasks:
1. Design logging architecture
2. Define log schema
3. Plan storage strategy
4. Implement search capability
```

**Your Logging Architecture:**
[Describe here]

**Key Components:**
- CloudWatch Logs vs. S3 vs. dedicated system
- Log levels and structure
- PII handling (masking, encryption)
- Retention and archival
- Search indexing (OpenSearch)
- Compliance controls

---

### 3.3 Tracing

**Self-Assessment Questions:**

1. **Distributed Tracing** (Score: ___/5)
   - Can you implement distributed tracing (X-Ray, Jaeger)?
   - How do you trace requests across microservices?
   - What's your sampling strategy?
   - How do you analyze trace data?

2. **Performance Analysis** (Score: ___/5)
   - How do you use tracing to identify bottlenecks?
   - What's your approach to profiling?
   - How do you correlate traces with metrics?
   - How do you track critical path latency?

**Tracing Challenge:**

```
Scenario: RAG request flow:
API Gateway → Lambda → SageMaker (embed) → OpenSearch → Bedrock → Response

Need to trace end-to-end to find latency issues.

Tasks:
1. Implement distributed tracing
2. Identify critical path
3. Set sampling rate
4. Create latency dashboard
```

**Your Tracing Strategy:**
[Describe here]

---

### 3.4 Alerting

**Self-Assessment Questions:**

1. **Alert Design** (Score: ___/5)
   - How do you design actionable alerts?
   - What's your approach to reducing alert fatigue?
   - How do you set thresholds and SLOs?
   - How do you escalate alerts?

2. **Incident Response** (Score: ___/5)
   - How do you integrate alerting with on-call?
   - What's your incident management process?
   - How do you conduct post-mortems?
   - How do you track MTTR and MTBF?

3. **SLOs and SLIs** (Score: ___/5)
   - Can you define SLIs and SLOs for AI systems?
   - How do you calculate error budgets?
   - What's your approach to SLO breaches?
   - How do you report on SLO compliance?

**Alerting Challenge:**

```
Scenario: Define alerting strategy for CoCounsel.

SLAs:
- 99.95% availability
- <2s response time (p95)
- <1% error rate

Tasks:
1. Define SLIs and SLOs
2. Create alert rules
3. Set up escalation
4. Design on-call rotation
```

**Your Alerting Strategy:**

**Critical Alerts (Page immediately):**
- _______________

**Warning Alerts (Ticket for next day):**
- _______________

**Info Alerts (Dashboard only):**
- _______________

**Expected Alerts:**

**Critical:**
- Error rate > 5% for 5 minutes
- Latency p95 > 5s for 10 minutes
- Service availability < 99%
- All instances unhealthy
- Database unavailable

**Warning:**
- Error rate > 1% for 30 minutes
- Latency p95 > 2s for 30 minutes
- High CPU/memory (> 80%)
- Approaching cost budget
- Model drift detected

**Info:**
- Deployment events
- Scaling events
- Cost anomalies
- Low-priority errors

---

## Part 4: System Design Scenarios

### Scenario 1: CoCounsel Global Expansion

```
Current: US-only, 10K users, single region (us-east-1)
Future: Global, 100K users, <2s latency worldwide

Design for:
1. Multi-region deployment
2. Data locality (GDPR, data residency)
3. Global load balancing
4. Consistent user experience
5. Cost efficiency
```

**Your Architecture:**
[Describe here]

**Key Decisions:**
- Region selection and routing
- Data replication strategy
- Model deployment approach
- Latency optimization
- Compliance handling

---

### Scenario 2: Westlaw Real-Time Updates

```
Current: Batch updates overnight (12-hour lag)
Future: Real-time updates as new laws/cases published

Design for:
1. Streaming ingestion pipeline
2. Incremental index updates
3. Eventual consistency handling
4. User notification of changes
5. Versioning and rollback
```

**Your Architecture:**
[Describe here]

---

### Scenario 3: Multi-Tenant SaaS Platform

```
Design Thomson Reuters AI Platform serving multiple products:
- CoCounsel (legal)
- Compliance solutions
- Tax research
- Financial analytics

Requirements:
1. Tenant isolation
2. Custom models per tenant
3. Usage tracking and billing
4. SLA guarantees per tier
5. Scalability to 1000+ tenants
```

**Your Architecture:**
[Describe here]

---

### Scenario 4: Cost Optimization

```
Current ML infrastructure costs: $2M/year
- SageMaker endpoints: $800K
- Bedrock API: $600K
- Data storage: $300K
- Compute: $300K

Leadership wants 40% reduction without quality loss.

Design optimization strategy:
1. Right-size infrastructure
2. Optimize ML serving
3. Reduce storage costs
4. Implement efficient caching
```

**Your Cost Optimization Plan:**
[Describe here]

---

## Part 5: Trade-offs and Decision Making

### 5.1 Architecture Decisions

**Self-Assessment Questions:**

1. **Design Trade-offs** (Score: ___/5)
   - How do you evaluate build vs. buy decisions?
   - What's your approach to selecting databases?
   - How do you choose between microservices and monolith?
   - How do you balance consistency and performance?

2. **Technology Selection** (Score: ___/5)
   - How do you evaluate new technologies?
   - What's your approach to managing technical debt?
   - How do you decide when to refactor?
   - How do you balance innovation and stability?

**Decision Framework:**

For each decision, evaluate:
1. **Requirements**: What are we optimizing for?
2. **Constraints**: Budget, time, team skills
3. **Options**: At least 3 alternatives
4. **Trade-offs**: Pros/cons of each
5. **Recommendation**: With justification
6. **Risks**: What could go wrong?

**Example Decision:**

```
Question: Should we build RAG in-house or use managed service?

Options:
A) Build on OpenSearch + self-hosted embeddings
B) Use Bedrock Knowledge Bases
C) Use third-party (Pinecone, Weaviate)

Evaluate using framework above.
```

**Your Analysis:**
[Describe here]

---

### 5.2 Scaling Decisions

**Questions:**

1. When would you scale vertically vs. horizontally?
2. At what point do you split a monolith?
3. How do you decide between SQL and NoSQL?
4. When do you introduce caching?
5. How do you know when to add a queue?

**Practice Scenario:**

```
Your service currently handles 100 req/sec on a single t3.large instance
at 60% CPU. Traffic is projected to 10x in 6 months.

Options:
A) Vertical: Move to larger instances
B) Horizontal: Add more t3.large instances
C) Hybrid: Move to c5.xlarge + horizontal scaling
D) Rewrite: Serverless (Lambda)

Analyze each option.
```

---

## Scoring & Gap Analysis

### Total Scores by Category

| Category | Your Score | Max Score | Percentage |
|----------|-----------|-----------|------------|
| Scalability | ___/35 | 35 | ___% |
| Reliability | ___/25 | 25 | ___% |
| Observability | ___/25 | 25 | ___% |
| Scenarios | ___/20 | 20 | ___% |
| Decision Making | ___/10 | 10 | ___% |
| **TOTAL** | ___/115 | 115 | ___% |

### Interpretation

- **85-100%**: Expert - Ready for principal-level system design
- **70-84%**: Advanced - Focus on weak areas
- **55-69%**: Proficient - Needs significant practice
- **<55%**: Developing - Study fundamentals

---

## Study Recommendations

### For Scores 1-2 (Developing)

**Resources:**
- "Designing Data-Intensive Applications" by Martin Kleppmann
- AWS Well-Architected Framework
- System Design Primer (GitHub)
- "Site Reliability Engineering" by Google
- AWS Architecture Center case studies

**Practice:**
- Complete 20+ system design problems
- Build and deploy scalable service
- Set up monitoring for personal project

---

### For Scores 3-4 (Proficient/Advanced)

**Resources:**
- "Building Microservices" by Sam Newman
- AWS re:Invent system design talks
- Company engineering blogs (Netflix, Uber, Meta)
- "Database Internals" by Alex Petrov

**Practice:**
- Design TR-specific systems
- Practice explaining trade-offs
- Mock system design interviews
- Study TR tech stack deeply

---

### For Scores 5 (Expert)

**Focus:**
- TR-specific architecture patterns
- Principal-level communication
- Practice teaching system design
- Review recent architecture decisions

---

## Interview Preparation Checklist

### System Design Interview Topics

- [ ] Design scalable RAG system (most likely question)
- [ ] Design real-time data pipeline
- [ ] Design multi-tenant SaaS platform
- [ ] Design global distributed system
- [ ] Cost optimization for ML infrastructure
- [ ] Design for 99.99% availability
- [ ] Design observability stack
- [ ] Migrate monolith to microservices
- [ ] Design ML model serving architecture
- [ ] Handle 10x traffic growth

### Key Discussion Points

- [ ] CAP theorem trade-offs
- [ ] Consistency models
- [ ] Caching strategies
- [ ] Database selection criteria
- [ ] Observability best practices
- [ ] Disaster recovery planning
- [ ] Cost vs. performance trade-offs
- [ ] Microservices vs. monolith
- [ ] Serverless vs. containers
- [ ] Build vs. buy decisions

### Preparation Activities

- [ ] Draw 10 different architectures
- [ ] Practice explaining trade-offs
- [ ] Review AWS services and limits
- [ ] Study TR architecture (from tech stack doc)
- [ ] Practice capacity planning
- [ ] Review observability tools
- [ ] Practice cost calculations
- [ ] Mock interviews with peers

---

## Practice Problems

### Problem 1: Design CoCounsel RAG System
- 100K users, 1M queries/month
- <2s latency, 99.9% uptime
- Draw architecture, explain scaling

### Problem 2: Design Document Processing Pipeline
- 1M documents/day
- OCR, classification, entity extraction
- Fault-tolerant, cost-effective

### Problem 3: Design ML Model Serving
- 50 different models
- 100K predictions/day
- A/B testing, monitoring, cost optimization

### Problem 4: Design Real-Time Analytics
- Ingest legal case data in real-time
- Process and index for search
- Dashboard with <5s lag

### Problem 5: Migrate to Multi-Region
- Current: us-east-1 only
- Target: Global with <500ms latency
- Handle data sovereignty, failover

---

## Notes & Reflections

**Date Completed**: _______________

**Overall Confidence Level** (1-5): ___

**Strongest Areas**:
1. _______________
2. _______________

**Areas for Improvement**:
1. _______________
2. _______________

**Study Plan** (Next 2 Weeks):
1. _______________
2. _______________
3. _______________

**Mock Interview Date**: _______________
