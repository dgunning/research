# Thomson Reuters - Principal AI Engineer Assessment

**Duration**: 180 minutes (3 hours)
**Total Points**: 100
**Passing Score**: 70/100
**Language**: Python 3.11+

---

## Test Structure

| Section | Questions | Points | Time Guideline |
|---------|-----------|--------|----------------|
| 1. Multiple Choice (ML/AI) | 15 | 15 | 20 min |
| 2. SQL & Data Analysis | 3 | 15 | 25 min |
| 3. Coding Problems | 4 | 40 | 90 min |
| 4. System Design | 2 | 30 | 45 min |
| **TOTAL** | **24** | **100** | **180 min** |

---

## Instructions

1. **Environment**: Python 3.11+, standard libraries + pandas, numpy, sklearn
2. **Submission**: All code must run without errors to receive credit
3. **Testing**: Your code will be tested against hidden test cases
4. **Documentation**: Comment your code for partial credit
5. **Plagiarism**: Using external AI assistants or copying code will result in disqualification

---

# Section 1: Multiple Choice Questions (15 points)

**Time**: 20 minutes | **Points**: 1 point each

---

## Question 1.1: RAG Architecture

In a RAG (Retrieval-Augmented Generation) system for legal documents, which component is most critical for ensuring citation accuracy?

A) The size of the embedding model
B) The chunk size used for document segmentation
C) The mapping between retrieved chunks and source document metadata
D) The temperature parameter of the LLM

**Answer**: ___

---

## Question 1.2: Vector Search

You're building a vector search system for 100M legal documents. Which approach will provide the best balance of speed and accuracy?

A) Exact k-NN search with brute force
B) HNSW (Hierarchical Navigable Small World) index
C) LSH (Locality-Sensitive Hashing)
D) Simple cosine similarity with linear scan

**Answer**: ___

---

## Question 1.3: LLM Context Windows

Your RAG system retrieves 20 relevant document chunks (500 tokens each) for a legal query. The LLM has a 32K token context window. What's the best strategy?

A) Concatenate all chunks and hope they fit
B) Use only the top 5 chunks to leave room for generation
C) Implement a ranking/re-ranking system to select most relevant chunks
D) Summarize each chunk first, then concatenate

**Answer**: ___

---

## Question 1.4: Prompt Engineering

For a legal contract analysis task, which prompt structure is most effective?

A) Direct question: "What are the key terms?"
B) Few-shot with examples of good analysis
C) Chain-of-thought with step-by-step reasoning
D) System prompt with role definition + structured output format + reasoning

**Answer**: ___

---

## Question 1.5: Model Drift Detection

Which metric is LEAST useful for detecting quality drift in a legal document classification model?

A) Prediction confidence distribution over time
B) Feature distribution shifts
C) Model inference latency
D) Label distribution of predictions

**Answer**: ___

---

## Question 1.6: Embedding Models

For legal documents, which approach typically produces the best embeddings?

A) Word2Vec trained on general text
B) OpenAI ada-002 embeddings
C) Domain-specific BERT fine-tuned on legal corpus
D) TF-IDF vectors

**Answer**: ___

---

## Question 1.7: Production ML

You deploy an LLM-based feature and observe 95th percentile latency is 8 seconds (target: 2s). What's the FIRST optimization to try?

A) Use a smaller model
B) Implement response streaming
C) Profile the system to identify bottlenecks
D) Add more GPU instances

**Answer**: ___

---

## Question 1.8: Evaluation Metrics

For a legal Q&A system, which metric is most important?

A) BLEU score
B) Response time
C) Citation accuracy and factual correctness
D) User engagement (clicks)

**Answer**: ___

---

## Question 1.9: Semantic Search

You implement semantic search but users complain it misses exact matches (e.g., case numbers, statute sections). What's the best fix?

A) Increase embedding dimension
B) Implement hybrid search (semantic + keyword)
C) Use a larger embedding model
D) Lower the similarity threshold

**Answer**: ___

---

## Question 1.10: Fine-tuning vs RAG

When should you choose fine-tuning over RAG for a legal AI application?

