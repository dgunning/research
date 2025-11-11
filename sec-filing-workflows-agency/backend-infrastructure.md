# SecFlow Design Agency - Backend Infrastructure Guide

## Overview

This guide outlines the backend infrastructure architecture for deploying and running SEC filing workflows at scale. The infrastructure design balances cost-effectiveness (critical for bootstrapped agency and clients) with production-readiness, security, and scalability.

### Infrastructure Philosophy

1. **Start Simple, Scale Smart** - Begin with managed services, scale only when needed
2. **Open Source First** - Prefer open-source tools to reduce costs and vendor lock-in
3. **Cloud Native** - Leverage cloud provider capabilities without tight coupling
4. **Security & Compliance** - Built-in from day one (financial services requirements)
5. **Observable & Debuggable** - Comprehensive monitoring and logging
6. **Cost Conscious** - Optimize for value, not just performance

### Target Workloads

The infrastructure must support multiple workflow patterns:
- **Classic ETL** - Scheduled batch processing (daily/weekly)
- **Real-Time Alerts** - Event-driven, low-latency triggers
- **AI-Augmented Analysis** - LLM API calls, caching, rate limiting
- **Multi-Agent Orchestration** - Complex state machines, long-running processes
- **Batch Processing** - High-volume parallel processing (hundreds/thousands of filings)

---

## Architecture Overview

### Reference Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                         Client Applications                          │
│              (Web Dashboard, API Clients, Email Alerts)              │
└────────────────────────────────┬────────────────────────────────────┘
                                 │
                    ┌────────────┴────────────┐
                    │     API Gateway         │
                    │  (Authentication, Rate  │
                    │   Limiting, Routing)    │
                    └────────┬────────┬───────┘
                             │        │
              ┌──────────────┘        └──────────────┐
              │                                       │
    ┌─────────▼─────────┐                  ┌────────▼────────┐
    │   Web API Layer   │                  │  Workflow Engine │
    │   (FastAPI/Flask) │                  │  (Airflow/Prefect)│
    └─────────┬─────────┘                  └────────┬────────┘
              │                                      │
    ┌─────────┴──────────┬──────────────────────────┴──────┐
    │                    │                                  │
┌───▼───────┐    ┌──────▼──────┐              ┌──────────▼─────────┐
│  Auth &   │    │   Database   │              │  Compute Workers   │
│   Users   │    │ (PostgreSQL) │              │  (Lambda/ECS/EC2)  │
│(Auth0/    │    │   (RDS)      │              └──────────┬─────────┘
│Supabase)  │    └──────┬───────┘                         │
└───────────┘           │                      ┌──────────▼─────────┐
                        │                      │   edgartools Core  │
                        │                      │  (SEC Data Access) │
    ┌───────────────────┴──────────┐          └──────────┬─────────┘
    │                               │                     │
┌───▼────────┐          ┌──────────▼──────┐   ┌─────────▼─────────┐
│  Metadata  │          │  Time Series DB │   │   File Storage    │
│   Store    │          │  (TimescaleDB/  │   │      (S3)         │
│(Workflow   │          │   InfluxDB)     │   │ (Raw filings,     │
│definitions,│          │  (Metrics)      │   │  processed data,  │
│  run logs) │          └─────────────────┘   │   artifacts)      │
└────────────┘                                 └───────────────────┘
                                                         │
                                              ┌──────────▼─────────┐
                                              │   Cache Layer      │
                                              │     (Redis)        │
                                              │ (Rate limiting,    │
                                              │  task queues,      │
                                              │  session data)     │
                                              └────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│                     External Services                                │
│                                                                       │
│  SEC EDGAR API  │  AI APIs (Claude, OpenAI)  │  Email (SendGrid)   │
│  News APIs      │  Cloud Storage (S3/GCS)    │  Monitoring         │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│                   Observability Stack                                │
│                                                                       │
│  Logs (CloudWatch/Loki)  │  Metrics (Prometheus/DataDog)           │
│  Traces (Jaeger/Tempo)   │  Alerts (PagerDuty/Opsgenie)            │
└─────────────────────────────────────────────────────────────────────┘
```

### Architecture Layers

1. **Client Layer** - Web dashboards, API consumers, notification channels
2. **API Gateway** - Authentication, rate limiting, routing, versioning
3. **Application Layer** - Web APIs, workflow orchestration, business logic
4. **Compute Layer** - Scalable workers executing workflow tasks
5. **Data Layer** - Databases, file storage, caching
6. **External Services** - SEC EDGAR, AI APIs, notifications
7. **Observability Layer** - Logging, metrics, tracing, alerting

---

## Cloud Provider Selection

### Recommended: Multi-Cloud Strategy (with AWS Primary)

**Primary: AWS (Amazon Web Services)**

**Why AWS:**
- Most comprehensive service catalog
- Strong in data/analytics (critical for SEC data)
- Mature ML/AI services (SageMaker, Bedrock)
- Excellent free tier (12 months)
- Large marketplace of customers
- Best documentation and community

**Secondary: GCP (Google Cloud Platform)**

**Why GCP:**
- Excellent for AI/ML workloads
- Competitive pricing
- Strong Kubernetes support
- Good for specific use cases

**Tertiary: Cloudflare (Edge Services)**

**Why Cloudflare:**
- Free tier CDN and DDoS protection
- Workers for edge computing
- R2 (S3-compatible, cheaper egress)

### Cloud Services Mapping

| Service Type | AWS | GCP Alternative | Notes |
|--------------|-----|-----------------|-------|
| Compute (Functions) | Lambda | Cloud Functions | AWS has better free tier |
| Compute (Containers) | ECS/Fargate | Cloud Run | GCP Cloud Run excellent |
| Compute (VMs) | EC2 | Compute Engine | Use for long-running processes |
| Object Storage | S3 | Cloud Storage | S3 de facto standard |
| Database (SQL) | RDS (PostgreSQL) | Cloud SQL | RDS easier management |
| Database (NoSQL) | DynamoDB | Firestore | Use case dependent |
| Cache | ElastiCache (Redis) | Memorystore | Redis standard |
| Message Queue | SQS | Cloud Tasks | SQS simple, reliable |
| Orchestration | Step Functions | Workflows | Step Functions mature |
| Monitoring | CloudWatch | Cloud Monitoring | DataDog preferred for both |
| API Gateway | API Gateway | Cloud Endpoints | AWS more features |

### Cost Optimization Strategy

**Use Free Tiers Aggressively:**
- AWS Lambda: 1M requests/month free (permanent)
- AWS S3: 5GB storage free (12 months)
- AWS RDS: 750 hours/month free (12 months)
- GCP Cloud Run: 2M requests/month free (permanent)
- Cloudflare: CDN and DDoS protection free

**Optimize for Cost:**
- Use spot instances for batch jobs (70% cheaper)
- Reserved instances for baseline load (40-60% cheaper)
- S3 lifecycle policies (move old data to Glacier)
- CloudFront/Cloudflare for static assets (reduce compute)
- Compress data in transit and at rest

---

## Compute Infrastructure

### Pattern 1: Serverless Functions (AWS Lambda)

**Best For:**
- Event-driven workflows
- Real-time alerts
- API endpoints
- Scheduled tasks (< 15 minutes)

**Configuration:**
```yaml
# Lambda Function Configuration
Runtime: Python 3.11
Memory: 512MB - 2048MB (based on workload)
Timeout: 5 minutes (default), 15 minutes (max)
Concurrency: 100-1000 (reserve capacity)
Environment Variables: Encrypted with KMS

