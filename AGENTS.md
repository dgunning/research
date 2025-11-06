Start by creating a new folder for your work with an appropriate name.

Create a notes.md file in that folder and append notes to it as you work, tracking what you tried and anything you learned along the way.

Build a README.md report at the end of the investigation. The README should start with the original prompt that initiated this research project, followed by your findings and results.

## Writing Self-Contained Scripts

When writing Python scripts that require external dependencies, use **uv with inline script metadata** (PEP 723) to make them self-contained and immediately runnable.

### Basic Pattern

Add a metadata block at the top of your script:

```python
#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "package-name>=version",
# ]
# ///
"""
Script description here.
"""

import package_name
# Your code...
```

### Running Scripts

```bash
# Just run with uv - no pip install needed!
uv run script.py

# Or make executable and run directly
chmod +x script.py
./script.py
```

### Best Practices

1. **Pin major versions** for stability: `"edgartools>=4.26.0,<5.0.0"`
2. **Keep dependencies minimal** - only include what you actually use
3. **Document why** each dependency is needed in comments
4. **Test with `uv run`** before committing

### Example

```python
#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "requests>=2.31.0",  # HTTP requests
#     "beautifulsoup4>=4.12.0",  # HTML parsing
# ]
# ///
"""Scrape and analyze web data."""

import requests
from bs4 import BeautifulSoup

# Script just works - no setup required!
```

See [SCRIPTS.md](SCRIPTS.md) for more templates and examples.

## Final Commit Contents

Your final commit should include just that folder and selected items from its contents:

- The notes.md and README.md files
- Any code you wrote along the way
- If you checked out and modified an existing repo, the output of "git diff" against that modified repo saved as a file - but not a copy of the full repo
- If appropriate, any binary files you created along the way provided they are less than 2MB in size

Do NOT include full copies of code that you fetched as part of your investigation. Your final commit should include only new files you created or diffs showing changes you made to existing code.

Don't create a _summary.md file - these are added automatically after you commit your changes.