A) When you need up-to-date information
B) When you need to teach the model new reasoning patterns
C) When you want to cite sources
D) When you have limited training data

**Answer**: ___

---

## Question 1.11: Cost Optimization

Your LLM API costs are $50K/month. Which optimization typically provides the largest cost reduction?

A) Prompt compression (removing unnecessary tokens)
B) Caching responses by semantic similarity
C) Using a smaller model for 80% of queries
D) Batch processing queries

**Answer**: ___

---

## Question 1.12: Data Privacy

For GDPR compliance in an AI system processing legal documents, which is required?

A) Encrypting all data at rest
B) Right to deletion of training data and model retraining
C) Using only open-source models
D) Hosting in Europe

**Answer**: ___

---

## Question 1.13: Transformer Architecture

In a transformer model, what does the attention mechanism primarily compute?

A) The similarity between query and key vectors
B) The gradient of the loss function
C) The probability distribution over vocabulary
D) The embedding of input tokens

**Answer**: ___

---

## Question 1.14: MLOps Best Practice

Which is the most important quality gate before deploying a new model version to production?

A) Model accuracy improved by at least 1%
B) Model performs better than current production model on holdout set
C) Model training completed without errors
D) Model uses fewer parameters than previous version

**Answer**: ___

---

## Question 1.15: System Reliability

For a legal AI service with 99.95% SLA, what's the maximum acceptable downtime per year?

A) 4.38 hours
B) 8.76 hours
C) 26.3 hours
D) 52.6 hours

**Answer**: ___

---

# Section 2: SQL & Data Analysis (15 points)

**Time**: 25 minutes

---

## Question 2.1: Query Performance Analysis (5 points)

You have a table `legal_documents` with 100M rows:

```sql
CREATE TABLE legal_documents (
    doc_id VARCHAR(50) PRIMARY KEY,
    document_type VARCHAR(50),
    jurisdiction VARCHAR(50),
    date_filed DATE,
    content TEXT,
    embedding_vector FLOAT[768]
);

-- Current indexes:
CREATE INDEX idx_date ON legal_documents(date_filed);
```

**Query that's running slow:**
```sql
SELECT doc_id, document_type, date_filed
FROM legal_documents
WHERE jurisdiction = 'Federal'
  AND document_type = 'Contract'
  AND date_filed >= '2020-01-01'
ORDER BY date_filed DESC
LIMIT 100;
```

**Questions:**

a) Why is this query slow? (2 points)

**Your Answer:**
_______________

b) What index(es) would you create to optimize it? Write the SQL. (3 points)

**Your SQL:**
```sql
-- Your index creation statement(s) here
```

---

## Question 2.2: ML Model Performance Analysis (5 points)

You have a table tracking model predictions:

```sql
CREATE TABLE model_predictions (
    prediction_id BIGINT PRIMARY KEY,
    model_version VARCHAR(20),
    prediction_date DATE,
    predicted_class VARCHAR(50),
    confidence FLOAT,
    actual_class VARCHAR(50),  -- NULL until labeled
    processing_time_ms INT
);
```

**Write a query to calculate the following for each model version:**
- Total predictions
- Average confidence
- Accuracy (where actual_class is not NULL)
- 95th percentile processing time

**Your SQL:**
```sql
-- Your query here
```

---

## Question 2.3: Document Retrieval Analytics (5 points)

You have tables tracking RAG system performance:

```sql
CREATE TABLE queries (
    query_id BIGINT PRIMARY KEY,
    user_id VARCHAR(50),
    query_text TEXT,
    timestamp TIMESTAMP
);

CREATE TABLE retrieved_documents (
    query_id BIGINT,
    doc_id VARCHAR(50),
    rank INT,  -- 1 = top result
    relevance_score FLOAT,
    FOREIGN KEY (query_id) REFERENCES queries(query_id)
);

CREATE TABLE user_clicks (
    query_id BIGINT,
    doc_id VARCHAR(50),
    click_timestamp TIMESTAMP,
    FOREIGN KEY (query_id) REFERENCES queries(query_id)
);
```