# Triggers
- EventBridge (scheduled cron)
- S3 (file uploads)
- SQS (queue messages)
- API Gateway (HTTP requests)
```

**Cost Structure:**
```
Requests: $0.20 per 1M requests
Compute: $0.0000166667 per GB-second
Free Tier: 1M requests + 400,000 GB-seconds per month

Example: 10K invocations/day, 512MB, 2s duration
Monthly: 300K invocations, 300K GB-seconds
Cost: $0 (within free tier)
```

**Best Practices:**
```python
# Lambda function template
import os
import json
from edgartools import Company, Filing

# Initialize outside handler (connection pooling)
def handler(event, context):
    """Process SEC filing trigger."""
    try:
        # Extract parameters
        ticker = event.get('ticker')
        form_type = event.get('form_type', '10-K')

        # Process with edgartools
        company = Company(ticker)
        filings = company.get_filings(form=form_type)

        # Do analysis...

        return {
            'statusCode': 200,
            'body': json.dumps({'status': 'success'})
        }

    except Exception as e:
        # Log error (CloudWatch)
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
```

### Pattern 2: Container Services (AWS ECS/Fargate)

**Best For:**
- Long-running processes (> 15 minutes)
- AI agent orchestration
- Complex dependencies
- Stateful workflows

**Configuration:**
```yaml
# ECS Task Definition
Task CPU: 0.5 vCPU - 4 vCPU
Task Memory: 1GB - 30GB
Launch Type: Fargate (serverless) or EC2 (cost optimization)

# Container Configuration
Image: python:3.11-slim
Environment: Production
Networking: VPC with NAT Gateway (outbound internet)
Scaling: Auto-scaling based on CPU/Memory or custom metrics
```

**Cost Structure:**
```
Fargate Pricing (us-east-1):
vCPU: $0.04048 per vCPU-hour
Memory: $0.004445 per GB-hour

Example: 1 vCPU, 2GB, 8 hours/day
Daily: 8 hours × ($0.04048 + 2 × $0.004445) = $0.40
Monthly: $0.40 × 30 = $12

Spot Fargate: 70% cheaper for interruptible workloads
```

**Docker Image Structure:**
```dockerfile
# Dockerfile for workflow workers
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Run application
CMD ["python", "workflow_worker.py"]
```

**Requirements.txt:**
```txt
edgartools>=4.26.0
anthropic>=0.40.0
langgraph>=0.0.20
pandas>=2.0.0
psycopg2-binary>=2.9.0
redis>=5.0.0
boto3>=1.28.0
```

### Pattern 3: Virtual Machines (AWS EC2)

**Best For:**
- Persistent workflow orchestrators (Airflow, Prefect)
- High-memory workloads
- Custom GPU requirements
- Cost optimization (reserved instances)

**Configuration:**
```yaml
# EC2 Instance Recommendation
Instance Type: t3.medium (2 vCPU, 4GB) for orchestrator
              t3.xlarge (4 vCPU, 16GB) for heavy processing

AMI: Amazon Linux 2023 or Ubuntu 22.04 LTS
Storage: 50GB gp3 SSD (general purpose)
Networking: VPC, Security Groups (SSH, HTTP/HTTPS only)
IAM Role: Grant S3, RDS, SQS access (no access keys)

# Auto Scaling Group
Min: 1 (orchestrator always on)
Max: 10 (worker pool scales with demand)
Target: CPU 70% (scale up when exceeded)
```

**Cost Structure:**
```
t3.medium On-Demand: $0.0416/hour = $30/month
t3.medium Reserved (1 year): $0.0256/hour = $18.50/month (38% savings)
t3.medium Spot: $0.0125/hour = $9/month (70% savings)

Recommendation:
- Orchestrator: Reserved instance (always on)
- Workers: Spot instances (interruptible OK)
```

### Compute Pattern Decision Matrix

| Workload | Lambda | ECS Fargate | ECS EC2 | EC2 | Recommendation |
|----------|--------|-------------|---------|-----|----------------|
| API endpoints | ✅ Excellent | ✅ Good | ❌ Overkill | ❌ Overkill | Lambda |
| Scheduled ETL (< 15 min) | ✅ Excellent | ✅ Good | ✅ Good | ❌ Overkill | Lambda |
| Scheduled ETL (> 15 min) | ❌ Limited | ✅ Excellent | ✅ Excellent | ✅ Good | ECS Fargate |
| Real-time alerts | ✅ Excellent | ✅ Good | ❌ Overkill | ❌ Overkill | Lambda |
| AI agent (< 15 min) | ✅ Good | ✅ Excellent | ✅ Good | ❌ Overkill | Lambda or Fargate |
| AI agent (> 15 min) | ❌ Limited | ✅ Excellent | ✅ Excellent | ✅ Good | ECS Fargate |
| Batch processing (1000s) | ❌ Limited | ✅ Excellent | ✅ Excellent | ✅ Good | ECS EC2 (spot) |
| Orchestrator (Airflow) | ❌ No | ❌ Possible | ✅ Good | ✅ Excellent | EC2 (reserved) |

---

## Data Storage

### Object Storage (AWS S3)

**Use Cases:**
- Raw SEC filings (XBRL, HTML, TXT)
- Processed datasets (CSV, Parquet, JSON)
- Workflow artifacts (reports, charts)
- Model outputs (AI analysis results)
- Backups and archives

**Bucket Structure:**
```
sec-filings-production/
├── raw/                    # Raw SEC filings
│   ├── 10-K/
│   │   ├── 2024/
│   │   │   ├── AAPL/
│   │   │   │   └── 0000320193-24-000123.txt
│   │   │   └── MSFT/
│   │   └── 2023/
│   ├── 10-Q/
│   └── 8-K/
├── processed/              # Processed data
│   ├── financials/
│   │   ├── income_statements.parquet
│   │   └── balance_sheets.parquet
│   └── analysis/
│       └── risk_factors.json
├── artifacts/              # Workflow outputs
│   ├── reports/
│   └── charts/
└── backups/               # Database backups
    └── postgres/
