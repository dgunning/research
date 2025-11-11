#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Generate blog post templates for different types of technical articles.

This script creates markdown templates pre-structured for different
types of technical blog posts (tutorials, deep dives, comparisons, etc.).

Usage:
    ./blog-generator.py <type> <title> [output-file]

Types:
    tutorial    - Step-by-step tutorial
    deepdive    - Deep technical explanation
    comparison  - Comparing technologies/approaches
    problem     - Problem-solution format
    guide       - Comprehensive guide

Examples:
    ./blog-generator.py tutorial "Building a REST API"
    ./blog-generator.py comparison "React vs Vue" react-vs-vue.md
"""

import sys
from pathlib import Path
from datetime import date


TUTORIAL_TEMPLATE = """# {title}

{hook_placeholder}

## TL;DR
- **What you'll build:** [Describe the end result]
- **Time required:** [Estimate]
- **Skill level:** [Beginner/Intermediate/Advanced]
- **Key technologies:** [List main tech used]

## Prerequisites

Before starting, you should have:
- [Prerequisite 1]
- [Prerequisite 2]
- [Tool/software needed]

## What We're Building

[Describe the final project and show what it will do. Include a screenshot or demo if possible.]

## Step 1: Project Setup

[Explain the initial setup]

```bash
# Commands for setup
```

**What this does:**
[Explain what the setup accomplishes]

## Step 2: [Core Implementation]

[Explain the main feature]

```language
// Your code here with comments
```

**Breaking it down:**
- [Explain key parts]
- [Explain why this approach]

## Step 3: [Additional Features]

[Continue building...]

## Step 4: Testing

Let's verify everything works:

```bash
# Test commands
```

**Expected output:**
```
[What users should see]
```

## Complete Code

Here's the full implementation:

```language
// Complete, runnable code
```

## Common Issues

### Issue 1: [Common error]
**Symptoms:** [What user sees]
**Solution:** [How to fix]

### Issue 2: [Another common error]
**Symptoms:** [What user sees]
**Solution:** [How to fix]

## Next Steps

Now that you've built this, you can:
- [Enhancement 1]
- [Enhancement 2]
- [Related concept to explore]

## Additional Resources

- [Official docs](URL)
- [Related article](URL)
- [Tool/library](URL)

## Conclusion

[Summarize what was accomplished]
[Reinforce key learning points]

**What did you build?** Share your implementation or ask questions in the comments below!

---

*Written by [Your Name] on {date}*
"""


DEEPDIVE_TEMPLATE = """# {title}

{hook_placeholder}

## What This Article Covers

- [Main topic 1]
- [Main topic 2]
- [Main topic 3]
- **Best for:** [Target audience]
- **Reading time:** [Estimate]

## Introduction

[Set the stage - why does this topic matter?]
[What problem does it solve or what understanding does it provide?]

## The Basics

Before diving deep, let's establish the fundamentals:

[High-level overview of the concept]

**Key terminology:**
- **[Term 1]:** [Definition]
- **[Term 2]:** [Definition]

## How It Works Internally

Now let's examine what's happening under the hood.

### The Mechanism

[Detailed explanation of the core mechanism]

```language
// Code example illustrating the concept
```

[Diagram or visual representation]

### The Process Flow

1. [Step 1 in the process]
2. [Step 2 in the process]
3. [Step 3 in the process]

[Detailed explanation of each step]

## Practical Implications

Understanding the internals helps us make better decisions:

### Performance Characteristics

[Explain time/space complexity, performance traits]

**Benchmarks:**
```
[Performance data or examples]
```

### When to Use This

**Best suited for:**
- [Scenario 1]
- [Scenario 2]

**Not ideal for:**
- [Scenario 3]
- [Scenario 4]

## Real-World Examples

### Example 1: [Use case]

[Describe a real scenario]

```language
// Implementation code
```

[Explanation of why this works well]

### Example 2: [Another use case]

[Another practical example]

## Advanced Concepts

For those who want to go deeper:

### [Advanced topic 1]

[Detailed explanation]

### [Advanced topic 2]

[Detailed explanation]

## Common Misconceptions

### Misconception 1: [Wrong belief]

**Reality:** [Correct understanding]
**Why it matters:** [Implications]

