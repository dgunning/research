# AWS Interview Preparation for Thomson Reuters Principal AI Engineer

**Target Role:** Principal AI Engineer at Thomson Reuters
**Last Updated:** November 21, 2025
**Based On:** Thomson Reuters' confirmed AWS infrastructure and architecture

---

## Table of Contents

1. [Overview - TR's AWS Commitment](#overview---trs-aws-commitment)
2. [Amazon SageMaker Deep Dive](#amazon-sagemaker-deep-dive)
3. [Amazon Bedrock & LLM Infrastructure](#amazon-bedrock--llm-infrastructure)
4. [Lambda & Serverless Architecture](#lambda--serverless-architecture)
5. [Containers - ECS & Fargate](#containers---ecs--fargate)
6. [Data Services](#data-services)
7. [Networking & Security](#networking--security)
8. [MLOps on AWS](#mlops-on-aws)
9. [Cost Optimization](#cost-optimization)
10. [Interview Questions & Scenarios](#interview-questions--scenarios)

---

## Overview - TR's AWS Commitment

### Why This Matters

Thomson Reuters is **all-in on AWS**. Understanding their specific usage is critical:

**Migration Facts:**
- **2018:** Started migration with AWS Professional Services
- **2020:** Completed **5 months ahead of schedule**
- **Scale:** Thousands of servers, hundreds of revenue-generating apps
- **Partnership:** Deep, long-term commitment (not multi-cloud exploration)

**Your Interview Context:**
- They expect **deep AWS knowledge**, not just familiarity
- Multi-cloud experience is nice, but AWS expertise is essential
- You should know AWS services better than alternatives

### Core AWS Services at TR

**Compute:**
- EC2 (including Spot Instances)
- Lambda (serverless functions)
- ECS (container orchestration)
- Fargate (serverless containers)

**AI/ML:**
- **SageMaker** (end-to-end ML platform) ⭐ CRITICAL
- **Bedrock** (managed LLMs) ⭐ CRITICAL
- OpenSearch Service (vector search for RAG)

**Data:**
- S3 (object storage, data lakes)
- DynamoDB (NoSQL, low-latency)
- RDS (relational databases)
- Redshift (data warehouse)

**Developer Tools:**
- CodePipeline, CodeBuild, CodeCommit
- CloudFormation, CDK (IaC)
- Systems Manager (Parameter Store)

**Monitoring:**
- CloudWatch (metrics, logs, alarms)

---

## Amazon SageMaker Deep Dive

### Why SageMaker is Critical

**TR's Usage:**
- **Core ML platform** for ~170 researchers and engineers
- **MLTools framework** built entirely on SageMaker
- Powers AI features in CoCounsel, Westlaw, Open Arena

**You Must Know:**
- SageMaker end-to-end workflow
- Integration patterns
- Cost optimization techniques
- Production deployment patterns

### SageMaker Components

```
Development
├─ SageMaker Studio (Jupyter notebooks, experimentation)
├─ SageMaker Experiments (tracking)
└─ Feature Store (feature management)

Training
├─ Training Jobs (distributed training)
├─ Spot Instances (cost optimization)
├─ Automatic Model Tuning (hyperparameter)
└─ Auto-shutdown GPUs (TR uses this!)

Model Management
├─ Model Registry (versioning, lineage)
├─ Model Cards (documentation)
└─ Approval Workflows (governance)

Deployment
├─ Real-time Endpoints (synchronous inference)
├─ Batch Transform (large-scale processing)
├─ Async Inference (long-running)
├─ Multi-model Endpoints (cost optimization)
└─ Serverless Inference (pay-per-use)

Monitoring
├─ Model Monitor (drift detection)
├─ Clarify (bias, explainability)
└─ Data Capture (logging)

Orchestration
└─ SageMaker Pipelines (MLOps workflows)
```

### Key Interview Topics

#### 1. Distributed Training

**Question:** "How would you train a large language model on SageMaker?"

**Answer:**
```python
from sagemaker.pytorch import PyTorch

# Distributed training configuration
estimator = PyTorch(
    entry_point='train.py',
    role=role,
    instance_type='ml.p4d.24xlarge',  # GPU instance
    instance_count=8,  # 8 nodes
    framework_version='2.0',
    distribution={
        'torch_distributed': {
            'enabled': True
        },
        'smdistributed': {
            'dataparallel': {
                'enabled': True
            }
        }
    },
    use_spot_instances=True,  # Cost savings
    max_wait=7200,
    checkpoints_s3_uri='s3://bucket/checkpoints/'  # Resume on spot interruption
)
```

**Key Points:**
- Data parallelism for large datasets
- Model parallelism for models too large for single GPU
- Spot instances can save 70-90% on costs
- Checkpointing critical for spot instance recovery

#### 2. Model Deployment Patterns

**Question:** "How would you deploy 100 different legal domain models cost-effectively?"

**Answer: Multi-Model Endpoints**

```python
from sagemaker.multidatamodel import MultiDataModel

# Create multi-model endpoint
mme = MultiDataModel(
    name='legal-models-multi',
    model_data_prefix='s3://bucket/models/',
    image_uri=inference_image,
    role=role
)

predictor = mme.deploy(
    initial_instance_count=2,
    instance_type='ml.m5.2xlarge'
)

# Invoke specific model
response = predictor.predict(
    data=input_data,
    target_model='contract-classifier-v2.tar.gz'
)
```

**Why This Matters:**
- TR has many specialized models (contract analysis, deposition prep, etc.)
- Multi-model endpoints share infrastructure → huge cost savings
- Models loaded on-demand into memory
- Automatic caching of frequently used models

#### 3. MLOps Pipeline

**Question:** "Design an MLOps pipeline for legal document classification."

**Answer: SageMaker Pipelines**

```python
from sagemaker.workflow.pipeline import Pipeline
from sagemaker.workflow.steps import (
    ProcessingStep, TrainingStep,
    CreateModelStep, ConditionStep
)
from sagemaker.workflow.conditions import ConditionGreaterThanOrEqualTo

# 1. Data preprocessing
preprocessing_step = ProcessingStep(
    name='Preprocess',
    processor=sklearn_processor,
    code='preprocess.py',
    inputs=[...],
    outputs=[...]
)

# 2. Model training
training_step = TrainingStep(
    name='Train',
    estimator=estimator,
    inputs={
        'train': TrainingInput(
            s3_data=preprocessing_step.properties
                .ProcessingOutputConfig.Outputs['train'].S3Output.S3Uri
        )
    }
)

# 3. Model evaluation
evaluation_step = ProcessingStep(
    name='Evaluate',
    processor=evaluation_processor,
    code='evaluate.py',
    property_files=[evaluation_report]
)

# 4. Conditional deployment (only if accuracy >= 95%)
condition = ConditionGreaterThanOrEqualTo(
    left=JsonGet(
        step_name=evaluation_step.name,
        property_file=evaluation_report,
        json_path='metrics.accuracy'
    ),
    right=0.95  # High bar for legal applications
)

condition_step = ConditionStep(
    name='CheckAccuracy',
    conditions=[condition],
    if_steps=[register_model_step, deploy_step],
    else_steps=[notify_failure_step]
)

# Create pipeline
pipeline = Pipeline(
    name='legal-classifier-pipeline',
    steps=[preprocessing_step, training_step,
           evaluation_step, condition_step]
)
```

**Why This Matters for TR:**
- **High accuracy required:** Legal applications can't have errors
- **Audit trail:** Every model training run logged
- **Reproducibility:** Same inputs always produce same model
- **Automation:** No manual steps, reduce human error

#### 4. Cost Optimization

**Question:** "TR processes millions of documents. How do you optimize SageMaker costs?"

**Answer:**

**1. Training Optimization:**
```python
# Use spot instances (70-90% savings)
estimator = PyTorch(
    ...,
    use_spot_instances=True,
    max_wait=3600,  # Wait up to 1 hour for spot
    checkpoint_s3_uri='s3://bucket/checkpoints/'
)

# Auto-shutdown GPUs after training (TR does this!)
lifecycle_config = {
    'OnStart': [
        {
            'Content': base64.b64encode(
                b'#!/bin/bash\n'
                b'echo "Training started"\n'
            ).decode()
        }
    ],
    'OnStop': [
        {
            'Content': base64.b64encode(
                b'#!/bin/bash\n'
                b'# Shutdown GPU instances automatically\n'
                b'shutdown -h now\n'
            ).decode()
        }
    ]
}
```

**2. Inference Optimization:**
```python
# Multi-model endpoints
# Instead of: 100 models × 2 instances × $1/hour = $200/hour
# Use: 1 multi-model endpoint × 4 instances × $1/hour = $4/hour
# Savings: 98%

# Auto-scaling
client.register_scalable_target(
    ServiceNamespace='sagemaker',
    ResourceId=f'endpoint/{endpoint_name}/variant/AllTraffic',
    ScalableDimension='sagemaker:variant:DesiredInstanceCount',
    MinCapacity=2,  # Scale down to 2 at night
    MaxCapacity=20  # Scale up to 20 during peak
)
```

**3. Storage Optimization:**
```python
# S3 lifecycle policies
lifecycle_policy = {
    'Rules': [
        {
            'Id': 'ArchiveOldTrainingData',
            'Status': 'Enabled',
            'Transitions': [
                {
                    'Days': 90,
                    'StorageClass': 'GLACIER'  # Move to cheap storage
                }
            ]
        }
    ]
}
```

**TR-Specific Context:**
- Open Arena: 19,000 users → need elastic scaling
- Legal accuracy requirements → can't sacrifice quality for cost
- Strategy: Optimize infrastructure, not model performance

---

## Amazon Bedrock & LLM Infrastructure

### Why Bedrock is Critical at TR

**Thomson Reuters' Usage:**
- **CoCounsel AI:** Claude for tax/compliance workflows
- **Open Arena:** Enterprise LLM playground (19,000 users, 70% adoption)
- **Multi-model strategy:** Access to multiple foundation models
- **Security:** Enterprise-grade isolation, no training on customer data

### Bedrock vs. Self-Hosted LLMs

**Why TR Chose Bedrock:**

| Factor | Self-Hosted | Bedrock |
|--------|-------------|---------|
| **Security** | Complex setup | Enterprise-grade built-in |
| **Compliance** | You manage | AWS manages |
| **Scaling** | Manual | Automatic |
| **Model access** | One vendor | Multiple (Claude, others) |
| **Operational overhead** | High | Low (managed service) |
| **Cost** | Predictable but high | Pay-per-use |
| **Data privacy** | Full control | AWS guarantees (no training) |

**For TR's use case:**
- ✅ Attorney-client privilege protection
- ✅ No training on customer data (guaranteed by AWS)
- ✅ Quick access to new models
- ✅ Reduced operational burden (focus on products, not infrastructure)

### Bedrock Architecture Patterns

#### 1. Model Selection Strategy

**TR's Approach:**
```python
class ModelSelector:
    """
    Thomson Reuters' model selection logic
    """
    def select_model(self, task_type, urgency, cost_sensitivity):
        if task_type in ['tax_compliance', 'deep_legal_analysis']:
            # Require transparent reasoning
            return 'anthropic.claude-3-5-sonnet-20241022-v2:0'

        elif urgency == 'high' or cost_sensitivity == 'high':
            # Speed and cost matter
            return 'anthropic.claude-3-haiku-20240307-v1:0'

        else:
            # Default balanced model
            return 'anthropic.claude-3-5-sonnet-20241022-v2:0'
```

**Interview Insight:**
> "We use Claude 3 Haiku for rapid processing and Claude 3.5 Sonnet for deep analysis, selected after extensive evaluation against human expert benchmarks."

#### 2. RAG with Bedrock

**Key Pattern at TR:**

```python
import boto3
import json

bedrock = boto3.client('bedrock-runtime')
opensearch = boto3.client('opensearchservice')

def query_with_rag(user_question, max_results=5):
    """
    RAG pattern used in CoCounsel/Westlaw
    """
    # 1. Retrieve relevant legal content
    relevant_docs = search_legal_content(
        query=user_question,
        index='westlaw-cases',
        max_results=max_results
    )

    # 2. Assemble context with citations
    context = "\n\n".join([
        f"Document {i+1} ({doc['citation']}):\n{doc['text']}"
        for i, doc in enumerate(relevant_docs)
    ])

    # 3. Construct prompt with context
    prompt = f"""You are a legal research assistant. Use ONLY the provided legal documents to answer the question. Always cite your sources.

Context:
{context}

Question: {user_question}

Answer with citations:"""

    # 4. Invoke Bedrock
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 2000,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    })

    response = bedrock.invoke_model(
        modelId='anthropic.claude-3-5-sonnet-20241022-v2:0',
        body=body
    )

    response_body = json.loads(response['body'].read())
    answer = response_body['content'][0]['text']

    # 5. Verify citations (important for legal!)
    verified_answer = verify_citations(answer, relevant_docs)

    return verified_answer

def verify_citations(answer, source_docs):
    """
    Critical step: ensure AI didn't hallucinate citations
    """
    # Extract citations from answer
    # Verify each citation exists in source_docs
    # Flag any unverifiable claims
    # ... implementation ...
    return verified_answer
```

**Key Concepts:**
- **Grounding:** All responses grounded in retrieved documents
- **Citations:** Every claim must have a citation
- **Verification:** Post-processing to check citation validity
- **Hallucination mitigation:** RAG reduces but doesn't eliminate hallucinations

#### 3. Prompt Caching for Cost Optimization

**TR's Optimization:**

```python
def invoke_with_caching(system_prompt, user_query, cache_key):
    """
    Use prompt caching to reduce costs
    """
    # Large system prompts (e.g., Practical Law context) can be cached
    # Reduces tokens processed, lowers cost

    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "system": [
            {
                "type": "text",
                "text": system_prompt,
                "cache_control": {"type": "ephemeral"}  # Cache this
            }
        ],
        "messages": [
            {
                "role": "user",
                "content": user_query
            }
        ]
    })

    response = bedrock.invoke_model(
        modelId='anthropic.claude-3-5-sonnet-20241022-v2:0',
        body=body
    )

    return response
```

**Cost Savings:**
- System prompts with Practical Law context: ~10,000 tokens
- Without caching: 10,000 input tokens per request
- With caching: 10,000 tokens first time, then 10% cost for cache hits
- At 19,000 users: Massive savings

#### 4. Bedrock Flows (Workflow Automation)

**TR's Open Arena Implementation:**

```python
# Bedrock Flows for multi-step agentic workflows
flow_definition = {
    "name": "legal-research-flow",
    "nodes": [
        {
            "name": "query-understanding",
            "type": "prompt",
            "configuration": {
                "prompt": "Extract key legal concepts and jurisdiction from: {{user_query}}"
            }
        },
        {
            "name": "retrieval",
            "type": "knowledge-base",
            "configuration": {
                "knowledgeBaseId": "westlaw-kb-id"
            }
        },
        {
            "name": "synthesis",
            "type": "prompt",
            "configuration": {
                "prompt": "Synthesize answer with citations from: {{retrieval.output}}"
            }
        }
    ],
    "connections": [
        {"source": "query-understanding", "target": "retrieval"},
        {"source": "retrieval", "target": "synthesis"}
    ]
}
```

**Benefits:**
- **Automation:** Multi-step workflows without coding
- **Provisioning:** "Fully automated provisioning directly within each user's AWS account"
- **Speed:** "Deployment time reduced from days to hours"

### Interview Questions on Bedrock

**Q1: "Why did TR choose Bedrock over hosting Claude on EC2?"**

**Answer:**
1. **Security & Compliance:**
   - AWS guarantees no training on customer data
   - Enterprise-grade encryption
   - Attorney-client privilege protection
   - Easier compliance audits

2. **Operational Efficiency:**
   - No model hosting/scaling to manage
   - Automatic updates to new model versions
   - High availability built-in
   - Focus engineers on products, not infrastructure

3. **Multi-Model Access:**
   - Can switch models easily
   - Test different models for different tasks
   - Not locked into one provider

4. **Cost Model:**
   - Pay-per-use (no idle costs)
   - Scales to zero
   - Better for variable workloads (Open Arena: 19,000 users)

**Q2: "How would you implement rate limiting and cost controls for 19,000 users?"**

**Answer:**
```python
import boto3
from functools import wraps
import time

# 1. Per-user rate limiting
class UserRateLimiter:
    def __init__(self, max_requests_per_minute=10):
        self.max_requests = max_requests_per_minute
        self.user_requests = {}  # user_id -> [(timestamp, tokens_used)]

    def check_limit(self, user_id, estimated_tokens):
        now = time.time()
        minute_ago = now - 60

        # Clean old requests
        if user_id in self.user_requests:
            self.user_requests[user_id] = [
                (ts, tokens) for ts, tokens in self.user_requests[user_id]
                if ts > minute_ago
            ]

        # Check limit
        recent_requests = len(self.user_requests.get(user_id, []))
        if recent_requests >= self.max_requests:
            raise RateLimitError(f"Rate limit exceeded: {recent_requests} requests/min")

        # Record request
        if user_id not in self.user_requests:
            self.user_requests[user_id] = []
        self.user_requests[user_id].append((now, estimated_tokens))

# 2. Cost monitoring
class CostMonitor:
    def __init__(self, daily_budget_usd=10000):
        self.daily_budget = daily_budget_usd
        self.today_cost = 0

    def track_request(self, tokens_input, tokens_output, model_id):
        # Claude 3.5 Sonnet pricing (example)
        input_cost = tokens_input * 0.003 / 1000  # $3 per 1M tokens
        output_cost = tokens_output * 0.015 / 1000  # $15 per 1M tokens
        request_cost = input_cost + output_cost

        self.today_cost += request_cost

        if self.today_cost > self.daily_budget:
            raise BudgetExceededError(f"Daily budget ${self.daily_budget} exceeded")

        return request_cost

# 3. Integration
rate_limiter = UserRateLimiter(max_requests_per_minute=20)
cost_monitor = CostMonitor(daily_budget_usd=50000)  # $50k/day for 19k users

def invoke_bedrock_with_controls(user_id, prompt, model_id):
    # Estimate tokens (rough)
    estimated_tokens = len(prompt.split()) * 1.3

    # Check rate limit
    rate_limiter.check_limit(user_id, estimated_tokens)

    # Invoke model
    response = bedrock.invoke_model(...)

    # Track cost
    cost = cost_monitor.track_request(
        tokens_input=response['usage']['input_tokens'],
        tokens_output=response['usage']['output_tokens'],
        model_id=model_id
    )

    return response, cost
```

**Additional Controls:**
- **User tiers:** Free (10 req/min), Pro (50 req/min), Enterprise (unlimited)
- **Model restrictions:** Free users get Haiku only, Pro gets Sonnet
- **Alerts:** CloudWatch alarms when approaching budget
- **Graceful degradation:** Queue requests during peak, don't reject

**Q3: "How would you monitor Bedrock model quality in production?"**

**Answer:**
```python
import boto3
import json

cloudwatch = boto3.client('cloudwatch')

class BedrockMonitor:
    def __init__(self):
        self.metrics_buffer = []

    def log_inference(self, user_query, response, latency_ms, cost):
        """
        Log every inference for analysis
        """
        log_entry = {
            'timestamp': time.time(),
            'query': user_query,
            'response': response,
            'latency_ms': latency_ms,
            'cost_usd': cost,
            'model_id': 'claude-3-5-sonnet',
            'tokens_input': response['usage']['input_tokens'],
            'tokens_output': response['usage']['output_tokens']
        }

        # Store in S3 for analysis
        s3.put_object(
            Bucket='bedrock-inference-logs',
            Key=f'logs/{datetime.now().strftime("%Y/%m/%d")}/{uuid.uuid4()}.json',
            Body=json.dumps(log_entry)
        )

        # Emit CloudWatch metrics
        self.emit_metrics(log_entry)

    def emit_metrics(self, log_entry):
        """
        Real-time metrics to CloudWatch
        """
        cloudwatch.put_metric_data(
            Namespace='Bedrock/Quality',
            MetricData=[
                {
                    'MetricName': 'Latency',
                    'Value': log_entry['latency_ms'],
                    'Unit': 'Milliseconds'
                },
                {
                    'MetricName': 'Cost',
                    'Value': log_entry['cost_usd'],
                    'Unit': 'None'
                },
                {
                    'MetricName': 'TokensUsed',
                    'Value': log_entry['tokens_input'] + log_entry['tokens_output'],
                    'Unit': 'Count'
                }
            ]
        )

    def analyze_quality(self):
        """
        Batch analysis of inference quality
        """
        # Run daily job to analyze logs
        # Check for:
        # - Increased refusal rates
        # - Latency degradation
        # - Cost spikes
        # - User complaints/feedback
        pass

# Quality checks specific to legal domain
def verify_legal_quality(response, expected_accuracy=0.95):
    """
    Legal-specific quality checks
    """
    checks = {
        'has_citations': bool(re.search(r'\d+\s+[A-Z]\.\w+\s+\d+', response)),
        'no_hallucinated_cases': verify_case_citations(response),
        'appropriate_disclaimer': 'not legal advice' in response.lower(),
        'clear_reasoning': len(response) > 100  # Not too terse
    }

    return all(checks.values())
```

---

## Lambda & Serverless Architecture

### Why Lambda Matters at TR

**Use Cases:**
- Event-driven processing (S3 upload → document analysis)
- API backends (lightweight, auto-scaling)
- Orchestration (Step Functions workflows)
- AI model integration (preprocessing, postprocessing)

### Key Lambda Patterns

#### 1. Document Processing Pipeline

```python
# Lambda triggered by S3 upload
import boto3
import json

s3 = boto3.client('s3')
bedrock = boto3.client('bedrock-runtime')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    """
    Process uploaded legal document
    """
    # Get uploaded file details
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Download document
    response = s3.get_object(Bucket=bucket, Key=key)
    document_text = response['Body'].read().decode('utf-8')

    # Extract metadata with Bedrock
    metadata = extract_document_metadata(document_text)

    # Store in DynamoDB
    table = dynamodb.Table('legal-documents')
    table.put_item(
        Item={
            'document_id': key,
            'upload_time': context.aws_request_id,
            'metadata': metadata,
            'status': 'processed'
        }
    )

    # Trigger downstream processing
    sns = boto3.client('sns')
    sns.publish(
        TopicArn='arn:aws:sns:us-east-1:123456789:document-processed',
        Message=json.dumps({'document_id': key})
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'document_id': key, 'status': 'processed'})
    }

def extract_document_metadata(text):
    """
    Use Bedrock to extract structured metadata
    """
    prompt = f"""Extract the following from this legal document:
- Document type (contract, brief, memo, etc.)
- Parties involved
- Key dates
- Jurisdiction

Document:
{text[:5000]}  # First 5000 chars

Respond in JSON format."""

    response = bedrock.invoke_model(
        modelId='anthropic.claude-3-haiku-20240307-v1:0',  # Fast model
        body=json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 500,
            "messages": [{"role": "user", "content": prompt}]
        })
    )

    return json.loads(response['body'].read())
```

#### 2. API Gateway + Lambda

```python
# RESTful API for CoCounsel
def lambda_handler(event, context):
    """
    Handle API requests for document analysis
    """
    # Parse request
    body = json.loads(event['body'])
    user_id = event['requestContext']['authorizer']['claims']['sub']
    document_id = body['document_id']
    analysis_type = body['analysis_type']  # 'summarize', 'extract', 'classify'

    # Rate limiting
    if not check_user_rate_limit(user_id):
        return {
            'statusCode': 429,
            'body': json.dumps({'error': 'Rate limit exceeded'})
        }

    # Get document from S3
    document = s3.get_object(
        Bucket='legal-documents',
        Key=f'{user_id}/{document_id}'
    )['Body'].read()

    # Process based on type
    if analysis_type == 'summarize':
        result = summarize_document(document)
    elif analysis_type == 'extract':
        result = extract_entities(document)
    elif analysis_type == 'classify':
        result = classify_document(document)
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid analysis type'})
        }

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'  # CORS
        },
        'body': json.dumps(result)
    }
```

#### 3. Step Functions Orchestration

```python
# Complex multi-step workflow
# Example: Deep Research workflow in CoCounsel

{
  "Comment": "Deep Research workflow",
  "StartAt": "PlanResearch",
  "States": {
    "PlanResearch": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:123456789:function:plan-research",
      "Next": "ParallelSearch"
    },
    "ParallelSearch": {
      "Type": "Parallel",
      "Branches": [
        {
          "StartAt": "SearchCases",
          "States": {
            "SearchCases": {
              "Type": "Task",
              "Resource": "arn:aws:lambda:us-east-1:123456789:function:search-cases",
              "End": true
            }
          }
        },
        {
          "StartAt": "SearchStatutes",
          "States": {
            "SearchStatutes": {
              "Type": "Task",
              "Resource": "arn:aws:lambda:us-east-1:123456789:function:search-statutes",
              "End": true
            }
          }
        },
        {
          "StartAt": "SearchSecondary",
          "States": {
            "SearchSecondary": {
              "Type": "Task",
              "Resource": "arn:aws:lambda:us-east-1:123456789:function:search-secondary",
              "End": true
            }
          }
        }
      ],
      "Next": "SynthesizeResults"
    },
    "SynthesizeResults": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:123456789:function:synthesize",
      "Next": "CheckCompleteness"
    },
    "CheckCompleteness": {
      "Type": "Choice",
      "Choices": [
        {
          "Variable": "$.completeness_score",
          "NumericGreaterThan": 0.9,
          "Next": "GenerateReport"
        }
      ],
      "Default": "PlanAdditionalResearch"
    },
    "PlanAdditionalResearch": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:123456789:function:plan-additional",
      "Next": "ParallelSearch"
    },
    "GenerateReport": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:123456789:function:generate-report",
      "End": true
    }
  }
}
```

**Why Step Functions:**
- **Agentic workflows:** Multi-step, iterative (Deep Research)
- **Parallel execution:** Search multiple sources simultaneously
- **Error handling:** Built-in retry logic
- **Visual workflow:** Easy to understand and debug
- **State management:** No need to manage state in Lambda

### Lambda Best Practices at TR

**1. Right-Sizing:**
```python
# Don't over-provision memory
# Test to find optimal memory (affects CPU too)

# For lightweight API: 512 MB
# For Bedrock calls: 1024 MB (network-bound)
# For document processing: 2048 MB (memory-intensive)
```

**2. Cold Start Mitigation:**
```python
# Use provisioned concurrency for user-facing APIs
aws lambda put-provisioned-concurrency-config \
    --function-name cocounsel-api \
    --provisioned-concurrent-executions 10  # Always warm

# For internal workflows: accept cold starts (cheaper)
```

**3. Timeout Configuration:**
```python
# Set reasonable timeouts
# API Gateway max: 29 seconds
# Lambda max: 15 minutes

# For API endpoints: 25 seconds
# For async processing: 5-10 minutes
# For Step Functions: 15 minutes per step
```

**4. Environment Variables & Secrets:**
```python
import os
import boto3

# Use environment variables for config
BEDROCK_MODEL = os.environ['BEDROCK_MODEL_ID']
DYNAMODB_TABLE = os.environ['DYNAMODB_TABLE']

# Use Parameter Store/Secrets Manager for secrets
ssm = boto3.client('ssm')
api_key = ssm.get_parameter(
    Name='/cocounsel/openai/api-key',
    WithDecryption=True
)['Parameter']['Value']
```

---

## Containers - ECS & Fargate

### Why ECS/Fargate at TR

**TR's Choice:**
- ECS/Fargate over EKS (Kubernetes)
- Why? Simpler, managed, less operational overhead
- Focus: Run containers, not manage orchestration

**Use Cases:**
- Modernized .NET applications (Windows → Linux containers)
- Microservices architecture
- Long-running services (not serverless-appropriate)

### ECS Architecture

```
┌─────────────────────────────────────────┐
│          Application Load Balancer       │
│        (distribute traffic)             │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│              ECS Service                 │
│  (desired count, auto-scaling)          │
└─────────────────────────────────────────┘
                  ↓
┌────────────┬────────────┬────────────┐
│  ECS Task  │  ECS Task  │  ECS Task  │
│  (Fargate) │  (Fargate) │  (Fargate) │
└────────────┴────────────┴────────────┘
       ↓            ↓            ↓
┌────────────────────────────────────────┐
│          Task Definition               │
│  - Docker image                        │
│  - CPU/memory allocation               │
│  - Environment variables               │
│  - IAM role                            │
└────────────────────────────────────────┘
```

### Key Patterns

#### 1. Microservice Deployment

```json
{
  "family": "cocounsel-document-service",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "1024",
  "memory": "2048",
  "containerDefinitions": [
    {
      "name": "document-service",
      "image": "123456789.dkr.ecr.us-east-1.amazonaws.com/document-service:latest",
      "portMappings": [
        {
          "containerPort": 8080,
          "protocol": "tcp"
        }
      ],
      "environment": [
        {
          "name": "BEDROCK_REGION",
          "value": "us-east-1"
        },
        {
          "name": "DYNAMODB_TABLE",
          "value": "documents"
        }
      ],
      "secrets": [
        {
          "name": "API_KEY",
          "valueFrom": "arn:aws:secretsmanager:us-east-1:123456789:secret:api-key"
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/document-service",
          "awslogs-region": "us-east-1",
          "awslogs-stream-prefix": "ecs"
        }
      },
      "healthCheck": {
        "command": ["CMD-SHELL", "curl -f http://localhost:8080/health || exit 1"],
        "interval": 30,
        "timeout": 5,
        "retries": 3
      }
    }
  ]
}
```

#### 2. Auto-Scaling Configuration

```python
import boto3

ecs = boto3.client('ecs')
autoscaling = boto3.client('application-autoscaling')

# Register service with auto-scaling
autoscaling.register_scalable_target(
    ServiceNamespace='ecs',
    ResourceId='service/cocounsel-cluster/document-service',
    ScalableDimension='ecs:service:DesiredCount',
    MinCapacity=2,  # Always run at least 2 for availability
    MaxCapacity=20  # Scale up to 20 during peak
)

# Target tracking scaling (based on CPU)
autoscaling.put_scaling_policy(
    PolicyName='cpu-target-tracking',
    ServiceNamespace='ecs',
    ResourceId='service/cocounsel-cluster/document-service',
    ScalableDimension='ecs:service:DesiredCount',
    PolicyType='TargetTrackingScaling',
    TargetTrackingScalingPolicyConfiguration={
        'TargetValue': 70.0,  # Keep CPU around 70%
        'PredefinedMetricSpecification': {
            'PredefinedMetricType': 'ECSServiceAverageCPUUtilization'
        },
        'ScaleInCooldown': 300,  # Wait 5 min before scaling down
        'ScaleOutCooldown': 60   # Wait 1 min before scaling up
    }
)

# Additional policy: scale based on request count
autoscaling.put_scaling_policy(
    PolicyName='request-target-tracking',
    ServiceNamespace='ecs',
    ResourceId='service/cocounsel-cluster/document-service',
    ScalableDimension='ecs:service:DesiredCount',
    PolicyType='TargetTrackingScaling',
    TargetTrackingScalingPolicyConfiguration={
        'TargetValue': 1000.0,  # 1000 requests per task
        'PredefinedMetricSpecification': {
            'PredefinedMetricType': 'ALBRequestCountPerTarget'
        }
    }
)
```

#### 3. Blue-Green Deployment

```python
# Blue-green deployment for zero-downtime updates
# CodeDeploy integration with ECS

deployment_config = {
    'version': 0.0,
    'Resources': [
        {
            'TargetService': {
                'Type': 'AWS::ECS::Service',
                'Properties': {
                    'TaskDefinition': 'new-task-definition-arn',
                    'LoadBalancerInfo': {
                        'ContainerName': 'document-service',
                        'ContainerPort': 8080
                    },
                    'PlatformVersion': 'LATEST'
                }
            }
        }
    ],
    'Hooks': [
        {
            'BeforeInstall': 'lambda-pre-deploy-validation'
        },
        {
            'AfterInstall': 'lambda-smoke-tests'
        },
        {
            'AfterAllowTestTraffic': 'lambda-integration-tests'
        },
        {
            'BeforeAllowTraffic': 'lambda-final-validation'
        }
    ]
}

# Deployment process:
# 1. Deploy new task definition (green)
# 2. Run smoke tests
# 3. Shift 10% traffic to green
# 4. Monitor metrics (5 minutes)
# 5. Shift 50% traffic
# 6. Monitor metrics (5 minutes)
# 7. Shift 100% traffic
# 8. Terminate blue tasks
```

### .NET Modernization on ECS

**TR's Journey:**
```
Legacy .NET Framework (Windows)
    ↓
[AWS Transform - AI Modernization]
    ↓
.NET 8 (Cross-platform)
    ↓
[Containerization]
    ↓
Linux Containers on Fargate
    ↓
30% cost reduction + 70% tech debt reduction
```

**Why This Matters:**
- **1.5M lines of code** modernized monthly
- **4x speed improvement**
- Shows TR's commitment to modernization
- Principal Engineer may lead similar efforts

---

## Data Services

### S3 - Object Storage

**TR's S3 Usage:**
- ML training datasets
- Legal document repository (40,000+ databases)
- Data lakes for analytics
- Model artifacts storage
- Backup and archival

**Key Patterns:**

#### 1. Intelligent Tiering

```python
# Automatic cost optimization
lifecycle_policy = {
    'Rules': [
        {
            'Id': 'IntelligentTieringForTrainingData',
            'Status': 'Enabled',
            'Transitions': [
                {
                    'Days': 30,
                    'StorageClass': 'INTELLIGENT_TIERING'
                },
                {
                    'Days': 90,
                    'StorageClass': 'GLACIER'
                }
            ],
            'NoncurrentVersionTransitions': [
                {
                    'NoncurrentDays': 30,
                    'StorageClass': 'GLACIER'
                }
            ]
        }
    ]
}

s3.put_bucket_lifecycle_configuration(
    Bucket='sagemaker-training-data',
    LifecycleConfiguration=lifecycle_policy
)
```

#### 2. S3 Select (Query in Place)

```python
# Query data without downloading (cost/speed optimization)
response = s3.select_object_content(
    Bucket='legal-documents',
    Key='case-law/2024/cases.csv',
    ExpressionType='SQL',
    Expression="SELECT * FROM s3object s WHERE s.jurisdiction = 'California' AND s.date > '2024-01-01'",
    InputSerialization={
        'CSV': {'FileHeaderInfo': 'USE'},
        'CompressionType': 'GZIP'
    },
    OutputSerialization={'JSON': {}}
)

# Process results
for event in response['Payload']:
    if 'Records' in event:
        records = event['Records']['Payload'].decode('utf-8')
        # Process records
```

### DynamoDB - NoSQL Database

**TR's DynamoDB Usage:**
- Low-latency document metadata
- User sessions and preferences
- Real-time application data
- OpenArena user activity tracking

**Key Patterns:**

#### 1. Single-Table Design

```python
# Efficient data modeling for multiple entity types
# Example: Documents, users, and sessions in one table

table_definition = {
    'TableName': 'cocounsel-data',
    'KeySchema': [
        {'AttributeName': 'PK', 'KeyType': 'HASH'},   # Partition key
        {'AttributeName': 'SK', 'KeyType': 'RANGE'}   # Sort key
    ],
    'AttributeDefinitions': [
        {'AttributeName': 'PK', 'AttributeType': 'S'},
        {'AttributeName': 'SK', 'AttributeType': 'S'},
        {'AttributeName': 'GSI1PK', 'AttributeType': 'S'},
        {'AttributeName': 'GSI1SK', 'AttributeType': 'S'}
    ],
    'GlobalSecondaryIndexes': [
        {
            'IndexName': 'GSI1',
            'KeySchema': [
                {'AttributeName': 'GSI1PK', 'KeyType': 'HASH'},
                {'AttributeName': 'GSI1SK', 'KeyType': 'RANGE'}
            ],
            'Projection': {'ProjectionType': 'ALL'}
        }
    ],
    'BillingMode': 'PAY_PER_REQUEST'  # On-demand (elastic)
}

# Example data patterns:
# User: PK=USER#123, SK=PROFILE
# Document: PK=USER#123, SK=DOC#456
# Session: PK=USER#123, SK=SESSION#789
# Query by document date: GSI1PK=USER#123, GSI1SK=DATE#2024-11-21
```

#### 2. DynamoDB Streams + Lambda

```python
# Real-time processing of data changes
def lambda_handler(event, context):
    """
    Trigger downstream processing when documents are added
    """
    for record in event['Records']:
        if record['eventName'] == 'INSERT':
            new_image = record['dynamodb']['NewImage']
            document_id = new_image['PK']['S']

            # Trigger document indexing for search
            trigger_opensearch_indexing(document_id)

            # Update user analytics
            update_user_metrics(new_image['user_id']['S'])

            # Send notification
            send_notification(new_image)
```

### Redshift - Data Warehouse

**TR's Redshift Usage:**
- Analytics and BI
- User behavior analysis
- Product usage metrics
- Business intelligence reporting

**Key Queries:**

```sql
-- Example: User adoption analysis
SELECT
    DATE_TRUNC('month', usage_date) AS month,
    product,
    COUNT(DISTINCT user_id) AS active_users,
    SUM(api_calls) AS total_calls,
    AVG(response_time_ms) AS avg_latency
FROM product_usage
WHERE usage_date >= DATE_ADD('month', -6, CURRENT_DATE)
GROUP BY month, product
ORDER BY month DESC, product;

-- Example: Feature usage trends
SELECT
    feature_name,
    COUNT(*) AS usage_count,
    COUNT(DISTINCT user_id) AS unique_users,
    AVG(session_duration_seconds) AS avg_duration
FROM feature_usage
WHERE usage_date = CURRENT_DATE
GROUP BY feature_name
ORDER BY usage_count DESC
LIMIT 10;
```

---

## Networking & Security

### VPC Architecture

**TR's Network Design (Typical):**

```
┌─────────────────────────────────────────────────────────┐
│                        VPC                              │
│                 (10.0.0.0/16)                           │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────────┐  ┌──────────────────┐           │
│  │  Public Subnet   │  │  Public Subnet   │           │
│  │   (AZ-1)         │  │   (AZ-2)         │           │
│  │  - NAT Gateway   │  │  - NAT Gateway   │           │
│  │  - ALB           │  │  - ALB           │           │
│  └──────────────────┘  └──────────────────┘           │
│           ↓                     ↓                       │
│  ┌──────────────────┐  ┌──────────────────┐           │
│  │ Private Subnet   │  │ Private Subnet   │           │
│  │   (AZ-1)         │  │   (AZ-2)         │           │
│  │  - ECS Tasks     │  │  - ECS Tasks     │           │
│  │  - Lambda        │  │  - Lambda        │           │
│  └──────────────────┘  └──────────────────┘           │
│           ↓                     ↓                       │
│  ┌──────────────────┐  ┌──────────────────┐           │
│  │ Database Subnet  │  │ Database Subnet  │           │
│  │   (AZ-1)         │  │   (AZ-2)         │           │
│  │  - RDS           │  │  - RDS           │           │
│  │  - OpenSearch    │  │  - OpenSearch    │           │
│  └──────────────────┘  └──────────────────┘           │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Key Principles:**
- **Multi-AZ:** High availability across availability zones
- **Private subnets:** Application and data layers not publicly accessible
- **Security groups:** Firewall rules at instance level
- **NACLs:** Subnet-level firewalls (defense in depth)

### IAM Best Practices

#### 1. Least Privilege

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "SageMakerTrainingJobAccess",
      "Effect": "Allow",
      "Action": [
        "sagemaker:CreateTrainingJob",
        "sagemaker:DescribeTrainingJob",
        "sagemaker:StopTrainingJob"
      ],
      "Resource": "arn:aws:sagemaker:us-east-1:123456789:training-job/legal-*",
      "Condition": {
        "StringEquals": {
          "aws:RequestedRegion": "us-east-1"
        }
      }
    },
    {
      "Sid": "S3TrainingDataAccess",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::training-data-bucket",
        "arn:aws:s3:::training-data-bucket/legal/*"
      ]
    }
  ]
}
```

#### 2. Role-Based Access

```python
# Lambda execution role
lambda_role = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel"
            ],
            "Resource": "arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:PutItem",
                "dynamodb:GetItem"
            ],
            "Resource": "arn:aws:dynamodb:us-east-1:123456789:table/documents"
        }
    ]
}
```

### Encryption

**At Rest:**
- S3: Server-side encryption (SSE-S3, SSE-KMS)
- DynamoDB: Encryption enabled by default
- RDS: Encrypted storage
- SageMaker: Encrypted training volumes

**In Transit:**
- TLS/SSL for all API calls
- VPC endpoints for AWS services (no internet)
- Private Link for Bedrock (TR uses this)

**Example: KMS Key Policy**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Enable IAM User Permissions",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789:root"
      },
      "Action": "kms:*",
      "Resource": "*"
    },
    {
      "Sid": "Allow SageMaker to use key",
      "Effect": "Allow",
      "Principal": {
        "Service": "sagemaker.amazonaws.com"
      },
      "Action": [
        "kms:Decrypt",
        "kms:DescribeKey",
        "kms:CreateGrant"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "sagemaker.us-east-1.amazonaws.com"
        }
      }
    }
  ]
}
```

---

## MLOps on AWS

### TR's MLOps Maturity

**Level 5 (Fully Automated):**
- ✅ Automated training pipelines
- ✅ Automated model registration
- ✅ Automated deployment
- ✅ Automated monitoring
- ✅ Automated retraining

### Complete MLOps Stack

```
Code Repository (CodeCommit/GitHub)
    ↓
CI/CD (CodePipeline + CodeBuild)
    ↓
SageMaker Pipelines (Training + Evaluation)
    ↓
Model Registry (Version Control)
    ↓
Approval Workflow (Manual for legal models)
    ↓
Deployment (Blue-Green via CodeDeploy)
    ↓
Monitoring (Model Monitor + CloudWatch)
    ↓
Drift Detection → Alert → Retrain
```

### Key Components

#### 1. Feature Store

```python
from sagemaker.feature_store.feature_group import FeatureGroup

# Define feature group
feature_group = FeatureGroup(
    name='legal-document-features',
    sagemaker_session=sagemaker_session
)

# Create feature definitions
feature_group.load_feature_definitions(
    data_frame=features_df
)

# Create feature group
feature_group.create(
    s3_uri=f's3://bucket/feature-store/',
    record_identifier_name='document_id',
    event_time_feature_name='event_time',
    role_arn=role,
    enable_online_store=True  # Low-latency access
)

# Ingest features
feature_group.ingest(
    data_frame=features_df,
    max_workers=5,
    wait=True
)

# Query features for training
query = feature_group.athena_query()
table = query.table_name
query_string = f'SELECT * FROM "{table}" WHERE jurisdiction = \'California\''
query.run(query_string)
query.wait()
features = query.as_dataframe()
```

#### 2. Model Lineage

```python
# Track complete model lineage
from sagemaker.lineage.visualizer import LineageTableVisualizer

# Visualize lineage
viz = LineageTableVisualizer(sagemaker_session)

# For a specific model
viz.show(model_package_arn=model_package_arn)

# Shows:
# - Training data sources
# - Code version
# - Hyperparameters
# - Evaluation metrics
# - Deployment history
```

#### 3. A/B Testing

```python
# Traffic splitting between model versions
from sagemaker.predictor import Predictor

# Deploy two variants
predictor = model_v1.deploy(
    initial_instance_count=1,
    instance_type='ml.m5.xlarge',
    endpoint_name='legal-classifier',
    variant_name='ModelV1',
    initial_variant_weight=0.9  # 90% traffic
)

# Add second variant
predictor.add_model_variant(
    model=model_v2,
    variant_name='ModelV2',
    initial_instance_count=1,
    instance_type='ml.m5.xlarge',
    initial_variant_weight=0.1  # 10% traffic
)

# Monitor metrics
# If ModelV2 performs better:
predictor.update_endpoint_weights_and_capacities(
    desired_weights_and_capacities=[
        {
            'VariantName': 'ModelV1',
            'DesiredWeight': 0.5  # Reduce to 50%
        },
        {
            'VariantName': 'ModelV2',
            'DesiredWeight': 0.5  # Increase to 50%
        }
    ]
)
```

---

## Cost Optimization

### TR's Cost Optimization Strategies

**Results:**
- **30% cost reduction** (Windows → Linux containers)
- **70-90% savings** (Spot instances for training)
- **Efficient scaling** (19,000 users in Open Arena)

### Key Techniques

#### 1. Compute Optimization

**SageMaker:**
- Spot instances for training (70-90% savings)
- Auto-shutdown GPUs after training
- Multi-model endpoints (share infrastructure)
- Right-sizing instances

**EC2:**
- Spot instances for non-critical workloads
- Reserved instances for steady-state (up to 72% savings)
- Savings Plans for flexible commitment

**Lambda:**
- Right-size memory (affects cost directly)
- Provisioned concurrency only for critical functions
- Async invocation where possible

#### 2. Storage Optimization

```python
# Intelligent tiering + lifecycle policies
lifecycle_policy = {
    'Rules': [
        {
            'Id': 'CostOptimization',
            'Status': 'Enabled',
            'Transitions': [
                # Frequently accessed data
                {
                    'Days': 0,
                    'StorageClass': 'INTELLIGENT_TIERING'
                },
                # Infrequently accessed
                {
                    'Days': 90,
                    'StorageClass': 'GLACIER_IR'  # Instant Retrieval
                },
                # Archive
                {
                    'Days': 365,
                    'StorageClass': 'DEEP_ARCHIVE'
                }
            ],
            'NoncurrentVersionExpiration': {
                'NoncurrentDays': 90  # Delete old versions
            }
        }
    ]
}
```

#### 3. Data Transfer Optimization

- **VPC Endpoints:** No internet gateway costs
- **S3 Transfer Acceleration:** Faster uploads (worth the cost for large files)
- **CloudFront:** Cache static content (reduce origin requests)
- **Regional resources:** Minimize cross-region traffic

#### 4. Monitoring Costs

```python
# Set up cost alerts
import boto3

cloudwatch = boto3.client('cloudwatch')
sns = boto3.client('sns')

# Create budget alarm
cloudwatch.put_metric_alarm(
    AlarmName='BedrockCostAlert',
    ComparisonOperator='GreaterThanThreshold',
    EvaluationPeriods=1,
    MetricName='EstimatedCharges',
    Namespace='AWS/Billing',
    Period=21600,  # 6 hours
    Statistic='Maximum',
    Threshold=10000.0,  # $10k
    ActionsEnabled=True,
    AlarmActions=[
        'arn:aws:sns:us-east-1:123456789:cost-alerts'
    ],
    AlarmDescription='Alert when Bedrock costs exceed $10k',
    Dimensions=[
        {
            'Name': 'ServiceName',
            'Value': 'Amazon Bedrock'
        }
    ]
)
```

---

## Interview Questions & Scenarios

### Scenario 1: Design RAG System on AWS

**Question:**
> "Design a RAG system for legal research that serves 20,000 attorneys. Focus on AWS services, scalability, and cost."

**Expected Answer Structure:**

```
1. Architecture Overview
┌────────────────────────────────────────────────────────┐
│                   User Interface                       │
│              (React App on CloudFront)                 │
└────────────────────────────────────────────────────────┘
                        ↓
┌────────────────────────────────────────────────────────┐
│              API Gateway + Lambda                      │
│         (Authentication, Rate Limiting)                │
└────────────────────────────────────────────────────────┘
                        ↓
┌────────────────────────────────────────────────────────┐
│           Retrieval Layer (Lambda)                     │
│  ├─ Query understanding                                │
│  ├─ Vector search (OpenSearch)                         │
│  └─ Context ranking                                    │
└────────────────────────────────────────────────────────┘
                        ↓
┌────────────────────────────────────────────────────────┐
│          Content Storage                               │
│  ├─ Documents (S3)                                     │
│  ├─ Embeddings (OpenSearch vector index)               │
│  └─ Metadata (DynamoDB)                                │
└────────────────────────────────────────────────────────┘
                        ↓
┌────────────────────────────────────────────────────────┐
│            Amazon Bedrock                              │
│  ├─ Claude for generation                              │
│  ├─ Prompt caching                                     │
│  └─ Response streaming                                 │
└────────────────────────────────────────────────────────┘

2. Scalability Considerations
- API Gateway: Auto-scales to millions of requests
- Lambda: Concurrent execution limits (1000 default, request increase)
- OpenSearch: Multi-node cluster, auto-scaling
- Bedrock: Managed, auto-scales
- DynamoDB: On-demand pricing, auto-scales

3. Cost Optimization
- Lambda: Right-sized memory, provisioned concurrency for peak hours only
- OpenSearch: Reserved instances for base load, on-demand for spikes
- Bedrock: Prompt caching (90% of context repeated)
- S3: Intelligent tiering for documents

4. Latency Targets
- P50: < 2 seconds
- P99: < 5 seconds
- Strategy:
  - CloudFront caching for static assets
  - DynamoDB for low-latency metadata
  - Parallel retrieval (fetch multiple docs simultaneously)
  - Streaming responses from Bedrock

5. Monitoring
- CloudWatch: Latency, error rates, costs
- X-Ray: Distributed tracing
- Custom metrics: Citation accuracy, user satisfaction
```

### Scenario 2: Model Drift Detected

**Question:**
> "Your legal document classifier's accuracy dropped from 95% to 87%. Walk me through debugging and resolving this."

**Expected Answer:**

```
1. Immediate Actions (5 minutes)
- Check SageMaker Model Monitor dashboard
- Review recent alerts
- Check if deployment happened recently (bad model?)
- Verify endpoint is healthy (not infrastructure issue)

2. Data Analysis (30 minutes)
- Pull sample of recent predictions from Data Capture
- Compare input distribution vs training distribution
  → Look for data drift
- Analyze misclassifications:
  → Are errors concentrated in specific categories?
  → New document types appearing?
  → Changed terminology?

3. Investigation (1-2 hours)
import pandas as pd
from scipy.stats import ks_2samp

# Get captured data
recent_data = get_recent_predictions(days=7)
training_data = get_training_data()

# Check feature drift
for feature in features:
    stat, p_value = ks_2samp(
        recent_data[feature],
        training_data[feature]
    )
    if p_value < 0.05:
        print(f"Drift detected in {feature}: p={p_value}")

# Analyze misclassifications
errors = recent_data[recent_data['prediction'] != recent_data['actual']]
print(errors.groupby('document_type').size())

4. Root Cause Determination
Common causes:
- Data drift: New legal terminology, case types
- Concept drift: Legal standards changed
- Upstream issues: Document preprocessing changed
- Bad deployment: Wrong model version
- External factors: New data source added

5. Resolution Strategy
If data drift:
- Retrain with recent data
- Update feature engineering
- Add new document types to training set

If concept drift:
- Consult legal experts
- Update labels for recent cases
- Retrain with corrected labels

If deployment issue:
- Rollback to previous version
- Fix CI/CD pipeline
- Add validation step

6. Prevention
- Continuous monitoring
- Automated retraining schedule
- Human-in-the-loop for edge cases
- A/B testing before full rollout
- Gradual traffic shifting

7. Communication
- Alert stakeholders
- Provide ETA for fix
- Post-incident review
- Update runbooks
```

### Scenario 3: Cost Spike Investigation

**Question:**
> "Your AWS bill for Bedrock jumped from $10k to $50k this month. How do you investigate?"

**Expected Answer:**

```
1. Immediate Investigation (10 minutes)
- Check AWS Cost Explorer
- Filter by service (Bedrock)
- Group by API operation
- Identify spike date

2. Detailed Analysis (30 minutes)
# Query CloudWatch Logs Insights
fields @timestamp, modelId, inputTokens, outputTokens, @message
| filter @message like /InvokeModel/
| stats sum(inputTokens) as totalInput,
        sum(outputTokens) as totalOutput,
        count() as requestCount by modelId
| sort totalOutput desc

Results might show:
- Model changed (Haiku → Sonnet = 5x cost increase)
- Output tokens exploded (generation not stopping?)
- Request count spiked (DDoS? Bug causing retry loops?)

3. Common Causes
a) Model Selection Issue
- Accidentally using Sonnet for all requests (should use Haiku for simple tasks)
- Fix: Review model selection logic

b) Token Explosion
- Prompts too long (including unnecessary context)
- Responses too long (max_tokens too high)
- Fix: Optimize prompts, tune max_tokens

c) Request Volume Spike
- Viral feature adoption
- Bug causing infinite loops
- DDoS or abuse
- Fix: Rate limiting, investigation

d) Prompt Caching Not Working
- Cache misses due to slight prompt variations
- Fix: Normalize prompts for consistency

4. Deep Dive Example
import boto3
import pandas as pd

# Get detailed cost data
ce = boto3.client('ce')

response = ce.get_cost_and_usage(
    TimePeriod={
        'Start': '2024-11-01',
        'End': '2024-11-30'
    },
    Granularity='DAILY',
    Filter={
        'Dimensions': {
            'Key': 'SERVICE',
            'Values': ['Amazon Bedrock']
        }
    },
    Metrics=['UnblendedCost'],
    GroupBy=[
        {'Type': 'DIMENSION', 'Key': 'USAGE_TYPE'}
    ]
)

# Analyze daily costs
# Identify anomaly date
# Cross-reference with deployments, incidents

5. Remediation
Short-term:
- Implement rate limiting
- Add cost alerts
- Review and optimize expensive queries
- Enable prompt caching

Long-term:
- Automated model selection (task → cheapest suitable model)
- Prompt optimization pipeline
- User tiers with quota limits
- Reserved capacity for predictable workloads

6. Prevention
- Cost anomaly detection (automated)
- Budget alerts at multiple thresholds
- Regular cost reviews
- Cost allocation tags (by team, feature, env)
- Load testing with cost monitoring
```

---

## Study Checklist

### Must Know (Critical)

**SageMaker:**
- [ ] End-to-end ML workflow
- [ ] Training job configuration (distributed, spot)
- [ ] Model Registry and versioning
- [ ] SageMaker Pipelines (MLOps)
- [ ] Deployment patterns (real-time, batch, multi-model)
- [ ] Model Monitor (drift detection)

**Bedrock:**
- [ ] Model selection strategy
- [ ] RAG integration patterns
- [ ] Cost optimization (prompt caching)
- [ ] Security (data privacy, no training)
- [ ] Bedrock Flows

**Lambda:**
- [ ] Event-driven patterns
- [ ] Integration with S3, DynamoDB, API Gateway
- [ ] Step Functions orchestration
- [ ] Cost optimization (right-sizing, provisioned concurrency)

**ECS/Fargate:**
- [ ] Task definitions
- [ ] Service auto-scaling
- [ ] Blue-green deployments
- [ ] Networking (ALB, VPC)

### Should Know (Important)

**Data Services:**
- [ ] S3 lifecycle policies, Intelligent Tiering
- [ ] DynamoDB single-table design
- [ ] Redshift for analytics
- [ ] OpenSearch for vector search

**Networking:**
- [ ] VPC architecture (public/private subnets)
- [ ] Security groups vs NACLs
- [ ] VPC endpoints

**Security:**
- [ ] IAM policies (least privilege)
- [ ] Encryption (at rest, in transit)
- [ ] KMS key management
- [ ] Secrets Manager

**Monitoring:**
- [ ] CloudWatch (metrics, logs, alarms)
- [ ] Cost monitoring and alerts
- [ ] Distributed tracing

### Nice to Have (Good to Know)

- [ ] CDK for Infrastructure as Code
- [ ] CodePipeline for CI/CD
- [ ] AWS Transform for .NET modernization
- [ ] CloudFront for content delivery
- [ ] EventBridge for event routing

---

## Hands-On Practice Recommendations

### 1. Build a Mini RAG System

**Project:** Simple legal Q&A system

```
Components:
1. Upload PDFs to S3
2. Lambda to process and chunk documents
3. Generate embeddings (SageMaker or Bedrock Embeddings)
4. Store in OpenSearch
5. Query endpoint (Lambda + API Gateway)
6. LLM generation (Bedrock)

Time: 4-6 hours
Cost: ~$10
```

### 2. Implement MLOps Pipeline

**Project:** Train and deploy a model with full automation

```
Components:
1. Sample dataset in S3
2. SageMaker Pipeline:
   - Preprocessing
   - Training
   - Evaluation
   - Conditional registration
3. Deploy to endpoint with auto-scaling
4. Set up Model Monitor

Time: 6-8 hours
Cost: ~$20-30
```

### 3. Cost Optimization Exercise

**Project:** Optimize an expensive ML workload

```
Baseline:
- Training: 4x ml.p3.8xlarge, on-demand = $48/hour
- Inference: 5x ml.m5.2xlarge, always on = $4/hour
- Monthly: ~$3,000

Optimized:
- Training: 4x ml.p3.8xlarge, spot = $9.60/hour (80% savings)
- Inference: Multi-model endpoint, auto-scaling 1-5 = $0.80-4/hour
- Monthly: ~$800

Time: 2-3 hours to implement
Savings: 73%
```

---

## Final Tips for Interview

### DO:
- ✅ Mention TR-specific patterns (SageMaker, Bedrock, ECS/Fargate)
- ✅ Discuss cost optimization (they care about this)
- ✅ Show understanding of legal domain requirements (accuracy, compliance)
- ✅ Emphasize managed services (less operational overhead)
- ✅ Talk about monitoring and observability
- ✅ Mention multi-model strategy

### DON'T:
- ❌ Suggest GCP/Azure without acknowledging TR is AWS-focused
- ❌ Over-engineer (Kubernetes when Fargate suffices)
- ❌ Ignore costs (always discuss optimization)
- ❌ Skip security/compliance (critical for legal industry)
- ❌ Forget monitoring (production systems need observability)

### Key Phrases to Use:
- "At Thomson Reuters' scale..."
- "Given the legal industry requirements..."
- "Balancing cost and performance..."
- "For 19,000 users in Open Arena..."
- "Following AWS best practices..."
- "With SageMaker, we can..."
- "Using Bedrock's managed service..."

---

**Good luck with your interviews!**

*Document created: November 21, 2025*
*For: Thomson Reuters Principal AI Engineer position*
*Focus: AWS technical interview preparation*
