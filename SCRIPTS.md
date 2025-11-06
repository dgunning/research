# Self-Contained Scripts with uv

This guide shows how to write Python scripts with inline dependencies using uv and PEP 723, making them immediately runnable without setup.

## Why Use Inline Dependencies?

**Problems with traditional approach:**
```bash
pip install package1 package2  # Must remember to do this
python script.py               # Then run
```

**Benefits of inline dependencies:**
- ✅ Self-contained - script includes everything needed
- ✅ Reproducible - versions locked in script
- ✅ No setup - just `uv run script.py`
- ✅ Fast - uv caches dependencies
- ✅ Isolated - each script gets own environment
- ✅ Portable - share script = share environment

## Basic Template

```python
#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "package-name>=1.0.0",
# ]
# ///
"""
Script description here.

Usage:
    uv run script.py
"""

import package_name

def main():
    # Your code here
    pass

if __name__ == "__main__":
    main()
```

## Running Scripts

```bash
# Option 1: Run with uv (always works)
uv run script.py

# Option 2: Make executable and run directly
chmod +x script.py
./script.py

# Option 3: Pass arguments
uv run script.py --arg value

# Option 4: Run from different directory
uv run path/to/script.py
```

## Common Templates

### 1. Data Analysis Script

```python
#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pandas>=2.0.0",
#     "matplotlib>=3.7.0",
#     "seaborn>=0.12.0",
# ]
# ///
"""
Analyze data and generate visualizations.

Usage:
    uv run analyze.py input.csv
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    if len(sys.argv) < 2:
        print("Usage: uv run analyze.py input.csv")
        sys.exit(1)

    df = pd.read_csv(sys.argv[1])
    # Analysis code...

if __name__ == "__main__":
    main()
```

### 2. Web Scraping Script

```python
#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "requests>=2.31.0",
#     "beautifulsoup4>=4.12.0",
#     "lxml>=5.0.0",  # Fast XML/HTML parser
# ]
# ///
"""
Scrape data from websites.

Usage:
    uv run scrape.py https://example.com
"""

import sys
import requests
from bs4 import BeautifulSoup

def scrape_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    # Scraping logic...
    return data

def main():
    if len(sys.argv) < 2:
        print("Usage: uv run scrape.py URL")
        sys.exit(1)

    url = sys.argv[1]
    data = scrape_url(url)
    print(data)

if __name__ == "__main__":
    main()
```

### 3. API Client Script

```python
#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "httpx>=0.25.0",  # Modern HTTP client
#     "pydantic>=2.0.0",  # Data validation
#     "rich>=13.0.0",  # Beautiful output
# ]
# ///
"""
Interact with REST API and display results.

Usage:
    uv run api_client.py --endpoint users
"""

import httpx
from pydantic import BaseModel
from rich import print as rprint

class User(BaseModel):
    id: int
    name: str
    email: str

def fetch_users():
    with httpx.Client() as client:
        response = client.get("https://api.example.com/users")
        users = [User(**u) for u in response.json()]
        return users

def main():
    users = fetch_users()
    for user in users:
        rprint(user)

if __name__ == "__main__":
    main()
```

### 4. Database Query Script

```python
#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "sqlalchemy>=2.0.0",
#     "pandas>=2.0.0",
# ]
# ///
"""
Query database and export results.

Usage:
    uv run query.py "SELECT * FROM table"
"""

import sys
from sqlalchemy import create_engine, text
import pandas as pd

def query_database(query_str):
    engine = create_engine("postgresql://user:pass@localhost/db")
    df = pd.read_sql(text(query_str), engine)
    return df

def main():
    if len(sys.argv) < 2:
        print("Usage: uv run query.py 'SQL QUERY'")
        sys.exit(1)

    df = query_database(sys.argv[1])
    print(df)

if __name__ == "__main__":
    main()
```

### 5. File Processing Script

```python
#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pyyaml>=6.0.0",
#     "toml>=0.10.0",
#     "jsonschema>=4.0.0",
# ]
# ///
"""
Process and validate configuration files.

Usage:
    uv run process.py config.yaml
"""

import sys
import yaml
import json
from jsonschema import validate

def process_config(filepath):
    with open(filepath) as f:
        config = yaml.safe_load(f)

    # Validation schema
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "version": {"type": "string"}
        },
        "required": ["name", "version"]
    }

    validate(instance=config, schema=schema)
    return config

def main():
    if len(sys.argv) < 2:
        print("Usage: uv run process.py config.yaml")
        sys.exit(1)

    config = process_config(sys.argv[1])
    print(json.dumps(config, indent=2))

if __name__ == "__main__":
    main()
```

## Version Pinning Strategies