**Write a query to calculate MRR (Mean Reciprocal Rank) by day for the last 30 days.**

MRR is calculated as: `1/rank` of the first clicked document, averaged across all queries.

**Your SQL:**
```sql
-- Your query here
```

---

# Section 3: Coding Problems (40 points)

**Time**: 90 minutes

---

## Problem 3.1: Document Chunking (8 points)

**Difficulty**: Medium
**Time**: 15 minutes

### Problem Statement

Implement a function to intelligently chunk legal documents for RAG. Legal documents have special structure (sections, subsections, citations) that should be preserved.

### Requirements

1. Split document into chunks of approximately `target_size` tokens
2. Try to break at section boundaries (lines starting with numbers like "1.", "1.1", etc.)
3. If a section is larger than `max_size`, split it but include section header in each chunk
4. Maintain document structure and context

### Function Signature

```python
def chunk_legal_document(
    document: str,
    target_size: int = 500,
    max_size: int = 1000
) -> list[dict]:
    """
    Chunk a legal document intelligently.

    Args:
        document: Full text of legal document
        target_size: Target chunk size in tokens (approximate)
        max_size: Maximum chunk size in tokens

    Returns:
        List of dictionaries with keys:
        - 'text': The chunk text
        - 'section': Section number/header if available
        - 'start_pos': Starting character position
        - 'end_pos': Ending character position
    """
    pass
```

### Example

```python
document = """
1. Parties
This Agreement is between Company A and Company B.

1.1 Company A
Company A is a Delaware corporation with principal place of business...
(500 more words)

1.2 Company B
Company B is a California corporation...
(500 more words)

2. Terms
The term of this agreement shall be...
"""

chunks = chunk_legal_document(document, target_size=200, max_size=400)
print(len(chunks))  # Should be 3-4 chunks
print(chunks[0]['section'])  # Should be "1. Parties"
```

### Constraints

- Document length: 1-100,000 characters
- Target size: 100-1000 tokens
- Use simple word count as token approximation (1 token ≈ 0.75 words)

### Test Cases

Your solution will be tested against:
- Documents with clear section structure
- Documents with nested sections (1.1.1, 1.1.2, etc.)
- Documents without clear structure
- Very long sections that exceed max_size

---

## Problem 3.2: Semantic Deduplication (10 points)

**Difficulty**: Medium-Hard
**Time**: 20 minutes

### Problem Statement

Implement a function to deduplicate similar documents using embeddings. In a legal database, the same document might appear multiple times with minor differences (typos, formatting). You need to identify and group duplicates.

### Function Signature

```python
import numpy as np
from typing import List, Tuple

def deduplicate_documents(
    doc_ids: List[str],
    embeddings: np.ndarray,
    similarity_threshold: float = 0.95
) -> List[List[str]]:
    """
    Group duplicate documents based on embedding similarity.

    Args:
        doc_ids: List of document IDs
        embeddings: 2D numpy array of shape (n_docs, embedding_dim)
        similarity_threshold: Cosine similarity threshold (0-1)

    Returns:
        List of lists, where each inner list contains IDs of duplicate docs.
        Each document appears in exactly one group.
        Groups are sorted by size (largest first).

    Example:
        doc_ids = ['d1', 'd2', 'd3', 'd4']
        # d1 and d3 are similar, d2 and d4 are similar
        result = [['d1', 'd3'], ['d2', 'd4']]
    """
    pass
```

### Requirements

1. Use cosine similarity to compare embeddings
2. Two documents are duplicates if similarity >= threshold
3. Handle transitive duplicates (if A~B and B~C, then A~B~C are all in same group)
4. Efficient for large datasets (10K+ documents)
5. Return groups sorted by size (largest first)

### Example

```python
doc_ids = ['doc1', 'doc2', 'doc3', 'doc4', 'doc5']
embeddings = np.array([
    [1.0, 0.0, 0.0],  # doc1
    [0.98, 0.1, 0.0], # doc2 (similar to doc1)
    [0.0, 1.0, 0.0],  # doc3
    [0.0, 0.98, 0.1], # doc4 (similar to doc3)
    [0.0, 0.0, 1.0],  # doc5
])

result = deduplicate_documents(doc_ids, embeddings, threshold=0.90)
# Expected: [['doc1', 'doc2'], ['doc3', 'doc4'], ['doc5']]
```

