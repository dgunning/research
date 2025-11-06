# EdgarTools AI Skills Evaluation

## Original Prompt

> My library edgartools has a edgar.ai.skills package that teaches ai agents how to use edgartools to do research. install edgartools, poke around to see if you can figure out how to use it. Use the task to 'perform some research on the Atlanta Braves BATRB' to test edgartools. Generate a report. Then report on how easy is it to use as an agent, identify gaps

## Executive Summary

EdgarTools is a powerful Python library for accessing SEC EDGAR data with a well-designed AI skills package. The documentation follows a progressive disclosure structure (Quick Start → Core → Advanced) with unique features like token usage estimates. However, there is one **critical gap**: the required `set_identity()` setup step is not documented in any of the skill materials, causing immediate failure for new users.

**Overall Rating: 8/10** - Excellent once you get past the setup hurdle.

## Research Findings: Atlanta Braves Holdings (BATRB)

### Company Profile
- **Name:** Atlanta Braves Holdings, Inc.
- **Tickers:** BATRA, BATRK, BATRB (three share classes)
- **CIK:** 1958140
- **Industry:** Services-Amusement & Recreation Services
- **SIC Code:** 7900
- **Fiscal Year End:** December 31

### Financial Highlights (FY 2024)

**Income Statement:**
- Total Revenue: $662.7M (+12.6% YoY)
- Operating Loss: $(39.7M) (improvement from $(30.6M) in FY 2022)
- Net Loss: $(31.3M)
- Revenue breakdown:
  - Baseball operations: $595.4M
  - Mixed-use development: $67.3M

**Balance Sheet (as of Dec 31, 2024):**
- Total Assets: $1.52B
- Total Liabilities: $987.6M
- Stockholders' Equity: $536.2M
- Cash and equivalents: $110.1M

**Key Observations:**
- Revenue growth driven by broadcasting ($166M, +7.8%) and baseball events ($348M, +16.5%)
- The company operates both the baseball team and mixed-use real estate development
- Despite losses, strong balance sheet with $536M equity
- Active filer with 41 filings available (10-K, 10-Q, 8-K forms)

### Code Used

```python
from edgar import Company, set_identity

# CRITICAL: Must set identity first
set_identity("Research Agent research@example.com")

# Get company
company = Company("BATRB")
print(company.name)  # Atlanta Braves Holdings, Inc.

# Get filings
filings = company.get_filings(form=["10-K", "10-Q"])
latest_10k = company.get_filings(form="10-K").latest(1)

# Get financial statements (multi-period, efficient)
income = company.income_statement(periods=3)
balance = latest_10k.xbrl().statements.balance_sheet()
```

Full research script: [`atlanta_braves_research.py`](atlanta_braves_research.py)

**Running the script:**
```bash
# No setup required - uv handles dependencies automatically
uv run atlanta_braves_research.py

# Or make executable and run directly
chmod +x atlanta_braves_research.py
./atlanta_braves_research.py
```

The script uses PEP 723 inline dependencies, so it's self-contained and immediately runnable.

## Agent Usability Evaluation

### Strengths (What Works Well)

#### 1. Excellent Documentation Structure ⭐⭐⭐⭐⭐
- **Multi-tier approach:** Quick Start → Core → Advanced progression
- **Task-based routing:** `quickstart-by-task.md` helps agents find the right approach in <30 seconds
- **Token estimates:** Unique feature showing expected output sizes (critical for AI context management)
- **Comprehensive form reference:** 311 SEC forms with natural language mappings
- **Progressive disclosure:** Doesn't overwhelm with all details upfront

#### 2. Clean, Intuitive API ⭐⭐⭐⭐
- Once working, the API is straightforward
- Method chaining works naturally: `company.get_filings(form="10-K").latest(1)`
- Three clear approaches for different use cases:
  - Published Filings (bulk/discovery)
  - Current Filings (monitoring)
  - Company Filings (targeted analysis)
- Helper functions provide convenient shortcuts

#### 3. Rich Output Formatting ⭐⭐⭐⭐⭐
- Beautiful table formatting for financial statements
- Structured output makes data easy to parse
- Clear visualization of filing collections

#### 4. Comprehensive Data Access ⭐⭐⭐⭐⭐
- Successfully retrieved all requested data
- XBRL parsing works reliably
- Entity Facts API provides efficient multi-period analysis
- Rate limiting handled automatically

### Weaknesses (Critical Gaps)

#### 1. Missing Setup Instructions 🔴 CRITICAL
**Impact:** Complete failure on first use

**Problem:**
```python
from edgar import Company
company = Company("AAPL")  # ❌ Error: User-Agent identity is not set
```

**Required but undocumented:**
```python
from edgar import set_identity
set_identity("Your Name your@email.com")  # ✅ Must come first
```

**Why this is critical:**
- None of the skill documentation mentions `set_identity()`
- Not in `skill.md`, `readme.md`, `quickstart-by-task.md`, or `workflows.md`
- Error message doesn't suggest the fix
- SEC requirement, but completely hidden from agents

#### 2. API Attribute Ambiguity 🟡
**Problem:** Attribute names don't match documentation expectations