```

**Storage Classes & Lifecycle:**
```yaml
# S3 Lifecycle Policy
Rules:
  - Move to Infrequent Access after 30 days
  - Move to Glacier after 90 days
  - Delete after 7 years (compliance requirement)

Storage Classes:
  - Standard: Frequent access, low latency ($0.023/GB)
  - Infrequent Access: Monthly access ($0.0125/GB + retrieval fee)
  - Glacier: Archive, rare access ($0.004/GB + retrieval fee)

Estimated Costs (100GB dataset):
  - Standard: $2.30/month
  - After 30 days: $1.25/month (IA)
  - After 90 days: $0.40/month (Glacier)
```

**S3 Configuration:**
```python
# Python SDK usage
import boto3
from datetime import datetime

s3 = boto3.client('s3')

def store_filing(ticker: str, accession: str, content: str):
    """Store SEC filing in S3."""
    bucket = 'sec-filings-production'
    year = datetime.now().year
    key = f'raw/10-K/{year}/{ticker}/{accession}.txt'

    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=content.encode('utf-8'),
        ServerSideEncryption='AES256',
        Metadata={
            'ticker': ticker,
            'accession': accession,
            'filing-date': datetime.now().isoformat()
        }
    )

    return f's3://{bucket}/{key}'
```

### Relational Database (AWS RDS PostgreSQL)

**Use Cases:**
- Workflow metadata (definitions, schedules, runs)
- User accounts and permissions
- API keys and tokens
- Structured financial data
- Audit logs and compliance records

**Configuration:**
```yaml
# RDS PostgreSQL Configuration
Engine: PostgreSQL 15.x
Instance Class: db.t3.micro (free tier) → db.t3.medium (production)
Storage: 20GB gp3 SSD (free tier) → 100GB+ (production)
Multi-AZ: No (dev) → Yes (production, high availability)
Automated Backups: 7 day retention
Encryption: At rest (KMS) and in transit (SSL)
```

**Database Schema:**
```sql
-- Workflows table
CREATE TABLE workflows (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    schedule JSONB,  -- Cron expression
    config JSONB,    -- Workflow configuration
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    created_by UUID REFERENCES users(id)
);

-- Workflow runs table
CREATE TABLE workflow_runs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    workflow_id UUID REFERENCES workflows(id),
    status VARCHAR(50), -- pending, running, success, failed
    started_at TIMESTAMP,
    completed_at TIMESTAMP,
    duration_seconds INTEGER,
    logs TEXT,
    outputs JSONB,
    error_message TEXT,
    metadata JSONB
);

