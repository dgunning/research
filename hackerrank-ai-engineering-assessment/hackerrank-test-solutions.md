# Thomson Reuters - Principal AI Engineer Assessment
# ANSWER KEY & SOLUTIONS

**For Evaluators Only**

---

# Section 1: Multiple Choice - Answers

| Question | Answer | Explanation |
|----------|--------|-------------|
| 1.1 | **C** | Mapping between chunks and source metadata is critical for accurate citations. Without proper tracking, you can't reliably cite where information came from. |
| 1.2 | **B** | HNSW provides excellent balance of speed (~99% accuracy) and recall for large-scale vector search. Used by major vector DBs. |
| 1.3 | **C** | Need re-ranking to select most relevant chunks. 10K tokens of context + generation leaves room in 32K window. |
| 1.4 | **D** | For production legal AI, need all components: role, structure, reasoning. Combines best practices. |
| 1.5 | **C** | Latency is system metric, not quality metric. Doesn't indicate model drift. Other options all signal quality changes. |
| 1.6 | **C** | Domain-specific models outperform general models for specialized text. Legal language is distinct. |
| 1.7 | **C** | Always profile first! Don't optimize blindly. Bottleneck could be retrieval, LLM, network, etc. |
| 1.8 | **C** | For legal AI, accuracy/correctness is paramount. Wrong legal advice has serious consequences. |
| 1.9 | **B** | Hybrid search combines best of both: semantic for concepts, keyword for exact matches. Standard solution. |
| 1.10 | **B** | Fine-tuning teaches new reasoning patterns/style. RAG better for knowledge/facts. |
| 1.11 | **C** | Model routing (80/20 rule) typically saves most. Use cheap models when sufficient. |
| 1.12 | **B** | GDPR requires right to deletion. If training data deleted, may need model retraining. Complex compliance requirement. |
| 1.13 | **A** | Attention computes relevance scores between query and key vectors to determine what to focus on. |
| 1.14 | **B** | Must outperform current prod on holdout. Absolute metrics can be misleading. |
| 1.15 | **A** | 99.95% = 0.05% downtime = 0.0005 × 365 × 24 = 4.38 hours/year |

**Score**: 15 points total (1 per correct answer)

---

# Section 2: SQL & Data Analysis - Solutions

## Question 2.1: Query Performance Analysis (5 points)

### Part a) Why is the query slow? (2 points)

**Answer:**

The query is slow because:

1. **Missing index on `jurisdiction`**: The WHERE clause filters on jurisdiction first, but there's no index. This causes a full table scan of 100M rows.

2. **Missing index on `document_type`**: Second filter has no index support.

3. **Compound filter inefficiency**: Even with the date index, the database must scan all dates >= 2020 and then filter by jurisdiction and type.

4. **Index on date alone is suboptimal**: The index doesn't help with the two primary filters.

**Scoring:**
- 2 points: Identifies missing indexes and explains scan issue
- 1 point: Mentions missing indexes only
- 0 points: Incorrect or no answer

### Part b) What index would you create? (3 points)

**Answer:**

```sql
-- Composite index covering all WHERE clause columns
CREATE INDEX idx_jurisdiction_type_date
ON legal_documents(jurisdiction, document_type, date_filed DESC);
```

**Alternative (also acceptable):**

```sql
-- Separate indexes (less optimal but helps)
CREATE INDEX idx_jurisdiction ON legal_documents(jurisdiction);
CREATE INDEX idx_doc_type ON legal_documents(document_type);
-- Keep existing date index
```

**Why the composite index is better:**
- Covers all WHERE clause columns in order of selectivity
- Date in descending order helps with ORDER BY
- Allows index-only scan for the SELECT columns if we add INCLUDE
- Single index is more efficient than multiple

**Bonus (if mentioned):**
```sql
-- Covering index (best solution)
CREATE INDEX idx_jurisdiction_type_date_covering
ON legal_documents(jurisdiction, document_type, date_filed DESC)
INCLUDE (doc_id, document_type);  -- PostgreSQL syntax
```

**Scoring:**
- 3 points: Composite index with correct column order
- 2 points: Multiple separate indexes
- 1 point: Partial solution or single index
- 0 points: Incorrect

---

## Question 2.2: ML Model Performance Analysis (5 points)

**Solution:**

```sql
SELECT
    model_version,
    COUNT(*) AS total_predictions,
    ROUND(AVG(confidence), 3) AS avg_confidence,
    ROUND(
        COUNT(CASE WHEN predicted_class = actual_class THEN 1 END) * 100.0 /
        NULLIF(COUNT(actual_class), 0),
        2
    ) AS accuracy_percent,
    PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY processing_time_ms) AS p95_processing_time_ms
FROM model_predictions
WHERE actual_class IS NOT NULL OR 1=1  -- Include all for counts
GROUP BY model_version
ORDER BY model_version;
```

**Key Points:**

1. **Total predictions**: Simple COUNT(*)
2. **Average confidence**: AVG(confidence)
3. **Accuracy**: Count matches / count labeled (handle NULLs)
4. **95th percentile**: Use PERCENTILE_CONT (PostgreSQL) or PERCENTILE_DISC

**Alternate accuracy calculation:**
```sql
-- Also acceptable
ROUND(
    SUM(CASE WHEN predicted_class = actual_class THEN 1 ELSE 0 END) * 100.0 /
    COUNT(actual_class),
    2
) AS accuracy_percent
```

**Scoring:**
- 5 points: All four metrics correct, handles NULLs properly
- 4 points: Minor issues with NULL handling or percentile
- 3 points: Missing one metric or significant error
- 2 points: Two metrics correct
- 1 point: Basic attempt
- 0 points: No answer or completely incorrect

---

## Question 2.3: Document Retrieval Analytics (5 points)

**Solution:**

```sql
WITH first_clicks AS (
    -- Get the rank of the first clicked document for each query
    SELECT
        q.query_id,
        DATE(q.timestamp) AS query_date,
        MIN(rd.rank) AS first_click_rank
    FROM queries q
    JOIN user_clicks uc ON q.query_id = uc.query_id
    JOIN retrieved_documents rd ON uc.query_id = rd.query_id
        AND uc.doc_id = rd.doc_id
    WHERE q.timestamp >= CURRENT_DATE - INTERVAL '30 days'
    GROUP BY q.query_id, DATE(q.timestamp)
),
daily_mrr AS (
    SELECT
        query_date,
        AVG(1.0 / first_click_rank) AS mrr
    FROM first_clicks
    GROUP BY query_date
)
SELECT
    query_date,
    ROUND(mrr, 4) AS mean_reciprocal_rank
FROM daily_mrr
ORDER BY query_date;
```