### Flexible (Recommended for Research)
```python
# dependencies = [
#     "requests>=2.31.0",  # Allow minor/patch updates
# ]
```

### Conservative
```python
# dependencies = [
#     "requests>=2.31.0,<3.0.0",  # Lock major version
# ]
```

### Exact (For Reproducibility)
```python
# dependencies = [
#     "requests==2.31.0",  # Exact version only
# ]
```

### With Extras
```python
# dependencies = [
#     "httpx[http2]>=0.25.0",  # Include optional dependencies
# ]
```

## Best Practices

### 1. Document Dependencies

```python
# dependencies = [
#     "requests>=2.31.0",      # HTTP client for API calls
#     "pandas>=2.0.0",         # Data manipulation
#     "matplotlib>=3.7.0",     # Visualization
# ]
```

### 2. Keep Dependencies Minimal

❌ Bad:
```python
# dependencies = [
#     "numpy",
#     "pandas",
#     "matplotlib",
#     "seaborn",
#     "scipy",
#     "scikit-learn",  # Not actually using all of these!
# ]
```

✅ Good:
```python
# dependencies = [
#     "pandas>=2.0.0",  # Only what I need
# ]
```

### 3. Pin Python Version

```python
# /// script
# requires-python = ">=3.11"  # Specify minimum version
# dependencies = [...]
# ///
```

### 4. Add Helpful Docstrings

```python
"""
Brief description of what the script does.

Usage:
    uv run script.py arg1 arg2

Options:
    --verbose    Show detailed output
    --output     Specify output file

Examples:
    uv run script.py data.csv --output results.json
"""
```

### 5. Handle Errors Gracefully

```python
def main():
    try:
        # Your code
        pass
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

## Troubleshooting

### Script Won't Run

**Problem:** `uv: command not found`

**Solution:** Install uv:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

**Problem:** `ModuleNotFoundError` even with dependencies declared

**Solution:** Check the metadata block syntax:
- Must start with `# /// script`
- Must end with `# ///`
- Must be valid TOML syntax

---

**Problem:** Script is slow on first run

**Solution:** This is normal! uv is downloading dependencies. Subsequent runs use cache and are fast.

---

**Problem:** Need to use system Python instead of uv

**Solution:** Install dependencies manually and run with python:
```bash
pip install package1 package2
python script.py
```

### Debugging Dependencies

**Check what uv would install:**
```bash
uv run --dry-run script.py
```

**Force reinstall:**
```bash
uv run --reinstall script.py
```

**Use specific Python version:**
```bash
uv run --python 3.11 script.py
```

## Advanced Features

### Multiple Python Files

If your script imports local modules, structure like this:

```
project/
├── main.py          # Entry point with metadata
├── helpers.py       # Local module
└── utils.py         # Another local module
```

```python
#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = ["requests>=2.31.0"]
# ///
"""Main entry point."""

from helpers import helper_function
from utils import utility_function

def main():
    helper_function()
    utility_function()

if __name__ == "__main__":
    main()
```

Run from the project directory:
```bash
cd project/
uv run main.py
```

### Environment Variables

```python
#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = ["python-dotenv>=1.0.0"]
# ///
"""Script that uses environment variables."""

import os
from dotenv import load_dotenv

def main():
    load_dotenv()  # Load from .env file
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("Error: API_KEY not set")
        sys.exit(1)

    # Use api_key...

if __name__ == "__main__":
    main()
```

### Configuration Files

```python
#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pydantic>=2.0.0",
#     "pydantic-settings>=2.0.0",
# ]
# ///
"""Script with configuration."""

from pydantic_settings import BaseSettings

class Config(BaseSettings):
    api_key: str
    endpoint: str = "https://api.example.com"

    class Config:
        env_file = ".env"

def main():
    config = Config()
    print(f"Using endpoint: {config.endpoint}")

if __name__ == "__main__":
    main()
```

## Examples in This Repository

See working examples in the research projects:

- `edgartools-ai-skills-evaluation/atlanta_braves_research.py` - SEC data analysis
- (More examples as projects are added)

## Resources

- [PEP 723 - Inline script metadata](https://peps.python.org/pep-0723/)
- [uv documentation](https://docs.astral.sh/uv/)
- [uv scripts guide](https://docs.astral.sh/uv/guides/scripts/)

## Quick Reference

| Task | Command |
|------|---------|
| Run script | `uv run script.py` |
| Run with args | `uv run script.py arg1 arg2` |
| Make executable | `chmod +x script.py` |
| Run executable | `./script.py` |
| Check dependencies | `uv run --dry-run script.py` |
| Force reinstall | `uv run --reinstall script.py` |
| Use specific Python | `uv run --python 3.11 script.py` |