### Constraints

- 1 ≤ n_docs ≤ 100,000
- embedding_dim = 768 (typical for BERT models)
- 0.7 ≤ similarity_threshold ≤ 1.0
- Time limit: 10 seconds for 10,000 documents

### Hints

- Cosine similarity: `dot(a, b) / (norm(a) * norm(b))`
- Consider using scipy or numpy for efficient computation
- Think about data structures for transitive closure

---

## Problem 3.3: LLM Response Validator (12 points)

**Difficulty**: Hard
**Time**: 30 minutes

### Problem Statement

Implement a validator for LLM-generated legal responses that checks for:
1. **Citation validity**: All citations match retrieved documents
2. **Factual grounding**: All claims are supported by retrieved documents
3. **Hallucination detection**: Identify unsupported statements

### Function Signature

```python
from typing import List, Dict

def validate_llm_response(
    response: str,
    retrieved_docs: List[Dict[str, str]],
    strict_mode: bool = True
) -> Dict:
    """
    Validate LLM response against retrieved documents.

    Args:
        response: The LLM-generated response (may contain [Doc1], [Doc2] citations)
        retrieved_docs: List of dicts with 'id' and 'content' keys
        strict_mode: If True, all statements must have citations

    Returns:
        Dictionary with:
        - 'valid': bool (True if validation passes)
        - 'errors': List[str] (list of validation errors)
        - 'warnings': List[str] (list of warnings)
        - 'citation_coverage': float (0-1, what % of response is cited)
        - 'invalid_citations': List[str] (citations that don't match docs)

    Example:
        response = "According to [Doc1], the contract term is 5 years. [Doc2] states..."
        retrieved_docs = [{'id': 'Doc1', 'content': '...term is 5 years...'}]

        result = validate_llm_response(response, retrieved_docs)
        # result['invalid_citations'] = ['Doc2']  # Doc2 not in retrieved_docs
    """
    pass
```

### Citation Format

Citations are in the format `[DocN]` where N is a document ID. Example:
```
"According to [Doc1], the statute of limitations is 3 years.
However, [Doc2] notes that extensions may apply."
```

### Validation Rules

1. **Invalid Citation**: Citation references a doc not in `retrieved_docs`
2. **Unsupported Claim**: A factual statement has no citation (in strict mode)
3. **Misattributed Citation**: Citation text doesn't match doc content (bonus)

### Example

```python
response = """
The contract term is 5 years according to [Doc1].
The penalty for early termination is $50,000 as stated in [Doc2].
Both parties agreed to arbitration [Doc3].
Additionally, the contract can be renewed.
"""

retrieved_docs = [
    {'id': 'Doc1', 'content': 'The term of this agreement shall be five (5) years.'},
    {'id': 'Doc2', 'content': 'Early termination penalty: $50,000.'},
]

result = validate_llm_response(response, retrieved_docs, strict_mode=True)

print(result)
# {
#   'valid': False,
#   'errors': ['Invalid citation: [Doc3] not in retrieved documents',
#              'Unsupported claim: "the contract can be renewed" has no citation'],
#   'warnings': [],
#   'citation_coverage': 0.75,
#   'invalid_citations': ['Doc3']
# }
```

### Constraints

- Response length: 100-5,000 characters
- Number of retrieved docs: 1-20
- Citation format is always `[DocN]` where N matches a doc ID
- Time limit: 2 seconds

### Bonus (2 extra points)

Implement semantic matching to verify citations actually support the claims (use simple keyword matching as proxy).

---

## Problem 3.4: RAG Cache Optimizer (10 points)

**Difficulty**: Hard
**Time**: 25 minutes

### Problem Statement

Implement an intelligent cache for RAG queries that:
1. Caches results based on semantic similarity (not exact matches)
2. Implements LRU eviction
3. Tracks cache hit rate and cost savings