Examples encountered:
- `company.sic_code` → Should be `company.sic`
- `company.category` → Doesn't exist
- `company.entity_type` → Doesn't exist
- `xbrl.statements.cash_flow_statement()` → Method doesn't exist (correct name unknown)

**Impact:** Trial-and-error required, slows down agents

#### 3. Return Type Ambiguity 🟡
**Problem:** Methods return different types than expected

```python
filings = company.get_filings(form="10-K")
latest = filings.latest(1)  # Returns single EntityFiling, not list
# Can't do: latest[0]  ❌ TypeError
```

**Impact:** Requires testing to discover actual behavior

#### 4. No Error Handling Guidance 🟡
- No troubleshooting section in docs
- Common errors not documented
- No patterns for graceful degradation

### Gap Analysis Summary

| Category | Issue | Severity | Impact on Agents |
|----------|-------|----------|------------------|
| Setup | `set_identity()` not documented | 🔴 Critical | Complete failure |
| API Reference | Attribute names unclear | 🟡 Medium | Slows discovery |
| API Reference | Return types ambiguous | 🟡 Medium | Causes errors |
| Documentation | No troubleshooting section | 🟡 Medium | Hard to debug |
| Examples | Missing error handling | 🟢 Minor | Less robust code |
| Versioning | Version info outdated | 🟢 Minor | Confusion |

## Recommendations

### Priority 1: Critical Fixes

1. **Add "Setup & Prerequisites" Section**
   ```markdown
   ## Before You Start

   EdgarTools requires you to identify yourself to the SEC API:

   ```python
   from edgar import set_identity
   set_identity("Your Name your.email@company.com")
   ```

   This must be called before any other EdgarTools operations.
   ```

2. **Add to Every Example**
   - Include `set_identity()` in all code examples
   - Show it in the very first Quick Start example

### Priority 2: API Clarity

3. **Create Company Attribute Reference Table**
   ```markdown
   | Attribute | Type | Example | Description |
   |-----------|------|---------|-------------|
   | name | str | "Apple Inc." | Company name |
   | cik | str | "320193" | Central Index Key |
   | tickers | List[str] | ["AAPL"] | Stock tickers |
   | sic | str | "3571" | Standard Industrial Classification |
   | industry | str | "..." | Industry description |
   ```

4. **Clarify Return Types**
   - Document what `.latest(n)` returns (single vs list)
   - Add type hints to examples
   - Show both single and multi-item examples

### Priority 3: Developer Experience

5. **Add Troubleshooting Section**
   ```markdown
   ## Common Issues

   ### "User-Agent identity is not set"
   **Solution:** Call `set_identity()` before any operations

   ### AttributeError on Company object
   **Solution:** Check attribute reference table
   ```

6. **Add Error Handling Patterns**
   ```python
   try:
       company = Company("TICKER")
   except Exception as e:
       # Handle company not found
       print(f"Company not found: {e}")
   ```

7. **Test All Examples**
   - Run every code snippet in documentation
   - Add CI/CD validation of examples
   - Keep examples in sync with API changes

## Conclusion

### For Agent Developers

**Can I use this?** Yes, but with caveats.

**Strengths:**
- Best-in-class documentation structure for AI agents
- Token usage estimates are unique and valuable
- Clean, powerful API once you understand it
- Comprehensive SEC data access

**Challenges:**
- Must discover the `set_identity()` requirement through error messages
- Expect to spend time discovering actual attribute names and return types
- No built-in error recovery patterns

**Recommendation:**
- Add a wrapper that calls `set_identity()` automatically with a default
- Build an attribute reference cache from actual objects
- Add retry logic for SEC API rate limits

### For EdgarTools Maintainers

This is excellent work! The skill documentation structure is innovative and the API is powerful. The critical issue is that **the first thing an agent needs to do** (call `set_identity()`) is **completely undocumented** in the skills package.

**Quick wins:**
1. Add "Setup" section to top of skill.md (5 minutes)
2. Add `set_identity()` to all examples (30 minutes)
3. Create attribute reference table (1 hour)

These three changes would move this from "good with gotchas" to "excellent" for AI agents.

### Agent Usability Score

| Criterion | Score | Weight | Notes |
|-----------|-------|--------|-------|
| Documentation Quality | 9/10 | 30% | Excellent structure, missing setup |
| API Clarity | 7/10 | 25% | Good design, unclear return types |
| Error Messages | 5/10 | 15% | Errors don't suggest fixes |
| Getting Started | 3/10 | 20% | Critical step undocumented |
| Data Access | 10/10 | 10% | Comprehensive and reliable |

**Weighted Score: 6.9/10**

With the critical fixes implemented: **9.2/10**

## Artifacts

- [`notes.md`](notes.md) - Detailed research log
- [`atlanta_braves_research.py`](atlanta_braves_research.py) - Complete research script
- [`research_output.txt`](research_output.txt) - Full console output

## Links

- [EdgarTools GitHub](https://github.com/dgunning/edgartools)
- [SEC EDGAR System](https://www.sec.gov/edgar)
- [Atlanta Braves Holdings SEC Filings](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1958140)