**Key Logic:**

1. **First CTE**: Find the rank of the first clicked document per query
2. **Join**: Link queries → clicks → retrieved docs to get rank
3. **Calculate**: 1/rank for each query, then average by day
4. **Filter**: Last 30 days

**Alternative approach (also acceptable):**

```sql
SELECT
    DATE(q.timestamp) AS query_date,
    ROUND(
        AVG(1.0 / MIN(rd.rank)),
        4
    ) AS mean_reciprocal_rank
FROM queries q
JOIN user_clicks uc ON q.query_id = uc.query_id
JOIN retrieved_documents rd ON uc.query_id = rd.query_id
    AND uc.doc_id = rd.doc_id
WHERE q.timestamp >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY DATE(q.timestamp), q.query_id
ORDER BY query_date;
```

Wait, this is incorrect - need to fix:

```sql
SELECT
    DATE(q.timestamp) AS query_date,
    ROUND(
        AVG(1.0 / min_rank),
        4
    ) AS mean_reciprocal_rank
FROM (
    SELECT
        q.query_id,
        q.timestamp,
        MIN(rd.rank) AS min_rank
    FROM queries q
    JOIN user_clicks uc ON q.query_id = uc.query_id
    JOIN retrieved_documents rd ON uc.query_id = rd.query_id
        AND uc.doc_id = rd.doc_id
    WHERE q.timestamp >= CURRENT_DATE - INTERVAL '30 days'
    GROUP BY q.query_id, q.timestamp
) subq
GROUP BY DATE(subq.timestamp)
ORDER BY query_date;
```

**Scoring:**
- 5 points: Correct MRR calculation, proper joins, handles edge cases
- 4 points: Correct logic with minor syntax issues
- 3 points: Correct approach but implementation errors
- 2 points: Understands MRR but query has significant issues
- 1 point: Basic attempt
- 0 points: Incorrect