### Class Signature

```python
import numpy as np
from typing import Optional, Dict, Any
from datetime import datetime

class SemanticRAGCache:
    """
    Cache for RAG queries with semantic similarity matching.
    """

    def __init__(
        self,
        max_size: int = 1000,
        similarity_threshold: float = 0.90,
        embedding_dim: int = 768
    ):
        """
        Initialize cache.

        Args:
            max_size: Maximum number of cached items
            similarity_threshold: Similarity threshold for cache hits
            embedding_dim: Dimension of query embeddings
        """
        pass

    def get(
        self,
        query: str,
        query_embedding: np.ndarray
    ) -> Optional[Dict[str, Any]]:
        """
        Get cached result if similar query exists.

        Args:
            query: Query text
            query_embedding: Query embedding vector (shape: embedding_dim)

        Returns:
            Cached result dict with 'response' and 'retrieved_docs' keys,
            or None if no cache hit.
        """
        pass

    def put(
        self,
        query: str,
        query_embedding: np.ndarray,
        result: Dict[str, Any]
    ):
        """
        Add result to cache.

        Args:
            query: Query text
            query_embedding: Query embedding vector
            result: Dict with 'response' and 'retrieved_docs' keys
        """
        pass

    def get_stats(self) -> Dict[str, Any]:
        """
        Get cache statistics.

        Returns:
            Dict with:
            - 'size': Current cache size
            - 'hits': Number of cache hits
            - 'misses': Number of cache misses
            - 'hit_rate': Cache hit rate (0-1)
            - 'evictions': Number of items evicted
        """
        pass
```

### Requirements

1. Cache stores query embeddings and results
2. On `get()`, find most similar cached query
3. If similarity >= threshold, return cached result (cache hit)
4. Implement LRU: evict least recently used item when cache is full
5. Track access times for LRU
6. Update cache statistics

### Example

```python
cache = SemanticRAGCache(max_size=3, similarity_threshold=0.90)

# Query 1
q1 = "What is the statute of limitations?"
emb1 = np.random.rand(768)
result1 = {'response': 'It is 3 years', 'retrieved_docs': ['doc1']}
cache.put(q1, emb1, result1)

# Query 2 (similar to q1)
q2 = "What is the statute of limitations for this case?"
emb2 = emb1 + 0.05  # Very similar embedding
cached = cache.get(q2, emb2)  # Should be cache hit if similar enough

print(cache.get_stats())
# {'size': 1, 'hits': 1, 'misses': 0, 'hit_rate': 1.0, 'evictions': 0}
```

### Constraints

- max_size: 10-10,000
- similarity_threshold: 0.7-1.0
- embedding_dim: 768
- get() and put() should be O(n) where n is cache size
- Bonus: Optimize to O(log n) or better using approximate nearest neighbor

### Test Cases

Your solution will be tested for:
1. Correct cache hits for similar queries
2. LRU eviction working correctly
3. Accurate statistics tracking
4. Performance with 1000+ cached items

---

# Section 4: System Design (30 points)

**Time**: 45 minutes

---

## Problem 4.1: Design RAG System for Westlaw (15 points)

### Problem Statement

Design a production RAG system for Westlaw that allows users to ask natural language questions about legal cases and statutes.

### Requirements

**Functional:**
- Handle 10,000 concurrent users
- Search across 100M legal documents
- Response time: <2s (p95)
- Support complex queries with multiple sub-questions
- Provide accurate citations for all claims

