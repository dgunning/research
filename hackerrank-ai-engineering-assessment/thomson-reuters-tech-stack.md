# Thomson Reuters Tech Stack & Infrastructure

**Research Date:** November 21, 2025
**Purpose:** Comprehensive overview of Thomson Reuters' technology infrastructure for Principal AI Engineer interview preparation

---

## Executive Summary

Thomson Reuters operates on a **modern, cloud-native infrastructure** primarily built on **Amazon Web Services (AWS)**, with a strong focus on AI/ML capabilities, microservices architecture, and .NET modernization. The company completed a massive cloud migration in 2018-2020, moving thousands of servers and hundreds of revenue-generating applications to AWS. As of 2025, TR has achieved significant modernization milestones including 1.5M lines of code modernized monthly and 70% reduction in technical debt.

**Key Technology Pillars:**
- **Cloud Platform:** AWS (primary), with some Oracle Cloud (OCI) and Google Cloud
- **AI/ML:** Amazon SageMaker, Amazon Bedrock, custom MLOps platform (MLTools)
- **Languages:** Python, Java, .NET (C#), TypeScript, Node.js, SQL
- **Frontend:** React, Next.js, TypeScript, Tailwind CSS
- **Backend:** Microservices, serverless (AWS Lambda), containers (ECS/Fargate)
- **Data:** Amazon S3, DynamoDB, Redshift, BigQuery, Oracle Autonomous Database

---

## Table of Contents

1. [Cloud Infrastructure](#cloud-infrastructure)
2. [AI/ML Platform](#aiml-platform)
3. [Programming Languages & Frameworks](#programming-languages--frameworks)
4. [Data & Storage](#data--storage)
5. [DevOps & CI/CD](#devops--cicd)
6. [Monitoring & Observability](#monitoring--observability)
7. [Security & Compliance](#security--compliance)
8. [Application Architecture](#application-architecture)
9. [Migration & Modernization](#migration--modernization)
10. [Interview Relevance](#interview-relevance)

---

## Cloud Infrastructure

### Primary Cloud: Amazon Web Services (AWS)

**Migration Timeline:**
- **2018:** Partnered with AWS Professional Services and AWS Managed Services
- **2020:** Completed large-scale migration **5 months ahead of schedule**
- **Scale:** Thousands of servers, hundreds of revenue-generating applications migrated

**AWS Services Used:**

#### Compute & Serverless
```
- Amazon EC2 (virtual servers)
  └─ EC2 Spot Instances (ML inference cost reduction)
- AWS Lambda (serverless functions)
  └─ Event-driven processing
  └─ Microservices orchestration
- Amazon ECS (Elastic Container Service)
  └─ Container orchestration
- AWS Fargate (serverless containers)
  └─ No server management
```

#### Storage & Databases
```
- Amazon S3 (object storage)
  └─ Data lakes
  └─ ML training data
  └─ Document storage
- Amazon DynamoDB (NoSQL database)
  └─ Scalable, low-latency
  └─ Document metadata
- Amazon RDS (relational databases)
- Amazon Redshift (data warehouse)
  └─ Analytics and BI
```

#### AI & Machine Learning
```
- Amazon SageMaker (end-to-end ML platform)
  └─ SageMaker Studio (experimentation)
  └─ SageMaker Training (distributed training)
  └─ SageMaker Model Registry
  └─ SageMaker Pipelines (MLOps)
  └─ SageMaker Hosting (model deployment)
  └─ SageMaker Model Monitor (drift detection)
  └─ SageMaker Clarify (bias detection, explainability)
  └─ SageMaker Experiments (tracking)

- Amazon Bedrock (managed LLM platform)
  └─ Claude (Anthropic) integration
  └─ Multiple foundation models
  └─ Amazon Bedrock Flows (workflow automation)
  └─ Provisioned directly per user account

- Amazon OpenSearch Service
  └─ Search and analytics
  └─ Log analysis
```

#### Application Services
```
- AWS API Gateway (API management)
- AWS Lambda Step Functions (workflow orchestration)
- Amazon Route 53 (DNS service)
- Amazon SES (email service)
```

#### Data & Analytics
```
- AWS Data Lab (data architecture consulting)
- Amazon Managed Streaming for Apache Kafka (MSK)
  └─ Real-time data streaming
  └─ Analytics data capture
- Amazon EMR (big data processing)
```

#### DevOps & Developer Tools
```
- AWS CloudFormation (infrastructure as code)
- AWS Cloud Development Kit (CDK)
  └─ Custom extensions for compliance
  └─ Policy enforcement
  └─ Standardization automation
- AWS CodeCommit (source control)
- AWS CodeBuild (CI/CD builds)
- AWS CodePipeline (CI/CD orchestration)
- AWS Systems Manager
  └─ Parameter Store (secrets management)
```

#### Security & Governance
```
- AWS IAM (identity and access management)
  └─ Roles and policies (least privilege)
- AWS Config (configuration tracking)
- AWS CloudTrail (audit logging)
- AWS ParameterStore (secrets management)
- AWS Secrets Manager
```

#### Monitoring & Operations
```
- AWS CloudWatch (monitoring and logging)
  └─ Metrics, logs, alarms
  └─ Application tracing
```

### Secondary Cloud Platforms

**Oracle Cloud Infrastructure (OCI):**
- **Oracle Autonomous Database**
  - Used for ONESOURCE tax application
  - Better stability, price-performance, security
  - Zero downtime requirement
  - Increased availability and scalability

**Google Cloud Platform (GCP):**
- **BigQuery** (data analytics)
- **Additional analytics services**
- Multi-cloud strategy for specific workloads

**IBM Cloud:**
- Historical relationships
- Specific workloads (not primary platform)

---

## AI/ML Platform

### Thomson Reuters Labs ML Infrastructure

**Team Size:** ~170 applied scientists and research engineers

### MLTools - Custom MLOps Framework

**Overview:**
- **TR MLTools:** Unified MLOps platform joining multiple libraries
- **CLI tool:** Command-line interface for standardized workflows
- **Boilerplate code:** Abstracts infrastructure deployment
- **Standard project structure:** Consistent across all ML projects

**Benefits Achieved:**
- Reduction of bugs
- Faster model development times
- Faster troubleshooting
- Faster reaction to model performance drift
- Cost savings through efficient ML processes

### Core MLOps Architecture

```
ML Development Workflow:
├─ Experimentation (SageMaker Studio)
│  └─ Jupyter notebooks
│  └─ Interactive development
│
├─ Training (SageMaker Training)
│  └─ Distributed training
│  └─ GPU instance management (auto-shutdown)
│  └─ Hyperparameter tuning
│
├─ Model Registry (SageMaker Model Registry)
│  └─ Version control
│  └─ Model lineage
│  └─ Approval workflows
│
├─ CI/CD Pipeline (SageMaker Pipelines + AWS DevOps)
│  └─ Automated testing
│  └─ Model validation
│  └─ Deployment automation
│
├─ Hosting (SageMaker Hosting Services)
│  └─ Real-time endpoints
│  └─ Batch transform
│  └─ Multi-model endpoints
│
└─ Monitoring (SageMaker Model Monitor + Clarify)
   └─ Data drift detection
   └─ Model drift detection
   └─ Bias monitoring
   └─ Explainability
   └─ Custom metrics
```

### Amazon Bedrock Integration

**Open Arena Platform:**
- **Self-service AI/ML platform** for employees
- **No-code AI access** for non-technical professionals
- **Enterprise-grade** security and governance

**Adoption Metrics:**
- **19,000 monthly active users**
- **70% employee adoption rate**

**Technical Architecture:**
```
User Request
    ↓
[Orchestration Layer]
    - Centrally hosted in Enterprise AI Platform AWS account
    - Manages AI workflow activities
    ↓
[Automated Provisioning]
    - Amazon Bedrock Flows
    - Provisioned directly in user's AWS account
    ↓
[Foundation Models]
    - Claude (Anthropic) - primary for legal/tax
    - OpenAI GPT-4 - via API (not Bedrock)
    - Multiple models available
    ↓
[Supporting Services]
    - AWS Lambda (serverless compute)
    - Amazon DynamoDB (low-latency storage)
    - Amazon OpenSearch Service (search)
    - Amazon S3 (document storage)
    - Dynamic resource allocation
```

**Deployment Speed:**
- **Reduced from days to hours** for AI model deployment
- Developed in **under 6 weeks** (initial platform)

### AI Model Strategy

**Multi-Model Approach:**
| Model Provider | Models | Use Cases | Integration |
|----------------|--------|-----------|-------------|
| **OpenAI** | GPT-4, o1-mini (testing) | CoCounsel core functionality | Direct API |
| **Anthropic** | Claude 3 Haiku, Claude 3.5 Sonnet | Tax/compliance, deep analysis | Amazon Bedrock |
| **Google** | Gemini | Specific workflows | Direct API |
| **Custom** | Fine-tuned models | Domain-specific tasks | SageMaker |

### RAG (Retrieval-Augmented Generation) Infrastructure

**Components:**
```
Content Repository (150+ years of legal data)
    ↓
[Embedding Generation]
    - Sentence transformers / OpenAI embeddings
    - Document chunking strategies
    ↓
[Vector Database]
    - Likely: Pinecone, Weaviate, or Amazon OpenSearch
    - Semantic search capabilities
    ↓
[Retrieval Layer]
    - Dense retrieval (embeddings)
    - Sparse retrieval (keyword/BM25)
    - Hybrid search with reranking
    ↓
[Context Assembly]
    - Token budget management
    - Relevance scoring
    - Citation extraction
    ↓
[LLM Generation]
    - Model selection based on task
    - Prompt construction with context
    ↓
Response with Citations
```

---

## Programming Languages & Frameworks

### Primary Languages

**Python** (Primary for AI/ML and data engineering)
- ML/AI development (SageMaker, TensorFlow, PyTorch)
- Data engineering (pandas, numpy)
- Backend services
- Automation and scripting
- MLOps tooling

**.NET / C#** (Legacy modernization, enterprise applications)
- Legacy applications (migrating .NET Framework → .NET)
- Windows → Linux containerization
- Significant codebase: **1.5M lines modernized monthly**
- Enterprise services
- Desktop applications (for professional tools)

**Java** (Backend services, enterprise applications)
- Microservices
- Enterprise integration
- Backend APIs
- Distributed systems

**TypeScript** (Frontend development)
- Primary frontend language
- Type-safe React development
- Node.js backend services

**Node.js / JavaScript** (Full-stack, backend services)
- RESTful APIs
- Microservices
- Real-time services
- Frontend build tools

**SQL** (Data analysis, database queries)
- Data engineering
- Analytics
- Reporting
- Database management

### Frontend Stack

**Primary Framework: React Ecosystem**
```
React (Primary UI library)
    ↓
Next.js (React framework)
    - Server-side rendering
    - Static site generation
    - API routes
    ↓
TypeScript (Type safety)
    - Static typing
    - Better IDE support
    ↓
Tailwind CSS (Styling)
    - Utility-first CSS
    - Responsive design
    - Performance optimization
```

**Notable Absences:**
- **Angular:** Not used (despite being enterprise-focused)
- **Vue:** Not used

**Why React?**
- Component reusability
- Strong ecosystem
- AI integration capabilities (important for CoCounsel)
- Performance with large datasets (legal research results)
- Server-side rendering (Next.js) for SEO

### Backend Stack

**Microservices Architecture:**
- RESTful APIs
- Event-driven services
- Serverless functions (AWS Lambda)
- Containerized services (ECS/Fargate)

**Data Processing:**
- **Apache Hadoop** (distributed computing)
- **Apache Spark** (big data processing)
- **Apache Kafka** (distributed streaming)
- **Apache Airflow** (workflow orchestration)

---

## Data & Storage

### Databases

**Relational Databases:**
```
Oracle Autonomous Database (OCI)
├─ ONESOURCE tax application
├─ Mission-critical data
└─ Zero downtime requirement

Amazon RDS
├─ PostgreSQL (likely for operational data)
├─ MySQL (legacy applications)
└─ Managed database service

Amazon Redshift
├─ Data warehousing
├─ Analytics workloads
└─ BI reporting
```

**NoSQL Databases:**
```
Amazon DynamoDB
├─ Low-latency requirements
├─ Document metadata
├─ User sessions
└─ Real-time applications
```

**Data Warehousing & Analytics:**
```
Amazon Redshift
├─ Structured data analytics
└─ SQL-based queries

Google BigQuery
├─ Large-scale analytics
└─ Multi-cloud strategy
```

**Search & Analytics:**
```
Amazon OpenSearch Service
├─ Full-text search
├─ Log analytics
├─ RAG retrieval layer
└─ Real-time search
```

**Caching:**
```
In-Memory Caching (likely Redis or ElastiCache)
├─ Prompt caching (LLM optimization)
├─ Session management
├─ API response caching
└─ Performance optimization
```

### Object Storage

**Amazon S3:**
- ML training datasets
- Legal document repositories (40,000+ databases)
- Data lakes
- Backup and archival
- Static asset hosting
- Application data

**Storage Patterns:**
- Tiered storage (Intelligent-Tiering)
- Lifecycle policies
- Cross-region replication
- Encryption at rest

### Data Streaming

**Amazon Managed Streaming for Apache Kafka (MSK):**
- Real-time data capture
- Analytics data streaming
- Event-driven architectures
- User activity tracking
- Log aggregation

**Use Cases:**
- Capturing analytics data for product teams
- Real-time user experience monitoring
- Data pipeline integration
- Microservices communication

---

## DevOps & CI/CD

### Infrastructure as Code (IaC)

**AWS Cloud Development Kit (CDK):**
- Custom TR extension for compliance
- Automated standardization
- Policy enforcement
- Faster infrastructure deployment

**AWS CloudFormation:**
- Infrastructure templates
- Stack management
- Change sets and rollback

**Benefits:**
- Consistent environments
- Version-controlled infrastructure
- Automated compliance checks
- Faster provisioning

### CI/CD Pipeline

**AWS Native Tools:**
```
Source Control
├─ AWS CodeCommit
└─ Git repositories

Build
├─ AWS CodeBuild
├─ Containerization
└─ Automated testing

Deployment
├─ AWS CodePipeline
├─ Multi-stage deployments
├─ Blue-green deployments
└─ Canary releases

Orchestration
└─ Lambda Step Functions (workflow automation)
```

**Likely Additional Tools:**
- GitHub/GitLab (for open-source integration)
- Jenkins (legacy systems)
- Container registries (ECR, Docker Hub)

### Containerization

**Amazon ECS (Elastic Container Service):**
- Container orchestration
- Microservices deployment
- Service discovery
- Load balancing

**AWS Fargate:**
- Serverless containers
- No server management
- Auto-scaling
- Cost optimization

**Container Strategy:**
```
Legacy .NET Applications
    ↓
[Modernization with AWS Transform]
    ↓
Containerized .NET Applications
    ↓
Deploy to ECS/Fargate
    ↓
Linux containers (30% cost savings)
```

### Deployment Patterns

**Blue-Green Deployments:**
- Zero downtime deployments
- Easy rollback
- Production traffic switching

**Canary Releases:**
- Gradual rollout
- Risk mitigation
- Performance monitoring

**Serverless Deployments:**
- AWS Lambda functions
- Event-driven architecture
- Auto-scaling

---

## Monitoring & Observability

### Monitoring Stack

**AWS CloudWatch:**
- Application metrics
- Log aggregation
- Alarms and notifications
- Dashboards
- Distributed tracing

**DataDog:**
- Application performance monitoring (APM)
- Infrastructure monitoring
- Log management
- Unified observability
- **Confirmed usage:** "Improved audit and traceability using AWS CloudWatch, DataDog and SumoLogic"

**SumoLogic:**
- Log analytics
- Security monitoring
- Notification flow tracking (producer to consumer visibility)
- Cloud-native log management

### SageMaker Model Monitoring

**SageMaker Model Monitor:**
- Data drift detection
- Model performance degradation
- Feature drift tracking
- Prediction drift monitoring

**SageMaker Clarify:**
- Bias detection
- Explainability (SHAP values)
- Feature attribution
- Fairness metrics

**Custom Monitoring:**
- Business metrics
- Domain-specific KPIs
- Legal accuracy metrics
- Citation verification rates

### Observability Strategy

```
Application Layer
    ↓
[Metrics Collection]
    - CloudWatch (AWS native)
    - DataDog (unified platform)
    ↓
[Log Aggregation]
    - CloudWatch Logs
    - SumoLogic
    ↓
[Distributed Tracing]
    - AWS X-Ray (likely)
    - DataDog APM
    ↓
[Alerting & Incident Response]
    - CloudWatch Alarms
    - PagerDuty (likely)
    - Incident management
    ↓
[Dashboards & Visualization]
    - CloudWatch Dashboards
    - DataDog Dashboards
    - Custom BI tools
```

---

## Security & Compliance

### AWS Security Best Practices

**Identity & Access Management:**
```
AWS IAM
├─ Least privilege principle
├─ Role-based access control (RBAC)
├─ Multi-factor authentication (MFA)
└─ Federated access

Security Groups & Network ACLs
├─ Network segmentation
├─ Firewall rules
└─ VPC isolation
```

**Secrets Management:**
```
AWS Parameter Store
├─ Application secrets centralization
├─ Encrypted storage
└─ Version control

AWS Secrets Manager
├─ Database credentials
├─ API keys
└─ Automatic rotation
```

**Configuration & Compliance:**
```
AWS Config
├─ Configuration tracking
├─ Compliance rules
├─ Change notifications
└─ Historical configuration

AWS CloudTrail
├─ API call logging
├─ Audit trail
├─ Security analysis
└─ Forensics
```

### Data Security

**Encryption:**
- **At Rest:** S3, DynamoDB, RDS, Redshift
- **In Transit:** TLS/SSL for all services
- **Key Management:** AWS KMS

**Attorney-Client Privilege Protection:**
- Data isolation for legal content
- Access controls and audit logs
- No AI training on customer data
- Compliance with legal professional standards

### Compliance Requirements

**Regulatory Compliance:**
- SOC 2 Type II
- GDPR (for international operations)
- Data privacy regulations
- Professional responsibility standards

**Thomson Reuters Trust Principles:**
- Transparency
- Data integrity
- Accuracy
- Professional standards

---

## Application Architecture

### Microservices Architecture

**Pattern:**
```
API Gateway
    ↓
Load Balancer (ALB)
    ↓
┌──────────┬──────────┬──────────┬──────────┐
│ Service  │ Service  │ Service  │ Service  │
│    A     │    B     │    C     │    D     │
└──────────┴──────────┴──────────┴──────────┘
    ↓          ↓          ↓          ↓
┌─────────────────────────────────────────┐
│       Message Queue (Kafka, SQS)        │
└─────────────────────────────────────────┘
    ↓
Data Layer (DynamoDB, RDS, S3)
```

**Benefits:**
- Independent scaling
- Technology flexibility
- Fault isolation
- Faster deployments
- Team autonomy

### Serverless Architecture

**AWS Lambda Functions:**
- Event-driven processing
- Auto-scaling
- Pay-per-use pricing
- No server management

**Use Cases:**
```
API Endpoints
├─ RESTful APIs via API Gateway
└─ GraphQL endpoints

Data Processing
├─ S3 event triggers (document upload)
├─ DynamoDB streams (data changes)
└─ EventBridge rules (scheduled tasks)

AI/ML Integration
├─ Model inference
├─ Preprocessing
└─ Postprocessing

Workflow Orchestration
├─ Step Functions (multi-step workflows)
└─ Agentic AI coordination
```

### CoCounsel AI Architecture

**High-Level Architecture:**
```
User Interface (React/Next.js)
    ↓
API Gateway
    ↓
┌─────────────────────────────────────────┐
│    CoCounsel Application Services       │
│    (Microservices, Serverless)          │
└─────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────┐
│        AI Orchestration Layer           │
│  - Model selection                      │
│  - Prompt engineering                   │
│  - RAG retrieval                        │
└─────────────────────────────────────────┘
    ↓                    ↓                 ↓
┌──────────┐    ┌──────────────┐    ┌──────────┐
│  OpenAI  │    │    Amazon    │    │ Content  │
│  API     │    │   Bedrock    │    │  Layer   │
│ (GPT-4)  │    │   (Claude)   │    │(Westlaw) │
└──────────┘    └──────────────┘    └──────────┘
```

### Westlaw Platform Architecture

**Likely Architecture:**
```
Search Interface (React)
    ↓
API Layer
    ↓
┌─────────────────────────────────────────┐
│         Search & Ranking Service         │
│  - Natural language processing          │
│  - Relevance ranking (ML models)        │
│  - Key Number classification            │
└─────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────┐
│       Content & Citation Layer          │
│  - 40,000+ databases                    │
│  - Citation graph (KeyCite)             │
│  - Document store                       │
└─────────────────────────────────────────┘
    ↓
Data Storage (S3, OpenSearch, Redshift)
```

---

## Migration & Modernization

### .NET Modernization Journey

**Timeline & Scale:**
- **Modernization Rate:** 1.5 million lines of code per month
- **Speed Increase:** 4x faster transformation
- **Technical Debt Reduction:** 70% reduction
- **Timeline:** Months → 2 weeks per application

### AWS Transform for .NET

**Tool:** Agentic AI for .NET modernization

**Capabilities:**
```
AI-Powered Agents:
├─ Asset discovery
├─ Codebase analysis
├─ Automated planning
├─ Code refactoring
├─ Security vulnerability detection
└─ Real-time adaptive optimization
```

**Migration Patterns:**
```
.NET Framework (Windows)
    ↓
[AWS Transform AI Refactoring]
    ↓
.NET (Cross-platform)
    ↓
[Containerization]
    ↓
Linux Containers (ECS/Fargate)
    ↓
30% cost reduction
```

**Benefits Achieved:**
- **30% cost reduction** (Windows → Linux containers)
- **4x speed improvement** in transformation
- **70% reduction in technical debt**
- **Security vulnerability detection** in unsupported versions
- **Parallel modernization** of hundreds of applications

**Quote from Matt Dimich, VP of Platform Engineering:**
> "AWS Transform felt like an extension of our team — constantly learning, optimizing, and helping us move faster."

### Cloud Migration Success

**Timeline:**
- **2018:** Started migration
- **2020:** Completed **5 months ahead of schedule**

**Scale:**
- Thousands of servers
- Hundreds of revenue-generating applications
- Mission-critical workloads

**Business Impact:**
- Increased business agility
- Faster innovation pace
- Enhanced data analytics capabilities
- Improved scalability
- Better disaster recovery

---

## Interview Relevance

### Why This Matters for Principal AI Engineer Role

**1. Cloud-Native Mindset**
- TR is **all-in on AWS**
- Deep AWS service integration
- You'll need AWS expertise (SageMaker, Bedrock, Lambda, etc.)
- Multi-cloud awareness (Oracle, GCP for specific use cases)

**2. AI/ML Infrastructure Experience**
- TR has **mature MLOps platform** (MLTools)
- SageMaker expertise highly valued
- Understanding of model lifecycle management
- Experience with Bedrock/LLMs expected

**3. Modernization Experience**
- TR is actively modernizing **.NET applications**
- Container expertise (ECS, Fargate)
- Understanding of legacy system constraints
- Migration experience valuable

**4. Scale & Reliability**
- **20,000+ organizations** rely on TR systems
- Zero downtime requirements
- Professional-grade accuracy standards
- High-stakes domain (legal, financial)

**5. Multi-Model AI Strategy**
- Not locked into single vendor
- OpenAI, Anthropic, Google integrations
- Model selection based on use case
- Cost optimization across providers

### Technical Skills to Highlight

**Must-Have:**
- ✅ **AWS expertise** (SageMaker, Bedrock, Lambda, ECS)
- ✅ **Python** for ML/AI development
- ✅ **MLOps experience** (CI/CD for ML, monitoring, drift detection)
- ✅ **LLM/RAG architecture** understanding
- ✅ **Microservices** and containerization

**Strong Plus:**
- ✅ **.NET experience** (modernization context)
- ✅ **React/TypeScript** (frontend integration with AI)
- ✅ **SageMaker** specific experience
- ✅ **Bedrock** and multi-model orchestration
- ✅ **Real-time streaming** (Kafka, MSK)

**Good to Have:**
- ✅ **Infrastructure as Code** (CDK, CloudFormation)
- ✅ **Monitoring tools** (CloudWatch, DataDog)
- ✅ **Data engineering** (Spark, Airflow)
- ✅ **Oracle** database experience

### Discussion Topics for Interview

**Architecture Questions:**
- "How would you design a multi-tenant RAG system on AWS?"
- "How would you optimize LLM inference costs while maintaining low latency?"
- "How would you implement blue-green deployments for ML models?"

**MLOps Questions:**
- "How would you detect and handle model drift in production?"
- "What's your approach to A/B testing ML models?"
- "How would you implement CI/CD for machine learning?"

**Modernization Questions:**
- "How would you approach modernizing a legacy .NET application?"
- "What's your strategy for containerizing applications?"
- "How do you balance technical debt vs. feature development?"

**Multi-Model Strategy Questions:**
- "How would you choose between different LLM providers?"
- "How would you implement fallback strategies for LLM failures?"
- "What metrics would you track for LLM performance?"

### Technology Alignments

**Your Experience → TR Tech Stack:**

| Your Experience | TR Equivalent | Relevance |
|----------------|---------------|-----------|
| AWS | Primary cloud | Direct match |
| SageMaker | Core ML platform | Critical |
| LLM/RAG | CoCounsel architecture | Essential |
| Python | Primary AI language | Required |
| Microservices | Application architecture | Important |
| Docker/K8s | ECS/Fargate (similar) | Transferable |
| MLOps | MLTools framework | Highly valued |

### Red Flags to Avoid

**❌ Don't Say:**
- "I prefer GCP/Azure over AWS" (they're AWS-committed)
- "Microservices are overrated" (their core architecture)
- "Legacy systems should be rewritten" (they're modernizing, not replacing)
- "Single model is sufficient" (they value multi-model strategy)

**✅ Do Say:**
- "I have experience with AWS and SageMaker..."
- "I understand the value of multi-model AI strategies..."
- "I've worked on MLOps and model lifecycle management..."
- "I appreciate the balance between modernization and reliability..."

---

## Key Technologies Summary

### By Category

**Cloud & Infrastructure:**
- AWS (primary), Oracle Cloud, Google Cloud
- EC2, Lambda, ECS, Fargate, S3, CloudFormation, CDK

**AI & Machine Learning:**
- Amazon SageMaker (full suite)
- Amazon Bedrock (Claude, multi-model)
- OpenAI API (GPT-4)
- Custom MLOps (MLTools)

**Languages:**
- Python (primary for AI/ML)
- .NET/C# (enterprise, modernizing)
- Java (backend services)
- TypeScript/Node.js (full-stack)

**Frontend:**
- React, Next.js, TypeScript, Tailwind CSS

**Data:**
- Oracle Autonomous Database
- Amazon DynamoDB, RDS, Redshift
- Amazon S3, OpenSearch
- Google BigQuery

**Streaming & Processing:**
- Apache Kafka (MSK)
- Apache Spark, Hadoop, Airflow

**DevOps:**
- AWS CodePipeline, CodeBuild, CodeCommit
- Docker, ECS, Fargate
- CloudFormation, CDK

**Monitoring:**
- AWS CloudWatch
- DataDog
- SumoLogic

**Security:**
- AWS IAM, Config, CloudTrail
- AWS Parameter Store, Secrets Manager

---

## Notable Technology Choices

### What Thomson Reuters Uses

✅ **React** (not Angular or Vue)
✅ **AWS** (heavily committed, not multi-cloud balanced)
✅ **SageMaker** (not Databricks or custom Kubernetes)
✅ **Bedrock** (managed LLMs, not self-hosted)
✅ **ECS/Fargate** (not Kubernetes/EKS for containers)
✅ **.NET** (significant legacy, actively modernizing)
✅ **Oracle** (for tax platform, despite AWS commitment)
✅ **Kafka/MSK** (for streaming, not Kinesis)

### Why These Choices Matter

**React Ecosystem:**
- AI integration capabilities important for CoCounsel
- Strong performance for data-heavy applications (legal research)
- Server-side rendering (Next.js) for SEO

**AWS Commitment:**
- Deep integration across services
- Custom CDK extensions
- Long-term partnership (since 2018)
- Not exploring multi-cloud significantly

**SageMaker over Alternatives:**
- Managed service reduces operational overhead
- Full lifecycle management
- Integrated with other AWS services
- Cost optimization (auto-shutdown, Spot instances)

**Bedrock for LLMs:**
- Security and compliance critical (legal industry)
- Multiple model access
- Amazon partnership (not just OpenAI)
- Enterprise-grade reliability

---

## Sources & References

### Primary Sources
- AWS Case Studies (Thomson Reuters)
- AWS Blog Posts (ML/AI infrastructure)
- Thomson Reuters Labs Medium Blog
- StackShare technology profile

### AWS Blog Posts Referenced
1. "How Thomson Reuters Labs achieved AI/ML innovation at pace with AWS MLOps services"
2. "How Thomson Reuters built an AI platform using Amazon SageMaker"
3. "Democratizing AI: Thomson Reuters Open Arena with Amazon Bedrock"
4. "Infrastructure as Code at Thomson Reuters with AWS CDK"
5. "How Thomson Reuters Turbocharged .NET Modernization with AWS Transform"

### Additional Sources
- Anthropic case study (Thomson Reuters + Claude)
- Computer Weekly (cloud migration coverage)
- InterviewQuery (interview guides)
- Job postings (technology requirements)

---

## Update History

**November 21, 2025:**
- Initial comprehensive research
- AWS infrastructure deep dive
- ML/AI platform architecture
- .NET modernization details
- Frontend/backend stack analysis
- DevOps and monitoring coverage

**For Future Updates:**
- Track AWS Transform expansion
- Monitor Bedrock adoption growth
- Update as new TR Labs blog posts publish
- Refresh with new case studies

---

*Document created for Thomson Reuters Principal AI Engineer interview preparation*
*Research Date: November 21, 2025*