-- SEC filings metadata table
CREATE TABLE sec_filings (
    accession_number VARCHAR(255) PRIMARY KEY,
    cik VARCHAR(10),
    ticker VARCHAR(10),
    company_name VARCHAR(255),
    form_type VARCHAR(10),
    filing_date DATE,
    period_end DATE,
    s3_path TEXT,
    processed BOOLEAN DEFAULT FALSE,
    processed_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Financial statements table (extracted data)
CREATE TABLE financial_statements (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    accession_number VARCHAR(255) REFERENCES sec_filings(accession_number),
    statement_type VARCHAR(50), -- income, balance, cashflow
    period_end DATE,
    data JSONB, -- Flexible schema for financial data
    created_at TIMESTAMP DEFAULT NOW()
);

-- Indexes for common queries
CREATE INDEX idx_filings_ticker_date ON sec_filings(ticker, filing_date DESC);
CREATE INDEX idx_filings_form_date ON sec_filings(form_type, filing_date DESC);
CREATE INDEX idx_workflow_runs_status ON workflow_runs(status, started_at DESC);
```

**Cost Structure:**
```
db.t3.micro (free tier):
  - vCPUs: 2
  - RAM: 1GB
  - Cost: $0 (12 months free tier)

db.t3.medium (production):
  - vCPUs: 2
  - RAM: 4GB
  - Cost: $0.068/hour = $49/month
  - Storage: 100GB gp3 = $11.50/month
  - Total: ~$60/month

Reserved Instance (1 year):
  - Cost: $0.042/hour = $30/month (40% savings)
```

### Time Series Database (TimescaleDB on RDS)

**Use Cases:**
- Workflow execution metrics
- API latency tracking
- Cost tracking over time
- Performance monitoring

**Why TimescaleDB:**
- PostgreSQL extension (easy to add)
- Excellent compression for time series
- Fast queries on time-based data
- Retention policies built-in

**Setup:**
```sql
-- Enable TimescaleDB extension
CREATE EXTENSION IF NOT EXISTS timescaledb;

-- Create hypertable for metrics
CREATE TABLE workflow_metrics (
    time TIMESTAMPTZ NOT NULL,
    workflow_id UUID,
    metric_name VARCHAR(100),
    metric_value DOUBLE PRECISION,
    labels JSONB
);

-- Convert to hypertable
SELECT create_hypertable('workflow_metrics', 'time');

-- Add retention policy (keep 90 days)
SELECT add_retention_policy('workflow_metrics', INTERVAL '90 days');

-- Add compression policy (compress data older than 7 days)
SELECT add_compression_policy('workflow_metrics', INTERVAL '7 days');
```

### Cache Layer (AWS ElastiCache Redis)

**Use Cases:**
- SEC filing caching (avoid repeated requests)
- Session management
- Rate limiting (API and SEC EDGAR)
- Task queues (Celery)
- Real-time workflow state

**Configuration:**
```yaml
# ElastiCache Redis Configuration
Node Type: cache.t3.micro (free tier eligible)
           cache.t3.medium (production)
Engine: Redis 7.x
Cluster Mode: Disabled (single node) → Enabled (production, sharding)
Encryption: In-transit and at-rest
Automatic Failover: Yes (Multi-AZ)
```

**Usage Patterns:**
```python
import redis
import hashlib
from datetime import timedelta

# Redis client
r = redis.Redis(
    host='redis-cluster.abc123.cache.amazonaws.com',
    port=6379,
    decode_responses=True,
    ssl=True
)

def cache_filing(accession: str, content: str, ttl: int = 86400):
    """Cache SEC filing with 24-hour TTL."""
    key = f'filing:{accession}'
    r.setex(key, ttl, content)

def get_cached_filing(accession: str) -> str | None:
    """Retrieve cached filing."""
    key = f'filing:{accession}'
    return r.get(key)

def rate_limit_check(api_key: str, limit: int = 100, window: int = 3600) -> bool:
    """Rate limiting using Redis."""
    key = f'ratelimit:{api_key}:{int(time.time() / window)}'
    current = r.incr(key)

    if current == 1:
        r.expire(key, window)

    return current <= limit
```

**Cost Structure:**
```
cache.t3.micro (free tier eligible):
  - Memory: 0.5GB
  - Cost: $0.017/hour = $12/month
  - Free tier: Not available for Redis

cache.t3.medium (production):
  - Memory: 3.09GB
  - Cost: $0.068/hour = $49/month

Reserved Instance (1 year):
  - Cost: $0.042/hour = $30/month (40% savings)
```

---

## Workflow Orchestration

### Option 1: Apache Airflow (Recommended for Complex Workflows)

**Why Airflow:**
- Industry standard for data pipelines
- Rich UI for monitoring and debugging
- Extensive plugin ecosystem
- Python-native (easy integration with edgartools)
- Open source (free)

**Deployment Options:**

#### Self-Hosted on EC2
```yaml
# EC2 Configuration for Airflow
Instance: t3.medium (2 vCPU, 4GB)
Storage: 50GB gp3 SSD
Cost: ~$30/month (on-demand), ~$18/month (reserved)

Components:
  - Webserver (UI)
  - Scheduler (triggers DAGs)
  - Worker (executes tasks)
  - PostgreSQL (metadata DB)
  - Redis (Celery backend)
```

**Installation:**
```bash
# Install Airflow
pip install apache-airflow[amazon,postgres,redis]==2.7.0

# Initialize database
airflow db init

# Create admin user
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@secflowdesign.com

# Start services
airflow webserver --port 8080
airflow scheduler
```

**DAG Example:**
```python
# dags/sec_filing_etl.py
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from edgartools import Company

default_args = {
    'owner': 'secflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'sec_filing_etl',
    default_args=default_args,
    description='Extract, transform, load SEC filings',
    schedule_interval='0 8 * * *',  # Daily at 8 AM
    catchup=False,
    tags=['sec', 'etl'],
)

def extract_filings(**context):
    """Extract SEC filings for watchlist companies."""
    tickers = ['AAPL', 'MSFT', 'GOOGL']
    filings = []

    for ticker in tickers:
        company = Company(ticker)
        latest = list(company.get_filings(form='10-K').head(1))
        filings.extend(latest)

    # Push to XCom for next task
    return [f.accession_number for f in filings]

def transform_filings(accessions, **context):
    """Transform filings into structured data."""
    results = []

    for accession in accessions:
        filing = Filing(accession)
        financials = filing.financials()

        # Extract key metrics
        results.append({
            'accession': accession,
            'ticker': filing.company,
            'filing_date': filing.filing_date,
            'revenue': financials.get('Revenues'),
            'net_income': financials.get('NetIncome'),
        })

    return results

def load_to_s3(data, **context):
    """Load processed data to S3."""
    s3_hook = S3Hook(aws_conn_id='aws_default')

    bucket = 'sec-filings-production'
    key = f'processed/financials/{datetime.now().date()}.json'

    s3_hook.load_string(
        string_data=json.dumps(data),
        key=key,
        bucket_name=bucket,
        replace=True
    )

# Define tasks
extract = PythonOperator(
    task_id='extract_filings',
    python_callable=extract_filings,
    dag=dag,
)

transform = PythonOperator(
    task_id='transform_filings',
    python_callable=transform_filings,
    op_kwargs={'accessions': '{{ ti.xcom_pull(task_ids="extract_filings") }}'},
    dag=dag,
)

load = PythonOperator(
    task_id='load_to_s3',
    python_callable=load_to_s3,
    op_kwargs={'data': '{{ ti.xcom_pull(task_ids="transform_filings") }}'},
    dag=dag,
)

# Set dependencies
extract >> transform >> load
```

### Option 2: Prefect (Modern Alternative)

**Why Prefect:**
- Modern UI and developer experience
- Better Python API than Airflow
- Hybrid execution (cloud + self-hosted)
- Built-in versioning and rollbacks
- Free tier available

**Deployment:**
```yaml
# Prefect Server on EC2
Instance: t3.small (2 vCPU, 2GB)
Cost: ~$15/month

# Or use Prefect Cloud (managed)
Free Tier: 20,000 task runs/month
Paid: $0.10 per 1,000 task runs
```

**Flow Example:**
```python
# flows/sec_filing_workflow.py
from prefect import flow, task
from prefect.deployments import Deployment
from prefect.server.schemas.schedules import CronSchedule
from edgartools import Company

@task(retries=3, retry_delay_seconds=300)
def extract_filings(tickers: list[str]) -> list[str]:
    """Extract SEC filings."""
    filings = []
    for ticker in tickers:
        company = Company(ticker)
        latest = list(company.get_filings(form='10-K').head(1))
        filings.extend([f.accession_number for f in latest])
    return filings

@task
def transform_filings(accessions: list[str]) -> list[dict]:
    """Transform filings into structured data."""
    results = []
    for accession in accessions:
        filing = Filing(accession)
        financials = filing.financials()
        results.append({
            'accession': accession,
            'ticker': filing.company,
            'revenue': financials.get('Revenues'),
        })
    return results

@task
def load_to_storage(data: list[dict]):
    """Load to storage."""
    # Implementation...
    pass

@flow(name="SEC Filing ETL")
def sec_filing_etl(tickers: list[str]):
    """Main ETL flow."""
    accessions = extract_filings(tickers)
    data = transform_filings(accessions)
    load_to_storage(data)

# Create deployment
deployment = Deployment.build_from_flow(
    flow=sec_filing_etl,
    name="daily-etl",
    work_queue_name="sec-workflows",
    schedule=CronSchedule(cron="0 8 * * *"),
    parameters={"tickers": ["AAPL", "MSFT", "GOOGL"]}
)

if __name__ == "__main__":
    deployment.apply()
```

### Option 3: AWS Step Functions (Serverless Orchestration)

**Why Step Functions:**
- Fully managed (no servers to maintain)
- Pay per execution ($0.025 per 1,000 state transitions)
- Visual workflow editor
- Integrates natively with Lambda, ECS, etc.
- Good for simple to moderate complexity

**State Machine Example:**
```json
{
  "Comment": "SEC Filing ETL Workflow",
  "StartAt": "ExtractFilings",
  "States": {
    "ExtractFilings": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:123456789:function:extract-filings",
      "Next": "TransformFilings",
      "Retry": [
        {
          "ErrorEquals": ["States.ALL"],
          "IntervalSeconds": 300,
          "MaxAttempts": 3,
          "BackoffRate": 2.0
        }
      ]
    },
    "TransformFilings": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:123456789:function:transform-filings",
      "Next": "LoadToS3"
    },
    "LoadToS3": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:123456789:function:load-to-s3",
      "End": true
    }
  }
}
```

**Cost Structure:**
```
Step Functions Standard:
  - $0.025 per 1,000 state transitions
  - Free tier: 4,000 state transitions/month