### Misconception 2: [Wrong belief]

**Reality:** [Correct understanding]

## Trade-offs and Alternatives

Like everything in software engineering, this approach has trade-offs:

**Advantages:**
- [Pro 1]
- [Pro 2]

**Disadvantages:**
- [Con 1]
- [Con 2]

**Alternatives:**
- [Alternative approach 1]: [When to use]
- [Alternative approach 2]: [When to use]

## Conclusion

[Recap the key insights]
[Provide actionable takeaway]

## Further Reading

- [Resource 1](URL) - [Why it's valuable]
- [Resource 2](URL) - [Why it's valuable]

---

*Written by [Your Name] on {date}*
"""


COMPARISON_TEMPLATE = """# {title}

{hook_placeholder}

## Quick Comparison

| Feature | [Option A] | [Option B] |
|---------|-----------|-----------|
| **Best for** | [Use case] | [Use case] |
| **Learning curve** | [Assessment] | [Assessment] |
| **Performance** | [Assessment] | [Assessment] |
| **Ecosystem** | [Assessment] | [Assessment] |
| **Popularity** | [Stats] | [Stats] |

## Introduction

[Explain the dilemma developers face]
[Why choosing between these matters]

## What Are We Comparing?

### [Option A]

[Brief description and background]

**Key characteristics:**
- [Trait 1]
- [Trait 2]

### [Option B]

[Brief description and background]

**Key characteristics:**
- [Trait 1]
- [Trait 2]

## Detailed Comparison

### Performance

**[Option A]:**
[Performance characteristics with data]

**[Option B]:**
[Performance characteristics with data]

**Winner:** [A/B/Tie] - [Brief reasoning]

### Developer Experience

**[Option A]:**
[Description of DX]

```language
// Example code
```

**[Option B]:**
[Description of DX]

```language
// Example code
```

**Winner:** [A/B/Tie] - [Brief reasoning]

### Ecosystem & Community

**[Option A]:**
- [Package/plugin availability]
- [Community size]
- [Corporate backing]

**[Option B]:**
- [Package/plugin availability]
- [Community size]
- [Corporate backing]

**Winner:** [A/B/Tie] - [Brief reasoning]

### Learning Curve

**[Option A]:**
[Time to productivity, documentation quality]

**[Option B]:**
[Time to productivity, documentation quality]

**Winner:** [A/B/Tie] - [Brief reasoning]

### Use Case Fit

**[Option A] excels at:**
- [Specific use case 1]
- [Specific use case 2]

**[Option B] excels at:**
- [Specific use case 1]
- [Specific use case 2]

## Real-World Examples

### Building [Common project type]

**With [Option A]:**
```language
// Implementation
```

**With [Option B]:**
```language
// Implementation
```

[Compare the approaches]

## Decision Framework

### Choose [Option A] if:
- [Criterion 1]
- [Criterion 2]
- [Criterion 3]

### Choose [Option B] if:
- [Criterion 1]
- [Criterion 2]
- [Criterion 3]

### Consider both if:
- [Scenario where either works]

## My Recommendation

[Your informed opinion based on experience]

**For most projects:** [Recommendation]
**For [specific scenario]:** [Alternative recommendation]

## Migration Considerations

If switching between them:
- [Migration consideration 1]
- [Migration consideration 2]

## Conclusion

[Summary of key differences]
[Final guidance on choosing]

**What's your experience?** Share your thoughts in the comments!

---

*Written by [Your Name] on {date}*
"""


PROBLEM_SOLUTION_TEMPLATE = """# {title}

{hook_placeholder}

## The Problem

[Describe the frustrating problem in detail]
[Make readers feel "yes, I've experienced this!"]

**You know you have this problem when:**
- [Symptom 1]
- [Symptom 2]
- [Symptom 3]

**Example scenario:**
[Describe a concrete situation where this occurs]

```language
// Code that demonstrates the problem
```

**What happens:**
```
[Error message or unexpected behavior]
```

## Why This Happens

[Explain the root cause]

The problem stems from [underlying cause]:

1. [Technical reason 1]
2. [Technical reason 2]
3. [Technical reason 3]

**Understanding the mechanics:**

[Deeper explanation with diagrams if helpful]

```language
// Code showing why the problem occurs
```

## The Solution

### Quick Fix (Temporary)

If you need an immediate solution:

```language
// Quick workaround code
```

**Why this works:**
[Brief explanation]

**Limitations:**
- [What this doesn't address]
- [When this isn't sufficient]

### Proper Solution (Recommended)

Here's how to fix this correctly:

#### Step 1: [First fix step]

[Explanation]

```language
// Implementation code
```

#### Step 2: [Second fix step]

[Explanation]

```language
// Implementation code
```

#### Step 3: [Third fix step]

[Explanation]

```language
// Implementation code
```

### Complete Fixed Code

```language
// Full working solution
```

**Verification:**
```bash
# How to test the fix
```

**Expected result:**
```
[Correct output]
```

## How to Prevent This

Now that it's fixed, let's prevent it from happening again:

### Best Practice 1: [Practice name]

[Explanation of preventive measure]

```language
// Example of good practice
```

### Best Practice 2: [Practice name]

[Another preventive measure]

### Monitoring & Detection

Set up alerts to catch this early:

```language
// Monitoring code or configuration
```

## Real-World Case Study

[Share a story of encountering and fixing this problem]

**The situation:**
[Context]

**What went wrong:**
[Description]

**The fix:**
[Solution applied]

**Lessons learned:**
- [Lesson 1]
- [Lesson 2]

## Related Issues

This problem is related to other common issues:

- **[Related problem 1]:** [Brief description and link]
- **[Related problem 2]:** [Brief description and link]

## Conclusion

[Recap the problem and solution]
[Reinforce the key preventive measures]

**Have you encountered this issue?** Share your experience in the comments!

## Additional Resources

- [Official docs](URL)
- [Related debugging guide](URL)
- [Tool that helps](URL)

---

*Written by [Your Name] on {date}*
"""


GUIDE_TEMPLATE = """# {title}: A Comprehensive Guide

{hook_placeholder}

## What This Guide Covers

This comprehensive guide will teach you:
- [Main topic 1]
- [Main topic 2]
- [Main topic 3]
- [Main topic 4]

**Who this is for:** [Target audience]
**Time to complete:** [Estimate]
**Prerequisites:** [Required knowledge]

## Table of Contents

1. [Section 1](#section-1)
2. [Section 2](#section-2)
3. [Section 3](#section-3)
4. [Section 4](#section-4)

---

## Introduction

[Comprehensive overview of the topic]
[Why this matters]
[What readers will accomplish]

## Part 1: The Fundamentals

### Understanding the Basics

[Foundation concepts]

**Key concepts:**
- **[Concept 1]:** [Definition and importance]
- **[Concept 2]:** [Definition and importance]
- **[Concept 3]:** [Definition and importance]

### Your First Example

Let's start with a simple example:

```language
// Basic example code with thorough comments
```

[Detailed walkthrough of the example]

### Core Principles

The foundation of [topic] rests on these principles:

1. **[Principle 1]:** [Explanation]
2. **[Principle 2]:** [Explanation]
3. **[Principle 3]:** [Explanation]

## Part 2: Intermediate Concepts

### [Intermediate topic 1]

[Explanation building on fundamentals]

```language
// More complex example
```

### [Intermediate topic 2]

[Further development]

### Common Patterns

These patterns appear frequently:

#### Pattern 1: [Name]

**When to use:**
[Scenario]

**Implementation:**
```language
// Code example
```

#### Pattern 2: [Name]

**When to use:**
[Scenario]

**Implementation:**
```language
// Code example
```

## Part 3: Advanced Techniques

### [Advanced topic 1]

[In-depth explanation]

**Performance considerations:**
[Discussion of trade-offs]

### [Advanced topic 2]

[Complex scenario handling]

### Real-World Applications

#### Use Case 1: [Scenario]

[Detailed walkthrough]

```language
// Production-ready code
```

#### Use Case 2: [Scenario]

[Another practical application]

## Part 4: Best Practices

### Dos and Don'ts

✅ **DO:**
- [Best practice 1]
- [Best practice 2]
- [Best practice 3]

❌ **DON'T:**
- [Anti-pattern 1]
- [Anti-pattern 2]
- [Anti-pattern 3]

### Code Organization

[Guidelines for structuring code]

### Testing Strategies

[How to test this effectively]

```language
// Test examples
```

### Performance Optimization

[Optimization techniques]

**Benchmarks:**
```
[Performance data]
```

## Part 5: Troubleshooting

### Common Problems

#### Problem 1: [Issue]

**Symptoms:**
[What you see]

**Cause:**
[Why it happens]

**Solution:**
[How to fix]

#### Problem 2: [Issue]

[Same structure]

### Debugging Techniques

[Effective debugging approaches]

### Getting Help

When you're stuck:
- [Resource 1]
- [Resource 2]
- [Community forum]

## Tools and Resources

### Essential Tools

- **[Tool 1]:** [What it does and why use it]
- **[Tool 2]:** [What it does and why use it]

### Libraries and Frameworks

- **[Library 1]:** [Use case]
- **[Library 2]:** [Use case]

### Learning Resources

**Documentation:**
- [Official docs](URL)
- [Additional docs](URL)

**Tutorials:**
- [Tutorial 1](URL) - [What it covers]
- [Tutorial 2](URL) - [What it covers]

**Books:**
- [Book 1] by [Author] - [Description]

**Communities:**
- [Forum/Discord/etc](URL)

## What's Next?

After mastering this guide:

1. **Build a project:** [Suggestion]
2. **Explore advanced topics:** [Next concepts]
3. **Contribute back:** [How to help others]

## Conclusion

[Comprehensive summary]
[Encouragement and next steps]

## Glossary

- **[Term 1]:** [Definition]
- **[Term 2]:** [Definition]
- **[Term 3]:** [Definition]

## Frequently Asked Questions

**Q: [Common question]**
A: [Answer]

**Q: [Common question]**
A: [Answer]

---

*Written by [Your Name] on {date}*
*Last updated: {date}*
"""


TEMPLATES = {
    'tutorial': TUTORIAL_TEMPLATE,
    'deepdive': DEEPDIVE_TEMPLATE,
    'comparison': COMPARISON_TEMPLATE,
    'problem': PROBLEM_SOLUTION_TEMPLATE,
    'guide': GUIDE_TEMPLATE,
}


def generate_template(template_type: str, title: str, output_file: str = None) -> None:
    """Generate a blog post template."""
    if template_type not in TEMPLATES:
        print(f"Error: Unknown template type '{template_type}'")
        print(f"Available types: {', '.join(TEMPLATES.keys())}")
        sys.exit(1)

    # Generate hook placeholder based on type
    hooks = {
        'tutorial': "[Start with a problem this tutorial solves or an exciting result readers will achieve]",
        'deepdive': "[Start with an intriguing question or surprising fact about the topic]",
        'comparison': "[Describe the dilemma: when developers face choice between these options]",
        'problem': "[Describe the frustrating problem that brings readers here]",
        'guide': "[Explain why this comprehensive guide exists and what gap it fills]",
    }

    # Fill in the template
    content = TEMPLATES[template_type].format(
        title=title,
        hook_placeholder=hooks[template_type],
        date=date.today().isoformat()
    )

    # Determine output file
    if output_file is None:
        # Generate filename from title
        filename = title.lower()
        filename = filename.replace(' ', '-')
        filename = ''.join(c for c in filename if c.isalnum() or c == '-')
        filename = filename.strip('-')
        output_file = f"{filename}.md"

    # Write the file
    output_path = Path(output_file)
    output_path.write_text(content)

    print(f"✅ Created {template_type} template: {output_file}")
    print(f"\n📝 Next steps:")
    print(f"   1. Open {output_file} in your editor")
    print(f"   2. Replace placeholders with your content")
    print(f"   3. Add your code examples and explanations")
    print(f"   4. Test all code examples")
    print(f"   5. Run ./readability-analyzer.py {output_file}")
    print(f"\n💡 Tip: Search for '[' to find all placeholders to fill in")


def main():
    """Main entry point."""
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    template_type = sys.argv[1].lower()
    title = sys.argv[2]
    output_file = sys.argv[3] if len(sys.argv) > 3 else None

    generate_template(template_type, title, output_file)


if __name__ == "__main__":
    main()
