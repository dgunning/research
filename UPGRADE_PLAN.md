# Research Project Upgrade Plan: Self-Contained Scripts with uv

## Current Problem

Research scripts require manual dependency installation:
```bash
pip install edgartools  # Required before running
python script.py
```

This makes scripts:
- Less portable
- Harder to reproduce
- Require setup documentation
- Break if dependencies aren't installed

## Proposed Solution

Use `uv` with PEP 723 inline script metadata to make scripts self-contained:

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "edgartools>=4.26.0",
#     "rich>=13.0.0",
# ]
# ///

from edgar import Company
# Script just works!
```

Run with: `uv run script.py` (no setup needed!)

## Benefits

1. **Self-Contained**: Each script declares its own dependencies
2. **Reproducible**: Version pinning in the script itself
3. **No Setup**: No pip install, no venv management
4. **Fast**: uv caches dependencies, subsequent runs are instant
5. **Isolated**: Each script gets its own environment automatically
6. **Portable**: Share script = share everything needed to run it

## Upgrade Tasks

### 1. Update AGENTS.md

Add sections:
- **Writing Self-Contained Scripts**: How to use PEP 723 syntax
- **Running Scripts**: Use `uv run script.py`
- **Best Practices**: Pin versions, minimal dependencies

### 2. Update CLAUDE.md

Add uv workflow to the instructions.

### 3. Create Script Template

Provide a template agents can copy:
```python
#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "package>=version",
# ]
# ///
"""
Script description.
"""

# Your code here
```

### 4. Update Existing Scripts

Update `edgartools-ai-skills-evaluation/atlanta_braves_research.py` as reference example.

### 5. Add Documentation

- Add `SCRIPTS.md` with examples
- Update README.md to mention uv approach
- Add troubleshooting for common issues

### 6. Optional: GitHub Actions

Consider if cogapp README generation needs uv support.

## Implementation Details

### PEP 723 Inline Script Metadata Format

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "package1>=1.0.0",
#     "package2>=2.0.0",
# ]
# ///
```

**Key points:**
- Must be at the top of the file (after shebang/docstring)
- Use `# ///` delimiters (3 slashes, space, word)
- TOML syntax inside the block
- Can specify Python version requirements
- Can pin exact versions or use ranges

### Running Scripts

**Basic:**
```bash
uv run script.py
```

**With arguments:**
```bash
uv run script.py --arg value
```

**Direct execution (if executable):**
```bash
./script.py  # If has #!/usr/bin/env -S uv run
```

### Best Practices for Agents

1. **Always include metadata block** in scripts with dependencies
2. **Pin major versions** for stability: `package>=4.0.0,<5.0.0`
3. **Keep dependencies minimal** - only what's needed
4. **Document why** each dependency is needed in comments
5. **Test with `uv run`** before committing

## Example: Before vs After

### Before (Current)
```python
# atlanta_braves_research.py
from edgar import Company, set_identity
# ... code ...
```

Running:
```bash
pip install edgartools  # Must do this first!
python atlanta_braves_research.py
```

### After (Upgraded)
```python
#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "edgartools>=4.26.0",
# ]
# ///
"""Research Atlanta Braves using edgartools."""

from edgar import Company, set_identity
# ... code ...
```

Running:
```bash
uv run atlanta_braves_research.py  # Just works!
# or if executable:
./atlanta_braves_research.py
```

## Migration Path

1. **Phase 1: Documentation** (this commit)
   - Update AGENTS.md with uv guidelines
   - Create script template
   - Document best practices

2. **Phase 2: Examples** (this commit)
   - Update atlanta_braves_research.py
   - Add example scripts to show patterns

3. **Phase 3: Future Research**
   - All new research projects use uv approach
   - README generation respects uv scripts

## Compatibility Notes

- **uv version**: Requires uv >= 0.4.0 (we have 0.8.17 ✓)
- **Python version**: PEP 723 is Python version agnostic
- **Fallback**: Scripts can still run with `python script.py` if dependencies installed
- **CI/CD**: GitHub Actions supports uv with astral-sh/setup-uv

## Files to Update

1. `/home/user/research/AGENTS.md` - Add uv section
2. `/home/user/research/CLAUDE.md` - Reference uv usage
3. `/home/user/research/.github/workflows/update-readme.yml` - Maybe add uv support
4. `/home/user/research/edgartools-ai-skills-evaluation/atlanta_braves_research.py` - Convert to uv
5. Create: `/home/user/research/SCRIPTS.md` - Template and examples

## Testing Plan

1. Convert atlanta_braves_research.py to use inline dependencies
2. Test: `uv run edgartools-ai-skills-evaluation/atlanta_braves_research.py`
3. Verify it works without any pip install
4. Test on fresh environment to confirm isolation

## Open Questions

1. Should we require uv for all scripts, or make it optional?
   - **Recommendation**: Strongly encourage, not require

2. Should simple scripts without dependencies skip the metadata block?
   - **Recommendation**: Yes, only add if needed

3. How to handle scripts that need system dependencies (not Python packages)?
   - **Recommendation**: Document in script docstring, keep using bash/apt

## Success Criteria

- [ ] AGENTS.md includes uv guidelines
- [ ] Script template created
- [ ] atlanta_braves_research.py converted and tested
- [ ] Documentation is clear and includes examples
- [ ] New researchers can run scripts with zero setup

## Timeline

All changes in single commit for atomic upgrade.

## References

- [PEP 723 - Inline script metadata](https://peps.python.org/pep-0723/)
- [uv documentation](https://docs.astral.sh/uv/)
- [uv scripts guide](https://docs.astral.sh/uv/guides/scripts/)