Example: 100 workflows/day, 3 states each
  - Monthly: 100 × 30 × 3 = 9,000 state transitions
  - Cost: (9,000 - 4,000) / 1,000 × $0.025 = $0.125

Very cost-effective for low-medium volume
```

### Orchestration Comparison

| Feature | Airflow | Prefect | Step Functions |
|---------|---------|---------|----------------|
| **Cost** | ~$18-30/month (EC2) | $0-15/month (cloud free tier) | ~$0-5/month (pay per use) |
| **Complexity** | High (learning curve) | Medium (modern API) | Low (visual editor) |
| **Flexibility** | Very High (Python) | Very High (Python) | Medium (limited logic) |
| **Managed** | No (self-hosted) | Yes (cloud option) | Yes (fully managed) |
| **Monitoring** | Excellent UI | Excellent UI | Good (CloudWatch) |
| **Community** | Large, mature | Growing | AWS ecosystem |
| **Best For** | Complex pipelines | Modern Python workflows | Simple to moderate |
| **Recommendation** | Production, complex | Development, modern | Serverless, simple |

**Overall Recommendation:**
- **Start with:** Prefect Cloud (free tier) or Step Functions
- **Scale to:** Self-hosted Airflow when complexity demands it
- **For clients:** Match to their preference and existing tools

---

## Security & Compliance

### Authentication & Authorization

**API Authentication:**
```python
# FastAPI with JWT authentication
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