**Non-Functional:**
- 99.95% availability
- GDPR compliant (don't store user queries)
- Audit trail for all AI responses
- Cost-effective (optimize for $/query)

### Your Design Should Cover

1. **High-Level Architecture** (5 points)
   - Draw/describe system components
   - Data flow from user query to response
   - Integration with existing Westlaw infrastructure

2. **Key Design Decisions** (5 points)
   - Embedding model choice and rationale
   - Vector database selection
   - LLM selection (which model(s), why)
   - Caching strategy
   - Monitoring and observability

3. **Scaling & Performance** (3 points)
   - How do you handle 10K concurrent users?
   - How do you achieve <2s latency?
   - How do you optimize costs?

4. **Reliability & Compliance** (2 points)
   - How do you achieve 99.95% uptime?
   - How do you handle GDPR requirements?
   - How do you maintain audit trails?

### Your Answer

**Architecture Diagram** (draw in text or describe clearly):
```
[Your diagram/description here]
```

**Component Choices:**

| Component | Choice | Rationale |
|-----------|--------|-----------|
| Embedding Model | | |
| Vector DB | | |
| LLM | | |
| Orchestration | | |
| Monitoring | | |

**Scaling Strategy:**
_______________

**Compliance Approach:**
_______________

**Cost Estimate:**
- Per query cost: _______________
- Monthly cost at 10M queries: _______________

---

## Problem 4.2: ML Model Deployment Pipeline (15 points)

### Problem Statement

Design an MLOps pipeline for deploying and monitoring a legal document classification model that categorizes documents into 500+ categories.

### Requirements

**Functional:**
- Automated training pipeline (weekly retraining on new data)
- A/B testing framework (test new models before full rollout)
- Automated quality gates (don't deploy if metrics regress)
- Rollback capability
- Model versioning

**Non-Functional:**
- Zero-downtime deployments
- Monitor for data drift and model degradation
- Cost visibility and optimization
- Audit trail for compliance

### Your Design Should Cover

1. **Pipeline Architecture** (5 points)
   - Training pipeline components
   - Deployment workflow
   - A/B testing mechanism
   - Rollback process

2. **Quality Gates** (4 points)
   - What metrics do you track?
   - What thresholds trigger alerts?
   - How do you prevent bad models from reaching production?
   - How do you handle edge cases?

3. **Monitoring & Operations** (4 points)
   - What do you monitor in production?
   - How do you detect data drift?
   - How do you handle model degradation?
   - What dashboards do you create?

4. **Cost Management** (2 points)
   - How do you track costs?
   - How do you optimize inference costs?
   - How do you forecast costs?

### Your Answer

**Pipeline Diagram:**
```
[Your diagram/description here]
```

**Technology Stack:**

| Component | Technology | Rationale |
|-----------|------------|-----------|
| Training | | |
| Model Registry | | |
| Deployment | | |
| A/B Testing | | |
| Monitoring | | |

**Quality Gates:**
1. _______________
2. _______________
3. _______________

**Monitoring Metrics:**
- Model Performance: _______________
- Data Quality: _______________
- System Health: _______________
- Business Impact: _______________

**Rollback Strategy:**
_______________

---

# Submission Instructions

## How to Submit

1. Save all your answers in a single file: `submission.md` or `submission.py`
2. For coding problems, include all function implementations
3. For system design, provide detailed written answers
4. Include any assumptions you made

## Evaluation Criteria

**Coding Problems:**
- Correctness (60%): Does it pass test cases?
- Code Quality (20%): Is it clean, readable, well-structured?
- Efficiency (20%): Is it performant for large inputs?

**System Design:**
- Completeness (40%): Did you address all requirements?
- Design Quality (30%): Are choices well-justified?
- Scalability (20%): Can it handle production scale?
- Trade-offs (10%): Did you discuss pros/cons?

**SQL:**
- Correctness (70%): Does query produce correct results?
- Efficiency (30%): Is query optimized?

---

# Tips for Success

1. **Read Carefully**: Understand requirements before coding
2. **Start Simple**: Get basic solution working, then optimize
3. **Test Your Code**: Run through examples mentally
4. **Comment**: Explain your approach for partial credit
5. **Time Management**: Don't spend too long on any one problem
6. **Trade-offs**: In system design, explain why you chose A over B

---

# Resources Available

During the test, you can use:
- Python documentation
- Pandas/Numpy documentation
- SQL reference
- Calculator

You CANNOT use:
- AI assistants (ChatGPT, Copilot, etc.)
- StackOverflow or external code
- Communication with others

---

# Good Luck!

Remember: Thomson Reuters values clear thinking, practical solutions, and the ability to balance trade-offs. Show your thought process, not just final answers.