**Edge Cases to Handle:**
- Queries with no clicks (exclude from MRR)
- Multiple clicks per query (use first click)
- Documents clicked but not in retrieved set (shouldn't happen with proper joins)

---

# Section 3: Coding Problems - Solutions

## Problem 3.1: Document Chunking (8 points)

### Solution

```python
import re
from typing import List, Dict

def chunk_legal_document(
    document: str,
    target_size: int = 500,
    max_size: int = 1000
) -> List[Dict]:
    """
    Chunk a legal document intelligently.
    """

    # Simple token count: 1 token ≈ 0.75 words
    def count_tokens(text: str) -> int:
        words = len(text.split())
        return int(words * 0.75)

    # Detect section headers (1., 1.1, 1.1.1, etc.)
    section_pattern = re.compile(r'^\d+(\.\d+)*\.?\s+[A-Z]')

    # Split into lines
    lines = document.split('\n')

    chunks = []
    current_chunk = []
    current_section = None
    current_tokens = 0
    start_pos = 0
    char_pos = 0

    for line in lines:
        line_tokens = count_tokens(line)

        # Check if this is a section header
        is_section = section_pattern.match(line.strip())

        if is_section:
            # Save previous chunk if it exists
            if current_chunk:
                chunk_text = '\n'.join(current_chunk)
                chunks.append({
                    'text': chunk_text,
                    'section': current_section,
                    'start_pos': start_pos,
                    'end_pos': char_pos
                })

            # Start new chunk with this section
            current_section = line.strip()
            current_chunk = [line]
            current_tokens = line_tokens
            start_pos = char_pos

        else:
            # Add line to current chunk
            current_chunk.append(line)
            current_tokens += line_tokens

            # Check if we should split
            if current_tokens >= target_size:
                # If over max_size, must split
                if current_tokens >= max_size:
                    chunk_text = '\n'.join(current_chunk)
                    chunks.append({
                        'text': chunk_text,
                        'section': current_section,
                        'start_pos': start_pos,
                        'end_pos': char_pos + len(line)
                    })

                    # Start new chunk, include section header if we have one
                    if current_section:
                        current_chunk = [current_section]
                        current_tokens = count_tokens(current_section)
                    else:
                        current_chunk = []
                        current_tokens = 0
                    start_pos = char_pos + len(line) + 1

        char_pos += len(line) + 1  # +1 for newline

    # Add final chunk
    if current_chunk:
        chunk_text = '\n'.join(current_chunk)
        chunks.append({
            'text': chunk_text,
            'section': current_section,
            'start_pos': start_pos,
            'end_pos': char_pos
        })

    return chunks


# Test
if __name__ == "__main__":
    document = """
1. Parties
This Agreement is between Company A and Company B.

1.1 Company A
Company A is a Delaware corporation with principal place of business in San Francisco.

1.2 Company B
Company B is a California corporation with principal place of business in Los Angeles.

2. Terms
The term of this agreement shall be five years from the effective date.
"""

    chunks = chunk_legal_document(document, target_size=50, max_size=100)

    for i, chunk in enumerate(chunks):
        print(f"\n--- Chunk {i+1} ---")
        print(f"Section: {chunk['section']}")
        print(f"Tokens: ~{len(chunk['text'].split()) * 0.75:.0f}")
        print(f"Text preview: {chunk['text'][:100]}...")
```

### Scoring Rubric (8 points)

**Correctness (5 points):**
- 2 points: Correctly identifies section headers
- 1 point: Respects target_size and max_size
- 1 point: Includes section headers in child chunks
- 1 point: Returns correct dictionary structure

**Code Quality (2 points):**
- 1 point: Clean, readable code
- 1 point: Proper error handling or edge cases

**Efficiency (1 point):**
- 1 point: O(n) time complexity where n is document length

### Common Mistakes

- Not handling documents without clear sections
- Not including section header in continuation chunks
- Token counting errors
- Not handling empty lines properly

---

## Problem 3.2: Semantic Deduplication (10 points)

### Solution

```python
import numpy as np
from typing import List, Tuple
from collections import defaultdict

def deduplicate_documents(
    doc_ids: List[str],
    embeddings: np.ndarray,
    similarity_threshold: float = 0.95
) -> List[List[str]]:
    """
    Group duplicate documents based on embedding similarity.
    """

    # Normalize embeddings for cosine similarity
    norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
    normalized_embeddings = embeddings / (norms + 1e-10)

    # Compute similarity matrix
    similarity_matrix = np.dot(normalized_embeddings, normalized_embeddings.T)

    # Find groups using Union-Find (Disjoint Set Union)
    parent = list(range(len(doc_ids)))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py

    # Union documents above threshold
    n = len(doc_ids)
    for i in range(n):
        for j in range(i + 1, n):
            if similarity_matrix[i, j] >= similarity_threshold:
                union(i, j)

    # Group documents by root parent
    groups = defaultdict(list)
    for i, doc_id in enumerate(doc_ids):
        root = find(i)
        groups[root].append(doc_id)

    # Convert to list and sort by size (largest first)
    result = sorted(groups.values(), key=len, reverse=True)

    return result


# Test
if __name__ == "__main__":
    doc_ids = ['doc1', 'doc2', 'doc3', 'doc4', 'doc5']
    embeddings = np.array([
        [1.0, 0.0, 0.0],  # doc1
        [0.98, 0.1, 0.0], # doc2 (similar to doc1)
        [0.0, 1.0, 0.0],  # doc3
        [0.0, 0.98, 0.1], # doc4 (similar to doc3)
        [0.0, 0.0, 1.0],  # doc5
    ])

    result = deduplicate_documents(doc_ids, embeddings, threshold=0.90)
    print(result)
    # Expected: [['doc1', 'doc2'], ['doc3', 'doc4'], ['doc5']]
```

### Alternative Solution (Clustering-based)

```python
from sklearn.cluster import AgglomerativeClustering

def deduplicate_documents_clustering(
    doc_ids: List[str],
    embeddings: np.ndarray,
    similarity_threshold: float = 0.95
) -> List[List[str]]:
    """
    Using hierarchical clustering for deduplication.
    """

    # Convert similarity threshold to distance threshold
    # cosine_distance = 1 - cosine_similarity
    distance_threshold = 1 - similarity_threshold

    # Agglomerative clustering
    clustering = AgglomerativeClustering(
        n_clusters=None,
        distance_threshold=distance_threshold,
        metric='cosine',
        linkage='average'
    )

    labels = clustering.fit_predict(embeddings)

    # Group by cluster label
    groups = defaultdict(list)
    for doc_id, label in zip(doc_ids, labels):
        groups[label].append(doc_id)

    # Sort by size
    result = sorted(groups.values(), key=len, reverse=True)

    return result
```

### Scoring Rubric (10 points)

**Correctness (6 points):**
- 2 points: Correct cosine similarity calculation
- 2 points: Handles transitive duplicates (Union-Find or equivalent)
- 1 point: Returns groups sorted by size
- 1 point: Each document appears in exactly one group

**Code Quality (2 points):**
- 1 point: Clean, well-structured code
- 1 point: Proper use of data structures

**Efficiency (2 points):**
- 1 point: O(n²) or better for similarity computation
- 1 point: Efficient grouping algorithm

### Performance Optimization

For very large datasets (100K+), use approximate methods:

```python
from sklearn.neighbors import NearestNeighbors

def deduplicate_documents_fast(
    doc_ids: List[str],
    embeddings: np.ndarray,
    similarity_threshold: float = 0.95,
    n_neighbors: int = 50
) -> List[List[str]]:
    """
    Fast deduplication using approximate nearest neighbors.
    """

    # Find approximate neighbors
    nbrs = NearestNeighbors(
        n_neighbors=min(n_neighbors, len(doc_ids)),
        metric='cosine',
        algorithm='brute'  # or 'ball_tree' for larger datasets
    )
    nbrs.fit(embeddings)

    distances, indices = nbrs.kneighbors(embeddings)

    # Union-Find as before, but only check nearest neighbors
    parent = list(range(len(doc_ids)))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py

    # Only check nearest neighbors
    for i in range(len(doc_ids)):
        for j, dist in zip(indices[i], distances[i]):
            if i != j and (1 - dist) >= similarity_threshold:
                union(i, j)

    # Group and return
    groups = defaultdict(list)
    for i, doc_id in enumerate(doc_ids):
        root = find(i)
        groups[root].append(doc_id)

    return sorted(groups.values(), key=len, reverse=True)
```

---

## Problem 3.3: LLM Response Validator (12 points)

### Solution

```python
import re
from typing import List, Dict

def validate_llm_response(
    response: str,
    retrieved_docs: List[Dict[str, str]],
    strict_mode: bool = True
) -> Dict:
    """
    Validate LLM response against retrieved documents.
    """

    # Extract all citations from response
    citation_pattern = r'\[Doc(\d+|[A-Za-z0-9_-]+)\]'
    citations_in_response = re.findall(citation_pattern, response)

    # Create set of valid doc IDs
    valid_doc_ids = {doc['id'] for doc in retrieved_docs}

    # Create dict for easy lookup
    docs_by_id = {doc['id']: doc['content'] for doc in retrieved_docs}

    errors = []
    warnings = []
    invalid_citations = []

    # Check 1: Invalid citations
    for citation in set(citations_in_response):
        if citation not in valid_doc_ids:
            invalid_citations.append(citation)
            errors.append(f"Invalid citation: [Doc{citation}] not in retrieved documents")

    # Check 2: Citation coverage
    # Split response into sentences
    sentences = re.split(r'[.!?]+', response)
    sentences = [s.strip() for s in sentences if s.strip()]

    cited_sentences = 0
    uncited_factual_sentences = []

    for sentence in sentences:
        # Check if sentence has citation
        has_citation = bool(re.search(citation_pattern, sentence))

        # Simple heuristic: sentence with specific claims should have citations
        # Look for patterns like "according to", "states that", contains numbers, etc.
        is_factual = any([
            re.search(r'\d+', sentence),  # Contains numbers
            re.search(r'\b(is|are|was|were|shall|will)\b', sentence.lower()),
            len(sentence.split()) > 10  # Substantial claim
        ])

        if has_citation:
            cited_sentences += 1
        elif is_factual and strict_mode:
            uncited_factual_sentences.append(sentence)

    # Calculate citation coverage
    if sentences:
        citation_coverage = cited_sentences / len(sentences)
    else:
        citation_coverage = 0.0

    # Check 3: Unsupported claims (in strict mode)
    if strict_mode:
        for sentence in uncited_factual_sentences:
            errors.append(f'Unsupported claim: "{sentence[:100]}" has no citation')

    # Check 4: BONUS - Verify citations actually support claims
    # This is a simplified version using keyword matching
    for sentence in sentences:
        # Find citations in this sentence
        sentence_citations = re.findall(citation_pattern, sentence)

        if sentence_citations:
            # Remove citations to get the claim
            claim = re.sub(citation_pattern, '', sentence).strip()

            # Check if claim keywords appear in cited documents
            claim_keywords = set(claim.lower().split())
            claim_keywords = {w for w in claim_keywords if len(w) > 4}  # Filter short words

            supported = False
            for citation in sentence_citations:
                if citation in docs_by_id:
                    doc_content = docs_by_id[citation].lower()
                    # Check if significant keywords appear in doc
                    matches = sum(1 for kw in claim_keywords if kw in doc_content)
                    if matches >= len(claim_keywords) * 0.3:  # 30% keyword overlap
                        supported = True
                        break

            if not supported and claim_keywords:
                warnings.append(
                    f'Potentially unsupported: "{claim[:80]}" may not be supported by cited docs'
                )

    # Determine overall validity
    valid = len(errors) == 0

    return {
        'valid': valid,
        'errors': errors,
        'warnings': warnings,
        'citation_coverage': round(citation_coverage, 2),
        'invalid_citations': invalid_citations
    }


# Test
if __name__ == "__main__":
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

    print("Valid:", result['valid'])
    print("\nErrors:")
    for error in result['errors']:
        print(f"  - {error}")
    print("\nWarnings:")
    for warning in result['warnings']:
        print(f"  - {warning}")
    print(f"\nCitation coverage: {result['citation_coverage']}")
    print(f"Invalid citations: {result['invalid_citations']}")
```

### Scoring Rubric (12 points)

**Correctness (8 points):**
- 2 points: Correctly identifies invalid citations
- 2 points: Calculates citation coverage accurately
- 2 points: Detects unsupported claims in strict mode
- 2 points: Returns proper dictionary structure

**Bonus (2 points):**
- 2 points: Implements semantic matching to verify citations support claims

**Code Quality (2 points):**
- 1 point: Clean, readable code
- 1 point: Good use of regex and data structures

### Test Cases

```python
# Test Case 1: All valid
response1 = "According to [Doc1], the term is 5 years."
docs1 = [{'id': 'Doc1', 'content': 'Term: 5 years'}]
# Expected: valid=True, coverage=1.0

# Test Case 2: Invalid citation
response2 = "According to [Doc99], the term is 5 years."
docs2 = [{'id': 'Doc1', 'content': 'Term: 5 years'}]
# Expected: valid=False, invalid_citations=['Doc99']

# Test Case 3: Missing citation (strict mode)
response3 = "The term is 5 years. The fee is $100."
docs3 = [{'id': 'Doc1', 'content': 'Term: 5 years'}]
# Expected: valid=False, errors about unsupported claims
```

---

## Problem 3.4: RAG Cache Optimizer (10 points)

### Solution

```python
import numpy as np
from typing import Optional, Dict, Any, Tuple
from datetime import datetime
from collections import OrderedDict

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
        self.max_size = max_size
        self.similarity_threshold = similarity_threshold
        self.embedding_dim = embedding_dim

        # Cache storage: OrderedDict for LRU
        # Key: cache_id, Value: (query, embedding, result, timestamp)
        self.cache = OrderedDict()

        # Statistics
        self.hits = 0
        self.misses = 0
        self.evictions = 0

        # Counter for cache IDs
        self.next_id = 0

    def _cosine_similarity(self, a: np.ndarray, b: np.ndarray) -> float:
        """Compute cosine similarity between two vectors."""
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-10)

    def _find_similar_query(
        self,
        query_embedding: np.ndarray
    ) -> Optional[Tuple[str, Dict[str, Any]]]:
        """
        Find most similar cached query above threshold.
        Returns (cache_id, cached_result) or None.
        """
        best_similarity = -1
        best_cache_id = None
        best_result = None

        for cache_id, (query, embedding, result, timestamp) in self.cache.items():
            similarity = self._cosine_similarity(query_embedding, embedding)

            if similarity >= self.similarity_threshold and similarity > best_similarity:
                best_similarity = similarity
                best_cache_id = cache_id
                best_result = result

        return (best_cache_id, best_result) if best_cache_id else None

    def get(
        self,
        query: str,
        query_embedding: np.ndarray
    ) -> Optional[Dict[str, Any]]:
        """
        Get cached result if similar query exists.
        """
        # Find similar query
        similar = self._find_similar_query(query_embedding)

        if similar:
            cache_id, result = similar

            # Update access time (LRU)
            self.cache.move_to_end(cache_id)

            # Update statistics
            self.hits += 1

            return result
        else:
            # Cache miss
            self.misses += 1
            return None

    def put(
        self,
        query: str,
        query_embedding: np.ndarray,
        result: Dict[str, Any]
    ):
        """
        Add result to cache.
        """
        # Check if cache is full
        if len(self.cache) >= self.max_size:
            # Evict least recently used (first item in OrderedDict)
            self.cache.popitem(last=False)
            self.evictions += 1

        # Add to cache
        cache_id = f"cache_{self.next_id}"
        self.next_id += 1

        self.cache[cache_id] = (
            query,
            query_embedding.copy(),
            result,
            datetime.now()
        )

    def get_stats(self) -> Dict[str, Any]:
        """
        Get cache statistics.
        """
        total_requests = self.hits + self.misses
        hit_rate = self.hits / total_requests if total_requests > 0 else 0.0

        return {
            'size': len(self.cache),
            'hits': self.hits,
            'misses': self.misses,
            'hit_rate': round(hit_rate, 3),
            'evictions': self.evictions
        }

    def clear(self):
        """Clear cache and reset statistics."""
        self.cache.clear()
        self.hits = 0
        self.misses = 0
        self.evictions = 0


# Test
if __name__ == "__main__":
    cache = SemanticRAGCache(max_size=3, similarity_threshold=0.90)

    # Query 1
    q1 = "What is the statute of limitations?"
    emb1 = np.random.rand(768)
    emb1 = emb1 / np.linalg.norm(emb1)  # Normalize
    result1 = {'response': 'It is 3 years', 'retrieved_docs': ['doc1']}
    cache.put(q1, emb1, result1)

    # Query 2 (similar to q1)
    q2 = "What is the statute of limitations for this case?"
    emb2 = emb1 + np.random.rand(768) * 0.05
    emb2 = emb2 / np.linalg.norm(emb2)  # Normalize

    cached = cache.get(q2, emb2)  # Should be cache hit
    print("Cache hit:", cached is not None)

    # Query 3 (different)
    q3 = "How to file a patent?"
    emb3 = np.random.rand(768)
    emb3 = emb3 / np.linalg.norm(emb3)
    result3 = {'response': 'File with USPTO', 'retrieved_docs': ['doc2']}

    cached = cache.get(q3, emb3)  # Should be cache miss
    print("Cache miss:", cached is None)
    cache.put(q3, emb3, result3)

    print("\nCache stats:", cache.get_stats())

    # Test LRU eviction
    for i in range(5):
        q = f"Query {i}"
        emb = np.random.rand(768)
        emb = emb / np.linalg.norm(emb)
        result = {'response': f'Answer {i}', 'retrieved_docs': [f'doc{i}']}
        cache.put(q, emb, result)

    print("\nCache stats after evictions:", cache.get_stats())
    print(f"Cache size: {cache.get_stats()['size']}")  # Should be max_size
```

### Optimized Solution (for larger caches)

```python
from sklearn.neighbors import NearestNeighbors

class FastSemanticRAGCache:
    """
    Optimized cache using approximate nearest neighbors.
    """

    def __init__(
        self,
        max_size: int = 1000,
        similarity_threshold: float = 0.90,
        embedding_dim: int = 768
    ):
        self.max_size = max_size
        self.similarity_threshold = similarity_threshold
        self.embedding_dim = embedding_dim

        # Store embeddings as numpy array for fast similarity search
        self.embeddings = []
        self.cache_data = OrderedDict()  # cache_id -> (query, result, timestamp)
        self.cache_ids = []  # Parallel to embeddings

        self.hits = 0
        self.misses = 0
        self.evictions = 0
        self.next_id = 0

        # Rebuild index periodically
        self.index = None
        self.index_dirty = True

    def _rebuild_index(self):
        """Rebuild NearestNeighbors index."""
        if len(self.embeddings) > 0:
            embeddings_array = np.array(self.embeddings)
            self.index = NearestNeighbors(
                n_neighbors=min(10, len(self.embeddings)),
                metric='cosine',
                algorithm='brute'
            )
            self.index.fit(embeddings_array)
            self.index_dirty = False

    def get(
        self,
        query: str,
        query_embedding: np.ndarray
    ) -> Optional[Dict[str, Any]]:
        """Get cached result using ANN search."""

        if len(self.embeddings) == 0:
            self.misses += 1
            return None

        # Rebuild index if needed
        if self.index_dirty:
            self._rebuild_index()

        # Find nearest neighbors
        distances, indices = self.index.kneighbors(
            query_embedding.reshape(1, -1),
            n_neighbors=min(5, len(self.embeddings))
        )

        # Check if any neighbor is above threshold
        for dist, idx in zip(distances[0], indices[0]):
            similarity = 1 - dist
            if similarity >= self.similarity_threshold:
                cache_id = self.cache_ids[idx]

                # Update LRU
                self.cache_data.move_to_end(cache_id)

                self.hits += 1
                return self.cache_data[cache_id][1]  # Return result

        self.misses += 1
        return None

    def put(
        self,
        query: str,
        query_embedding: np.ndarray,
        result: Dict[str, Any]
    ):
        """Add to cache."""

        # Evict if full
        if len(self.cache_data) >= self.max_size:
            # Remove LRU
            old_cache_id, _ = self.cache_data.popitem(last=False)

            # Remove from embeddings
            idx = self.cache_ids.index(old_cache_id)
            self.embeddings.pop(idx)
            self.cache_ids.pop(idx)

            self.evictions += 1
            self.index_dirty = True

        # Add new entry
        cache_id = f"cache_{self.next_id}"
        self.next_id += 1

        self.cache_data[cache_id] = (query, result, datetime.now())
        self.embeddings.append(query_embedding.copy())
        self.cache_ids.append(cache_id)

        self.index_dirty = True

    def get_stats(self) -> Dict[str, Any]:
        """Get statistics."""
        total = self.hits + self.misses
        hit_rate = self.hits / total if total > 0 else 0.0

        return {
            'size': len(self.cache_data),
            'hits': self.hits,
            'misses': self.misses,
            'hit_rate': round(hit_rate, 3),
            'evictions': self.evictions
        }
```

### Scoring Rubric (10 points)

**Correctness (6 points):**
- 2 points: Semantic similarity matching works correctly
- 2 points: LRU eviction implemented properly
- 1 point: Statistics tracked accurately
- 1 point: Handles edge cases (empty cache, threshold not met)

**Code Quality (2 points):**
- 1 point: Clean, well-structured code
- 1 point: Good use of data structures (OrderedDict)

**Efficiency (2 points):**
- 1 point: Reasonable time complexity for get/put
- 1 point: Bonus for optimizations (ANN, indexing)

### Test Cases

```python
# Test 1: Basic functionality
cache = SemanticRAGCache(max_size=2, similarity_threshold=0.95)
# Add item, retrieve similar query

# Test 2: LRU eviction
# Add 3 items to cache with max_size=2
# Verify oldest is evicted

# Test 3: Statistics tracking
# Perform hits and misses, verify stats are correct

# Test 4: Similarity threshold
# Query with similarity 0.90 vs 0.94 with threshold 0.95
# Verify threshold is respected
```

---

# Section 4: System Design - Solution Guidelines

## Problem 4.1: Design RAG System for Westlaw (15 points)

### High-Level Architecture (5 points)

```
┌─────────────────────────────────────────────────────────────────┐
│                         User Interface                          │
│                   (Westlaw Web/Mobile App)                      │
└────────────────────────────┬────────────────────────────────────┘
                             │
                ┌────────────┴────────────┐
                │    API Gateway (AWS)    │
                │  - Auth, Rate limiting  │
                └────────────┬────────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
┌───────▼───────┐   ┌───────▼────────┐  ┌────────▼───────┐
│ Query Service │   │ Embedding      │  │ Citation       │
│ (Lambda/ECS)  │   │ Service (SM)   │  │ Validator      │
└───────┬───────┘   └───────┬────────┘  └────────────────┘
        │                   │
        │     ┌─────────────┘
        │     │
┌───────▼─────▼────────────────────────────────────────────────┐
│              Retrieval Layer (OpenSearch)                    │
│  - Vector index (100M docs × 768 dims)                       │
│  - Hybrid search (semantic + keyword)                        │
│  - Multi-tenant filtering                                    │
└───────────────────────────┬──────────────────────────────────┘
                            │
        ┌───────────────────┴─────────────────────┐
        │                                         │
┌───────▼───────┐                      ┌──────────▼─────────┐
│ LLM Service   │                      │ Document Store     │
│ (Bedrock)     │                      │ (S3 + Metadata DB) │
│ - Claude 3.5  │                      │ - Original docs    │
│ - Streaming   │                      │ - Preprocessed     │
└───────┬───────┘                      └────────────────────┘
        │
┌───────▼───────────────────────────────────────────────────────┐
│                    Response Cache                              │
│              (ElastiCache - Semantic Cache)                    │
└────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────┐
│                   Monitoring & Observability                     │
│  - CloudWatch (metrics, logs)                                    │
│  - X-Ray (tracing)                                              │
│  - Custom quality metrics                                        │
└──────────────────────────────────────────────────────────────────┘
```

### Key Design Decisions (5 points)

| Component | Choice | Rationale |
|-----------|--------|-----------|
| **Embedding Model** | Sentence-Transformers (legal-bert-base) fine-tuned on legal corpus | Domain-specific gives better retrieval quality than general models. 768-dim balances quality and speed. |
| **Vector DB** | AWS OpenSearch with k-NN plugin | Native AWS integration, proven at scale, supports hybrid search, good cost/performance. Alternative: Pinecone for managed option. |
| **LLM** | Amazon Bedrock (Claude 3.5 Sonnet primary, Haiku for simple queries) | Multi-model strategy optimizes cost/quality. Claude strong for legal reasoning. Bedrock provides SLA and compliance. |
| **Orchestration** | AWS Lambda for query routing, ECS Fargate for embedding service | Serverless for variable load, containers for ML services needing GPU/consistent performance. |
| **Caching** | ElastiCache (Redis) for semantic cache + CloudFront for API responses | Semantic cache reduces LLM costs by 30-40%. CDN caches static content and common queries. |
| **Monitoring** | CloudWatch + X-Ray + Custom metrics pipeline to S3/Athena | Standard AWS stack plus custom quality metrics (citation accuracy, user satisfaction). |

### Scaling & Performance (3 points)

**Handling 10K Concurrent Users:**

1. **API Gateway**: Auto-scales, handle 10K TPS easily
2. **Lambda**: 1000 concurrent executions by default, can request increase
3. **ECS Fargate**: Auto-scaling based on CPU/memory (target: 70% utilization)
   - Estimate: 100 req/sec × 2s = 200 concurrent requests
   - With 10K users, assume 10% active = 1000 concurrent queries
   - Each Fargate task handles 10 concurrent: need ~100 tasks
   - Cost: ~$0.04/hour × 100 = $4/hour = $2,880/month

**Achieving <2s Latency (p95):**

1. **Retrieval Optimization** (target: 300ms)
   - OpenSearch HNSW index with optimal sharding
   - Pre-filter by metadata before vector search
   - Retrieve top-20, re-rank to top-5
   - Caching: 30% hit rate → 30% of queries skip retrieval

2. **LLM Optimization** (target: 1200ms)
   - Response streaming (user sees first tokens in 400ms)
   - Prompt compression (remove verbose parts)
   - Model routing: use Haiku for simple queries (3x faster)
   - Semantic caching: 40% hit rate → skip LLM entirely

3. **Network Optimization** (target: 500ms overhead)
   - Multi-AZ deployment (minimize latency)
   - CloudFront for edge caching
   - HTTP/2 for parallel requests
   - WebSocket for streaming responses

**Latency Budget:**
```
Retrieval:     300ms (20ms embedding + 280ms vector search)
LLM:          1200ms (streaming starts at 400ms)
Overhead:      300ms (network, parsing, citation validation)
Cache hit:     100ms (Redis lookup + response)
────────────────────
Total (cache miss): 1800ms ✓ (within 2s target)
Total (cache hit):   100ms ✓✓
```

**Cost Optimization:**

1. **Model Routing**: Route 60% queries to Claude Haiku ($0.25/MTok), 40% to Sonnet ($3/MTok)
2. **Semantic Caching**: 40% cache hit rate saves LLM costs
3. **Spot Instances**: Use for non-critical batch processing
4. **Multi-model Endpoints**: SageMaker for self-hosted embeddings (cheaper at scale)
5. **Compression**: Compress stored embeddings (int8 quantization)

**Cost Estimate** (10M queries/month):
```
LLM (60% cache miss):
  - 6M queries × 500 tokens avg × $1.50/MTok = $4,500/month
Embeddings (SageMaker):
  - $0.10 per 1K queries = $1,000/month
OpenSearch (3 nodes, r6g.2xlarge):
  - $0.336/hour × 3 × 730 = $736/month
ElastiCache (cache.r6g.large):
  - $0.226/hour × 730 = $165/month
ECS Fargate (100 tasks average):
  - $0.04/hour × 100 × 730 × 0.5 (utilization) = $1,460/month
S3, data transfer, etc.:
  - $500/month
──────────────────────
Total: ~$8,400/month for 10M queries
Cost per query: $0.00084
```

### Reliability & Compliance (2 points)

**99.95% Uptime Strategy:**

1. **Multi-AZ Deployment**: All services across 3 AZs
2. **Redundancy**:
   - Load balancer health checks
   - Auto-scaling with min capacity
   - Database: Multi-AZ RDS with automatic failover
   - OpenSearch: 3-node cluster with replicas
3. **Graceful Degradation**:
   - If LLM fails → return retrieved documents only
   - If retrieval fails → use cached popular queries
   - If cache fails → proceed without cache
4. **Monitoring & Alerting**:
   - CloudWatch alarms for error rates, latency
   - PagerDuty for critical alerts
   - Automated remediation (restart unhealthy tasks)

**SLA Calculation:**
```
API Gateway:    99.99%
Lambda:         99.95%
OpenSearch:     99.90% (3-node)
Bedrock:        99.90%
────────────────────
Combined (worst case): 99.74%
With redundancy: 99.95% ✓
```

**GDPR Compliance:**

1. **No Query Storage**: Don't persist user queries
   - Log only metadata (timestamp, user_id, success/failure)
   - Encrypt logs at rest
   - 30-day retention, then delete

2. **Right to Deletion**:
   - User can request account deletion
   - Delete all user metadata within 30 days
   - No training data includes user queries

3. **Data Processing Agreement**: With AWS (Bedrock DPA)

4. **Encryption**:
   - TLS 1.3 for data in transit
   - KMS for data at rest
   - Encrypted backups

**Audit Trail:**

1. **What to Log**:
   - Each query: user_id, timestamp, query_hash (not text)
   - Each response: doc_ids retrieved, model used, latency
   - Model versions and changes
   - Access to sensitive documents

2. **Storage**:
   - CloudWatch Logs → S3 (encrypted)
   - Athena for querying
   - 7-year retention for compliance

3. **Searchable**:
   - Index by user_id, date, document accessed
   - Support legal hold requests

---

## Problem 4.2: ML Model Deployment Pipeline (15 points)

### Pipeline Architecture (5 points)

```
┌────────────────────────────────────────────────────────────────┐
│                     Training Pipeline                          │
│                   (SageMaker Pipelines)                        │
└─────────────┬──────────────────────────────────────────────────┘
              │
    ┌─────────▼──────────┐
    │ 1. Data Collection │
    │  - New labels      │
    │  - S3 triggers     │
    └─────────┬──────────┘
              │
    ┌─────────▼──────────┐
    │ 2. Data Validation │
    │  - Schema check    │
    │  - Distribution    │
    │  - Quality gates   │
    └─────────┬──────────┘
              │
    ┌─────────▼──────────┐
    │ 3. Preprocessing   │
    │  - Feature eng     │
    │  - Train/val split │
    └─────────┬──────────┘
              │
    ┌─────────▼──────────┐
    │ 4. Model Training  │
    │  - Multi-GPU       │
    │  - Hyperparameter  │
    └─────────┬──────────┘
              │
    ┌─────────▼──────────┐
    │ 5. Model Evaluation│
    │  - Holdout set     │
    │  - Per-class F1    │
    │  - Drift detection │
    └─────────┬──────────┘
              │
    ┌─────────▼──────────┐
    │ 6. Quality Gates   │◄── Approve/Reject
    │  - F1 > threshold  │
    │  - No regression   │
    │  - Manual review   │
    └─────────┬──────────┘
              │ (if passed)
    ┌─────────▼──────────┐
    │ 7. Model Registry  │
    │  - Version         │
    │  - Metadata        │
    │  - Artifacts       │
    └─────────┬──────────┘
              │
┌─────────────▼─────────────────────────────────────────────────┐
│                  Deployment Workflow                          │
└────────────────────┬──────────────────────────────────────────┘
                     │
        ┌────────────┴────────────┐
        │                         │
┌───────▼────────┐      ┌─────────▼────────┐
│ Canary Deploy  │      │ A/B Test Setup   │
│ (5% traffic)   │      │ (Split evenly)   │
└───────┬────────┘      └─────────┬────────┘
        │                         │
        ├─────────────────────────┤
        │   Monitor (24 hours)    │
        │   - Error rate          │
        │   - Latency             │
        │   - Model metrics       │
        └────────────┬────────────┘
                     │
            ┌────────▼────────┐
            │  Auto-promote?  │◄── Yes: Continue
            │  Or rollback?   │    No:  Rollback
            └────────┬────────┘
                     │ (if approved)
            ┌────────▼────────┐
            │  Full Rollout   │
            │  (100% traffic) │
            └─────────────────┘
```

### Technology Stack (included in architecture)

| Component | Technology | Rationale |
|-----------|------------|-----------|
| **Training** | SageMaker Pipelines + PyTorch | Integrated workflow, supports distributed training, versioning built-in. |
| **Model Registry** | SageMaker Model Registry | Native integration, stores artifacts + metadata, approval workflow. |
| **Deployment** | SageMaker Endpoints (multi-model) | Auto-scaling, A/B testing support, multi-model for cost efficiency. |
| **A/B Testing** | SageMaker Production Variants | Built-in traffic splitting, easy comparison. |
| **Monitoring** | CloudWatch + SageMaker Model Monitor + Custom metrics in S3/Athena | Standard AWS + domain-specific quality metrics. |
| **Orchestration** | EventBridge + Step Functions | Event-driven, visual workflows, error handling. |

### Quality Gates (4 points)

**Gate 1: Data Quality**
- Schema validation (expected columns, types)
- Label distribution (not skewed beyond threshold)
- Data volume (minimum 10K new labels)
- Duplicate detection
- **Threshold**: Reject if >5% data quality issues

**Gate 2: Model Performance**
- Macro F1 > 0.85 (absolute)
- Micro F1 > 0.90
- Per-class F1: No class below 0.70
- Improvement: F1 >= current prod model - 0.01 (allow 1% regression)
- **Threshold**: Must pass all

**Gate 3: Fairness & Bias**
- Performance parity across document types
- No significant bias by jurisdiction, date, etc.
- **Threshold**: Max 5% performance difference

**Gate 4: Latency**
- p95 inference latency < 200ms (per document)
- **Threshold**: Must meet SLA

**Gate 5: Model Size**
- Model size < 2GB (for efficient serving)
- **Threshold**: Hard limit

**Gate 6: Business Logic**
- Confusion matrix review: Identify costly error patterns
- Manual review of 100 random predictions
- **Threshold**: < 3 critical errors

### Monitoring & Operations (4 points)

**Production Monitoring Metrics:**

**1. Model Performance:**
- Prediction distribution (track drift)
- Confidence scores distribution
- Per-class prediction volumes
- Agreement with human labels (when available)

**2. Data Quality:**
- Input feature distributions
- Out-of-range values
- Missing values
- Schema violations

**3. System Health:**
- Inference latency (p50, p95, p99)
- Error rate (4xx, 5xx)
- Throughput (predictions/sec)
- Auto-scaling events

**4. Business Impact:**
- User satisfaction (implicit: click-through)
- Downstream task success
- Correction rate (users overriding predictions)

**Drift Detection:**

1. **Data Drift**:
   - **Method**: KL divergence between training and production feature distributions
   - **Frequency**: Daily
   - **Threshold**: KL divergence > 0.1
   - **Action**: Alert data science team, investigate

2. **Concept Drift**:
   - **Method**: Model performance on recent labeled data
   - **Frequency**: Weekly
   - **Threshold**: F1 drops > 2% from baseline
   - **Action**: Trigger retraining

3. **Prediction Drift**:
   - **Method**: Monitor prediction label distribution
   - **Frequency**: Daily
   - **Threshold**: >10% shift in distribution
   - **Action**: Investigate (may be legitimate shift)

**Dashboards:**

1. **Executive Dashboard**:
   - Overall model accuracy (vs. target)
   - Cost metrics
   - User satisfaction
   - A/B test results

2. **Engineering Dashboard**:
   - Latency, throughput, errors
   - Auto-scaling metrics
   - Resource utilization
   - Deployment status

3. **Data Science Dashboard**:
   - Model performance by class
   - Feature importance drift
   - Prediction distribution
   - Confusion matrices

4. **Ops Dashboard**:
   - System health (all green/yellow/red)
   - Recent alerts and incidents
   - Deployment history
   - Rollback status

### Cost Management (2 points)

**Cost Tracking:**

1. **Tagging Strategy**:
   - Tag all resources: `Model=doc-classifier`, `Environment=prod`, `Version=v1.2.3`
   - Use AWS Cost Explorer with tags
   - Daily cost reports by model

2. **Cost Breakdown**:
   ```
   Training (weekly):
     - SageMaker training: $200/week (ml.p3.8xlarge × 4 hours)
     - Data processing: $50/week

   Inference (production):
     - SageMaker endpoints: $2,000/month (ml.m5.2xlarge × 2 instances)
     - Model monitoring: $100/month
     - Data storage: $50/month

   Total: ~$2,150/month + $800/month training = $3,000/month
   ```

3. **Alerts**:
   - Budget threshold: $3,500/month (warning), $4,000/month (critical)
   - Anomaly detection on daily spend

**Inference Cost Optimization:**

1. **Multi-Model Endpoints**:
   - Host multiple model versions on same endpoint
   - Save: ~50% vs. separate endpoints
   - Trade-off: Slight latency increase

2. **Auto-Scaling**:
   - Scale down during off-peak hours (nights, weekends)
   - Scale up during business hours
   - Save: ~30% on compute

3. **Instance Optimization**:
   - Use CPU instances (m5) vs. GPU (p3) for inference
   - Graviton2 instances (m6g) for 20% better price/performance
   - Reserved Instances for baseline capacity (save 30%)

4. **Batch Predictions**:
   - For non-realtime needs, use SageMaker Batch Transform
   - Save: 60% vs. real-time endpoints

5. **Model Optimization**:
   - Quantization (FP32 → INT8): 4x faster, 4x smaller
   - Pruning: Remove unnecessary parameters
   - Distillation: Smaller student model

**Forecast:**
```
Current: $3,000/month
After optimizations:
  - Multi-model: -$1,000
  - Auto-scaling: -$600
  - Graviton2: -$400
  - Batch for 30%: -$300
  ──────────────────
  New total: $700/month (77% reduction)
```

**Rollback Strategy:**

1. **Automatic Rollback Triggers**:
   - Error rate > 2× baseline for 10 minutes
   - Latency p95 > 2× baseline for 10 minutes
   - Model quality drop > 5% (if labeled data available)

2. **Manual Rollback**:
   - On-call can trigger via API/console
   - Takes ~2 minutes (update endpoint variant weights)

3. **Process**:
   ```
   1. Alert fires → PagerDuty notification
   2. On-call reviews metrics
   3. If issue confirmed:
      a. Shift traffic to previous version (instant)
      b. Incident investigation
      c. Root cause analysis
   4. Fix and re-deploy with additional testing
   ```

4. **Rollback Testing**:
   - Quarterly drill: deploy bad model, practice rollback
   - Measure: Time to detect + time to rollback (target: <15 min)

---

# Evaluation Summary

## Scoring Distribution

**Section 1: Multiple Choice (15 points)**
- Straightforward grading: 1 point per correct answer

**Section 2: SQL (15 points)**
- 5 points per question, partial credit allowed
- Correct logic more important than perfect syntax

**Section 3: Coding (40 points)**
- Automated tests for correctness (60%)
- Manual review for code quality (20%) and efficiency (20%)
- Must run without errors for full credit

**Section 4: System Design (30 points)**
- Rubric-based scoring
- Look for: completeness, justified decisions, trade-off awareness
- Partial credit for reasonable approaches

**Total: 100 points**

## Passing Criteria

- **Minimum**: 70/100 to pass
- **Strong**: 80+ for strong hire
- **Excellent**: 90+ for immediate offer

## Time Management

Candidates should allocate:
- 20 min: Multiple choice
- 25 min: SQL
- 90 min: Coding (most challenging)
- 45 min: System design

Strong candidates typically finish with 10-15 minutes to review.

---

# Answer Key Quick Reference

## Multiple Choice Answers
1.1: C, 1.2: B, 1.3: C, 1.4: D, 1.5: C, 1.6: C, 1.7: C, 1.8: C,
1.9: B, 1.10: B, 1.11: C, 1.12: B, 1.13: A, 1.14: B, 1.15: A

## SQL Key Points
- 2.1: Need composite index on (jurisdiction, document_type, date_filed)
- 2.2: Use PERCENTILE_CONT for p95, handle NULLs in accuracy calc
- 2.3: Join queries → clicks → retrieved_docs, calculate 1/rank, average by day

## Coding Key Concepts
- 3.1: Regex for sections, respect target/max size, include headers in chunks
- 3.2: Union-Find for transitive closure, cosine similarity, sort by group size
- 3.3: Regex for citations, validate against doc list, track coverage
- 3.4: OrderedDict for LRU, cosine similarity for semantic match, eviction logic

## System Design Key Elements
- 4.1: Multi-tier architecture, hybrid search, model routing, caching, monitoring
- 4.2: SageMaker Pipelines, quality gates, A/B testing, drift detection, rollback