app = FastAPI()
security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Verify JWT token."""
    try:
        payload = jwt.decode(
            credentials.credentials,
            os.getenv('JWT_SECRET'),
            algorithms=['HS256']
        )
        return payload
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.get("/workflows")
def list_workflows(user = Depends(verify_token)):
    """List workflows for authenticated user."""
    # Implementation...
    pass
```

**IAM Roles (AWS):**
```yaml
# Lambda Execution Role
PolicyDocument:
  Version: '2012-10-17'
  Statement:
    - Effect: Allow
      Action:
        - logs:CreateLogGroup
        - logs:CreateLogStream
        - logs:PutLogEvents
      Resource: arn:aws:logs:*:*:*

    - Effect: Allow
      Action:
        - s3:GetObject
        - s3:PutObject
      Resource: arn:aws:s3:::sec-filings-production/*

    - Effect: Allow
      Action:
        - secretsmanager:GetSecretValue
      Resource: arn:aws:secretsmanager:*:*:secret:anthropic-api-key-*
```

### Secrets Management

**AWS Secrets Manager:**
```python
import boto3
import json

def get_secret(secret_name: str) -> dict:
    """Retrieve secret from AWS Secrets Manager."""
    client = boto3.client('secretsmanager')

    response = client.get_secret_value(SecretId=secret_name)
    return json.loads(response['SecretString'])

# Usage
anthropic_key = get_secret('anthropic-api-key')['key']
```

**Environment Variables (Encrypted):**
```yaml
# Lambda environment variables (encrypted with KMS)
Environment:
  Variables:
    DATABASE_URL: !encrypted "arn:aws:kms:..."
    ANTHROPIC_API_KEY: !encrypted "arn:aws:kms:..."
    REDIS_URL: !encrypted "arn:aws:kms:..."
```

### Network Security

**VPC Configuration:**
```yaml
# VPC for secure deployment
VPC:
  CIDR: 10.0.0.0/16

  Subnets:
    Public:
      - 10.0.1.0/24  # AZ 1
      - 10.0.2.0/24  # AZ 2
    Private:
      - 10.0.11.0/24 # AZ 1
      - 10.0.12.0/24 # AZ 2

  Security Groups:
    WebAPI:
      Inbound:
        - Port 443 from 0.0.0.0/0 (HTTPS)
      Outbound:
        - All to VPC CIDR

    Database:
      Inbound:
        - Port 5432 from WebAPI SG only
      Outbound:
        - None (no outbound needed)

    Lambda:
      Inbound:
        - None (Lambda initiated)
      Outbound:
        - Port 443 to 0.0.0.0/0 (SEC EDGAR, APIs)
        - Port 5432 to Database SG
        - Port 6379 to Redis SG
```

### Data Encryption

**At Rest:**
- S3: Server-side encryption (SSE-S3 or SSE-KMS)
- RDS: Storage encryption with KMS
- Redis: Encryption at rest enabled
- EBS volumes: Encrypted

**In Transit:**
- HTTPS/TLS 1.3 for all API traffic
- SSL for database connections
- VPN for admin access

### Compliance Requirements

**Financial Services Compliance:**
- SOC 2 Type II readiness
- GDPR compliance (if EU customers)
- Data retention policies (7 years for financial data)
- Audit logging (immutable, encrypted)
- Access controls (RBAC)

**Audit Logging:**
```sql
-- Audit log table
CREATE TABLE audit_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    timestamp TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    user_id UUID REFERENCES users(id),
    action VARCHAR(100) NOT NULL,  -- CREATE, READ, UPDATE, DELETE
    resource_type VARCHAR(100),    -- workflow, filing, api_call
    resource_id VARCHAR(255),
    ip_address INET,
    user_agent TEXT,
    request_id UUID,
    details JSONB,
    CONSTRAINT audit_logs_immutable CHECK (false)  -- Prevent updates
);

-- Prevent updates/deletes
CREATE RULE audit_logs_no_update AS ON UPDATE TO audit_logs DO INSTEAD NOTHING;
CREATE RULE audit_logs_no_delete AS ON DELETE TO audit_logs DO INSTEAD NOTHING;
```

---

## Monitoring & Observability

### Logging Strategy

**Structured Logging:**
```python
import logging
import json
from pythonjsonlogger import jsonlogger

# Configure structured logging
logger = logging.getLogger()
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter(
    '%(timestamp)s %(level)s %(name)s %(message)s'
)
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

# Usage
logger.info('Workflow started', extra={
    'workflow_id': 'abc-123',
    'ticker': 'AAPL',
    'form_type': '10-K'
})
```

**Log Aggregation:**

**Option 1: CloudWatch Logs (AWS Native)**
```yaml
# CloudWatch Log Groups
/aws/lambda/extract-filings
/aws/lambda/transform-filings
/aws/ecs/workflow-workers
/airflow/scheduler
/airflow/worker

# Retention: 30 days (configurable)
# Cost: $0.50/GB ingested, $0.03/GB stored
```

**Option 2: Self-Hosted Loki (Cost-Effective)**
```yaml
# Loki on EC2 (t3.small)
Cost: ~$15/month
Storage: S3 (cheap long-term storage)
Query: Grafana (free)

# docker-compose.yml
version: '3'
services:
  loki:
    image: grafana/loki:latest
    ports:
      - "3100:3100"
    volumes:
      - ./loki-config.yaml:/etc/loki/local-config.yaml

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=secret
```

### Metrics & Monitoring

**Key Metrics to Track:**
```yaml
Application Metrics:
  - Workflow execution time
  - Workflow success/failure rate
  - API latency (p50, p95, p99)
  - API error rate
  - Queue depth
  - Cache hit rate

Business Metrics:
  - Filings processed per day
  - API calls to Claude/OpenAI
  - Cost per workflow execution
  - Active users
  - Customer workflows running

Infrastructure Metrics:
  - CPU utilization
  - Memory usage
  - Disk I/O
  - Network throughput
  - Database connections
  - Lambda cold starts
```

**Option 1: CloudWatch (AWS Native)**
```python
import boto3

cloudwatch = boto3.client('cloudwatch')

def publish_metric(namespace: str, metric_name: str, value: float, unit: str = 'None'):
    """Publish custom metric to CloudWatch."""
    cloudwatch.put_metric_data(
        Namespace=namespace,
        MetricData=[
            {
                'MetricName': metric_name,
                'Value': value,
                'Unit': unit,
                'Timestamp': datetime.utcnow()
            }
        ]
    )

# Usage
publish_metric('SecFlow/Workflows', 'ExecutionTime', 45.2, 'Seconds')
```

**Option 2: Prometheus + Grafana (Self-Hosted)**
```python
# prometheus_client for Python
from prometheus_client import Counter, Histogram, Gauge, start_http_server

# Define metrics
workflow_counter = Counter('workflows_total', 'Total workflows executed', ['status'])
workflow_duration = Histogram('workflow_duration_seconds', 'Workflow execution time')
active_workflows = Gauge('workflows_active', 'Currently active workflows')

# Instrument code
@workflow_duration.time()
def execute_workflow():
    active_workflows.inc()
    try:
        # Workflow logic...
        workflow_counter.labels(status='success').inc()
    except Exception:
        workflow_counter.labels(status='failed').inc()
    finally:
        active_workflows.dec()

# Start metrics server
start_http_server(8000)
```

**Option 3: DataDog (Commercial, Excellent UX)**
```yaml
Cost: $15/host/month
Features:
  - APM (application performance monitoring)
  - Log aggregation
  - Custom dashboards
  - Alerting
  - Integrations (AWS, Python, etc.)

# Python agent
pip install ddtrace

# Run with tracing
ddtrace-run python workflow_worker.py
```

**Recommendation:**
- **Development:** CloudWatch (free tier, simple)
- **Production (Bootstrapped):** Prometheus + Grafana (self-hosted, free)
- **Production (Scale):** DataDog (pay for ease of use)

### Alerting

**Alert Channels:**
- Email (SES, SendGrid)
- Slack (webhooks)
- PagerDuty (on-call)
- SMS (SNS)

**Alert Rules:**
```yaml
# Example alert rules
Alerts:
  - Name: High Error Rate
    Condition: error_rate > 5%
    Window: 5 minutes
    Severity: warning
    Channels: [slack, email]

  - Name: Workflow Failure
    Condition: workflow.status == 'failed'
    Severity: critical
    Channels: [slack, pagerduty, email]

  - Name: High Latency
    Condition: p95_latency > 5s
    Window: 10 minutes
    Severity: warning
    Channels: [slack]

  - Name: Database Connection Pool Exhausted
    Condition: db_connections > 90% of max
    Severity: critical
    Channels: [slack, pagerduty]

  - Name: High AI API Costs
    Condition: daily_ai_cost > $100
    Severity: warning
    Channels: [email]
```

---

## CI/CD Pipeline

### GitHub Actions Workflow

```yaml
# .github/workflows/deploy.yml
name: Deploy to Production

on:
  push:
    branches: [main]

env:
  AWS_REGION: us-east-1
  ECR_REPOSITORY: workflow-workers

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov

      - name: Run tests
        run: pytest --cov=src tests/

      - name: Upload coverage
        uses: codecov/codecov-action@v3

  build-and-push:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v2
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ env.AWS_REGION }}

      - name: Login to Amazon ECR
        id: login-ecr
        uses: aws-actions/amazon-ecr-login@v1

      - name: Build, tag, and push image
        env:
          ECR_REGISTRY: ${{ steps.login-ecr.outputs.registry }}
          IMAGE_TAG: ${{ github.sha }}
        run: |
          docker build -t $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG .
          docker push $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG
          docker tag $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG $ECR_REGISTRY/$ECR_REPOSITORY:latest
          docker push $ECR_REGISTRY/$ECR_REPOSITORY:latest

  deploy:
    needs: build-and-push
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to ECS
        run: |
          aws ecs update-service \
            --cluster production \
            --service workflow-workers \
            --force-new-deployment \
            --region ${{ env.AWS_REGION }}
```

### Infrastructure as Code (Terraform)

```hcl
# terraform/main.tf
terraform {
  required_version = ">= 1.0"

  backend "s3" {
    bucket = "secflow-terraform-state"
    key    = "production/terraform.tfstate"
    region = "us-east-1"
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# S3 bucket for SEC filings
resource "aws_s3_bucket" "sec_filings" {
  bucket = "sec-filings-production"

  tags = {
    Environment = "production"
    Project     = "secflow"
  }
}

resource "aws_s3_bucket_versioning" "sec_filings" {
  bucket = aws_s3_bucket.sec_filings.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_lifecycle_configuration" "sec_filings" {
  bucket = aws_s3_bucket.sec_filings.id

  rule {
    id     = "archive-old-filings"
    status = "Enabled"

    transition {
      days          = 30
      storage_class = "STANDARD_IA"
    }

    transition {
      days          = 90
      storage_class = "GLACIER"
    }
  }
}

# RDS PostgreSQL
resource "aws_db_instance" "main" {
  identifier = "secflow-production"

  engine         = "postgres"
  engine_version = "15.4"
  instance_class = "db.t3.medium"

  allocated_storage     = 100
  storage_type          = "gp3"
  storage_encrypted     = true

  db_name  = "secflow"
  username = var.db_username
  password = var.db_password

  multi_az               = true
  backup_retention_period = 7

  tags = {
    Environment = "production"
  }
}

# Lambda function
resource "aws_lambda_function" "extract_filings" {
  function_name = "extract-filings"
  role          = aws_iam_role.lambda_exec.arn

  package_type  = "Image"
  image_uri     = "${var.ecr_repository}:latest"

  memory_size = 512
  timeout     = 300

  environment {
    variables = {
      DATABASE_URL = "postgresql://${var.db_username}:${var.db_password}@${aws_db_instance.main.endpoint}/secflow"
      S3_BUCKET    = aws_s3_bucket.sec_filings.id
    }
  }

  tags = {
    Environment = "production"
  }
}
```

---

## Cost Optimization

### Cost Breakdown (Estimated Monthly)

**Starter Configuration (MVP):**
```
Compute:
  - Lambda (free tier): $0
  - ECS Fargate (minimal): $12

Storage:
  - S3 (100GB): $2.30
  - RDS db.t3.micro (free tier): $0

Cache:
  - ElastiCache t3.micro: $12

Networking:
  - Data transfer: $5

Monitoring:
  - CloudWatch (basic): $5

Total: ~$36/month
```

**Production Configuration:**
```
Compute:
  - Lambda (1M invocations): $5
  - ECS Fargate (3 tasks): $36
  - EC2 Airflow (t3.medium reserved): $18

Storage:
  - S3 (500GB with lifecycle): $8
  - RDS db.t3.medium (reserved): $30

Cache:
  - ElastiCache t3.medium (reserved): $30

Networking:
  - Data transfer: $20
  - NAT Gateway: $32

Monitoring:
  - DataDog (2 hosts): $30
  - CloudWatch: $15

External APIs:
  - Claude API: $100-500 (usage based)

Total: ~$324-724/month (excluding AI API costs)
```

### Cost Optimization Strategies

**1. Use Free Tiers Aggressively**
```
AWS Free Tier (12 months):
  - Lambda: 1M requests/month
  - RDS: 750 hours/month (db.t3.micro)
  - S3: 5GB storage + 20,000 GET requests
  - CloudWatch: 10 custom metrics
  - SNS: 1,000 email notifications

Permanent Free Tier:
  - Lambda: 1M requests/month
  - DynamoDB: 25GB storage + 25 WCU/RCU
  - CloudWatch Logs: 5GB ingestion
```

**2. Reserved Instances**
```
1-Year Reserved (vs On-Demand):
  - EC2: 40% savings
  - RDS: 40% savings
  - ElastiCache: 40% savings

3-Year Reserved (vs On-Demand):
  - EC2: 60% savings
  - RDS: 60% savings

Recommendation: Reserve baseline capacity after 3 months
```

**3. Spot Instances**
```
Use for:
  - Batch processing workers
  - Non-critical workloads
  - Stateless applications

Savings: 70-90% vs On-Demand
Risk: Can be terminated with 2-minute warning

Implementation:
  - ECS Fargate Spot
  - EC2 Spot Fleet
  - Graceful shutdown handlers
```

**4. Storage Lifecycle Policies**
```
S3 Lifecycle Rules:
  - Standard (0-30 days): $0.023/GB
  - Infrequent Access (30-90 days): $0.0125/GB
  - Glacier (90+ days): $0.004/GB

Savings: 80% for archived data
```

**5. Cache Aggressively**
```
Redis Caching Strategy:
  - SEC filings: 24-hour TTL
  - API responses: 1-hour TTL
  - Rate limit counters: window-based

Impact:
  - Reduce SEC requests by 80%
  - Reduce AI API calls by 50%
  - Reduce compute time by 60%
```

**6. Optimize AI API Usage**
```
Strategies:
  - Cache LLM responses (hash input → cache output)
  - Use cheaper models when possible (Haiku vs Opus)
  - Batch requests where applicable
  - Implement token limits per request
  - Monitor and alert on high usage

Cost Reduction: 40-60%
```

---

## Disaster Recovery & Backup

### Backup Strategy

**Database Backups:**
```yaml
RDS Automated Backups:
  Frequency: Daily
  Retention: 7 days
  Window: 3:00-4:00 AM UTC (low traffic)

Manual Snapshots:
  Frequency: Weekly (before major deployments)
  Retention: 30 days
  Storage: S3 (automated by RDS)
```

**Application Data Backups:**
```yaml
S3 Versioning:
  Enabled: Yes
  Lifecycle: Keep all versions for 30 days

Cross-Region Replication:
  Enabled: Yes (for critical data)
  Target: us-west-2 (different region)

S3 Backup:
  Tool: AWS Backup
  Frequency: Daily
  Retention: 90 days
```

**Configuration Backups:**
```yaml
Infrastructure as Code:
  Tool: Terraform
  Storage: Git repository
  Versioning: Git tags

Application Config:
  Storage: AWS Systems Manager Parameter Store
  Versioning: Automatic
  Backup: Included in Terraform
```

### Disaster Recovery Plan

**RTO & RPO Targets:**
```
RTO (Recovery Time Objective): 4 hours
RPO (Recovery Point Objective): 1 hour

Meaning:
  - Can recover within 4 hours of incident
  - Data loss limited to last 1 hour
```

**DR Procedures:**

**1. Database Failure**
```bash
# Restore from snapshot
aws rds restore-db-instance-from-db-snapshot \
  --db-instance-identifier secflow-production-restored \
  --db-snapshot-identifier secflow-backup-2024-01-15

# Update DNS/connection strings
# Test and verify
# Cutover traffic
```

**2. Application Failure**
```bash
# Rollback deployment
aws ecs update-service \
  --cluster production \
  --service workflow-workers \
  --task-definition workflow-workers:previous

# Or redeploy from Git tag
git checkout v1.2.3
./deploy.sh production
```

**3. Complete Region Failure**
```bash
# Activate DR region
terraform workspace select dr-us-west-2
terraform apply

# Restore database from snapshot
aws rds restore-db-instance-from-db-snapshot \
  --region us-west-2 \
  --db-snapshot-identifier <latest-snapshot>

# Update DNS to point to DR region
aws route53 change-resource-record-sets \
  --hosted-zone-id Z123456 \
  --change-batch file://dns-change.json

# Verify and monitor
```

---

## Scaling Strategy

### Phase 1: MVP (0-10 Customers)

**Infrastructure:**
```
- Lambda (free tier)
- RDS db.t3.micro (free tier)
- S3 (lifecycle policies)
- ElastiCache t3.micro
- Basic CloudWatch monitoring

Monthly Cost: ~$30-50
```

**Capacity:**
- 100 workflows/day
- 1,000 SEC filings/day
- 5,000 API calls/day

### Phase 2: Growth (10-50 Customers)

**Infrastructure:**
```
- Lambda + ECS Fargate mix
- RDS db.t3.medium (reserved)
- ElastiCache t3.medium (reserved)
- Self-hosted Airflow (EC2 t3.medium reserved)
- Prometheus + Grafana monitoring

Monthly Cost: ~$200-300
```

**Capacity:**
- 1,000 workflows/day
- 10,000 SEC filings/day
- 50,000 API calls/day

**Scaling Triggers:**
- Add Fargate tasks when queue depth > 100
- Scale up RDS when CPU > 70%
- Add Redis cache nodes when memory > 80%

### Phase 3: Scale (50+ Customers)

**Infrastructure:**
```
- ECS Fargate auto-scaling (5-20 tasks)
- RDS db.r5.xlarge (reserved, read replicas)
- ElastiCache cluster (3 nodes)
- Managed Airflow (MWAA) or large EC2
- DataDog monitoring

Monthly Cost: ~$1,000-2,000
```

**Capacity:**
- 10,000+ workflows/day
- 100,000+ SEC filings/day
- 500,000+ API calls/day

**Advanced Scaling:**
- Database read replicas (3x)
- Multi-region deployment
- CDN for API responses
- Dedicated customer instances (enterprise)

---

## Implementation Checklist

### Initial Setup (Week 1)

- [ ] Set up AWS account (or GCP)
- [ ] Configure IAM roles and policies
- [ ] Create VPC and networking
- [ ] Set up S3 buckets with lifecycle policies
- [ ] Deploy RDS PostgreSQL (free tier initially)
- [ ] Set up ElastiCache Redis
- [ ] Configure CloudWatch logging
- [ ] Set up secrets management (AWS Secrets Manager)
- [ ] Create first Lambda function (Hello World)
- [ ] Set up CI/CD pipeline (GitHub Actions)

### MVP Deployment (Week 2-3)

- [ ] Deploy workflow orchestrator (Prefect Cloud or Step Functions)
- [ ] Implement first workflow (Classic ETL)
- [ ] Set up API layer (FastAPI)
- [ ] Configure authentication (JWT)
- [ ] Deploy to production
- [ ] Set up monitoring dashboards
- [ ] Configure alerts (Slack, email)
- [ ] Document runbooks
- [ ] Load test (basic)
- [ ] Security audit (basic)

### Production Hardening (Week 4-6)

- [ ] Enable database encryption
- [ ] Implement backup strategy
- [ ] Set up disaster recovery procedures
- [ ] Configure auto-scaling
- [ ] Implement rate limiting
- [ ] Add comprehensive logging
- [ ] Set up error tracking (Sentry)
- [ ] Performance optimization
- [ ] Security hardening (WAF, etc.)
- [ ] Compliance audit preparation

### Ongoing Operations

- [ ] Monitor costs weekly
- [ ] Review security logs daily
- [ ] Update dependencies monthly
- [ ] Test disaster recovery quarterly
- [ ] Optimize performance monthly
- [ ] Review and update documentation quarterly

---

## Conclusion

This infrastructure guide provides a comprehensive, production-ready backend architecture for running SEC filing workflows at scale while maintaining cost-effectiveness critical for bootstrapped operations.

### Key Takeaways

1. **Start Simple** - Begin with serverless (Lambda) and managed services (RDS, Redis)
2. **Scale Smart** - Add complexity only when needed (Fargate → EC2)
3. **Monitor Everything** - Comprehensive observability from day one
4. **Optimize Costs** - Use free tiers, reserved instances, spot instances, caching
5. **Security First** - Encryption, secrets management, IAM roles, audit logging
6. **Automate Everything** - CI/CD, Infrastructure as Code, monitoring, alerting

### Recommended Starting Point

**For MVP (First 3 Months):**
```
- AWS Lambda (workflow tasks)
- AWS Step Functions or Prefect Cloud (orchestration)
- RDS PostgreSQL t3.micro (database)
- ElastiCache t3.micro (cache)
- S3 (storage)
- CloudWatch (monitoring)

Monthly Cost: $30-50
```

**Path to Scale:**
```
Month 1-3:   MVP configuration ($30-50/month)
Month 4-6:   Add Fargate, upgrade RDS ($100-200/month)
Month 7-12:  Add Airflow, monitoring ($200-400/month)
Year 2+:     Scale to $1,000-2,000/month as customer base grows
```

This infrastructure scales naturally with business growth, maintains security and compliance requirements for financial services, and optimizes costs throughout the journey.
