#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "textstat>=0.7.3",  # Readability metrics
#     "markdown>=3.5.0",  # Parse markdown
# ]
# ///
"""
Analyze the readability of technical writing.

This script calculates various readability metrics for markdown files
to help ensure your technical writing is accessible to your target audience.

Usage:
    ./readability-analyzer.py <file.md>
    ./readability-analyzer.py blog-post.md
"""

import sys
import re
from pathlib import Path
import textstat
from markdown import markdown
from html import unescape


def strip_markdown(text: str) -> str:
    """Convert markdown to plain text for analysis."""
    # Convert markdown to HTML
    html = markdown(text)

    # Remove HTML tags
    text = re.sub('<[^<]+?>', '', html)

    # Unescape HTML entities
    text = unescape(text)

    # Remove code blocks (they skew readability)
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    text = re.sub(r'`[^`]+`', '', text)

    return text.strip()


def count_code_blocks(text: str) -> dict:
    """Count code blocks and inline code."""
    fenced_blocks = len(re.findall(r'```.*?```', text, re.DOTALL))
    inline_code = len(re.findall(r'`[^`]+`', text))

    return {
        'code_blocks': fenced_blocks,
        'inline_code': inline_code
    }


def analyze_structure(text: str) -> dict:
    """Analyze document structure."""
    lines = text.split('\n')

    headings = {
        'h1': len([l for l in lines if l.startswith('# ')]),
        'h2': len([l for l in lines if l.startswith('## ')]),
        'h3': len([l for l in lines if l.startswith('### ')]),
        'h4': len([l for l in lines if l.startswith('#### ')])
    }

    # Count lists
    bullet_lists = len([l for l in lines if re.match(r'^\s*[-*+]\s', l)])
    numbered_lists = len([l for l in lines if re.match(r'^\s*\d+\.\s', l)])

    # Count links and images
    links = len(re.findall(r'\[([^\]]+)\]\(([^\)]+)\)', text))
    images = len(re.findall(r'!\[([^\]]*)\]\(([^\)]+)\)', text))

    return {
        'headings': headings,
        'bullet_list_items': bullet_lists,
        'numbered_list_items': numbered_lists,
        'links': links,
        'images': images
    }


def analyze_readability(file_path: str) -> None:
    """Analyze a markdown file's readability."""
    path = Path(file_path)

    if not path.exists():
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    # Read the file
    content = path.read_text()

    # Get structure info
    structure = analyze_structure(content)
    code_info = count_code_blocks(content)

    # Strip markdown for text analysis
    plain_text = strip_markdown(content)

    if not plain_text:
        print("Error: No readable text found in file.")
        sys.exit(1)

    # Calculate metrics
    flesch_reading = textstat.flesch_reading_ease(plain_text)
    flesch_grade = textstat.flesch_kincaid_grade(plain_text)
    smog = textstat.smog_index(plain_text)

    word_count = textstat.lexicon_count(plain_text)
    sentence_count = textstat.sentence_count(plain_text)

    # Print results
    print(f"\n{'='*60}")
    print(f"READABILITY ANALYSIS: {path.name}")
    print(f"{'='*60}\n")

    # Basic stats
    print("📊 BASIC STATISTICS")
    print(f"   Words: {word_count:,}")
    print(f"   Sentences: {sentence_count}")
    print(f"   Avg words per sentence: {word_count/sentence_count:.1f}")
    print(f"   Reading time: ~{word_count // 200} minutes\n")

    # Readability scores
    print("📖 READABILITY SCORES")
    print(f"   Flesch Reading Ease: {flesch_reading:.1f}")

    if flesch_reading >= 90:
        level = "Very Easy (5th grade)"
        emoji = "🟢"
    elif flesch_reading >= 80:
        level = "Easy (6th grade)"
        emoji = "🟢"
    elif flesch_reading >= 70:
        level = "Fairly Easy (7th grade)"
        emoji = "🟢"
    elif flesch_reading >= 60:
        level = "Standard (8th-9th grade)"
        emoji = "🟡"
    elif flesch_reading >= 50:
        level = "Fairly Difficult (10th-12th grade)"
        emoji = "🟡"
    elif flesch_reading >= 30:
        level = "Difficult (College)"
        emoji = "🟠"
    else:
        level = "Very Difficult (College graduate)"
        emoji = "🔴"

    print(f"   {emoji} {level}")
    print(f"   Flesch-Kincaid Grade: {flesch_grade:.1f}")
    print(f"   SMOG Index: {smog:.1f}\n")

    # Structure analysis
    print("🏗️  DOCUMENT STRUCTURE")
    print(f"   H1 headings: {structure['headings']['h1']}")
    print(f"   H2 headings: {structure['headings']['h2']}")
    print(f"   H3 headings: {structure['headings']['h3']}")
    print(f"   H4 headings: {structure['headings']['h4']}")
    print(f"   Bullet points: {structure['bullet_list_items']}")
    print(f"   Numbered items: {structure['numbered_list_items']}")
    print(f"   Links: {structure['links']}")
    print(f"   Images: {structure['images']}\n")

    # Code analysis
    print("💻 CODE ELEMENTS")
    print(f"   Code blocks: {code_info['code_blocks']}")
    print(f"   Inline code: {code_info['inline_code']}\n")

    # Recommendations
    print("💡 RECOMMENDATIONS")

    recommendations = []

    # Check for multiple H1s
    if structure['headings']['h1'] > 1:
        recommendations.append("⚠️  Use only one H1 heading (article title)")

    # Check for heading hierarchy
    if structure['headings']['h2'] == 0 and structure['headings']['h3'] > 0:
        recommendations.append("⚠️  Don't skip heading levels (use H2 before H3)")

    # Check readability
    if flesch_reading < 50:
        recommendations.append("📝 Consider simplifying sentences for better readability")

    # Check average sentence length
    avg_words = word_count / sentence_count
    if avg_words > 25:
        recommendations.append(f"📝 Average sentence length ({avg_words:.1f} words) is high - aim for 15-20")

    # Check for code examples
    if code_info['code_blocks'] == 0 and 'code' in content.lower():
        recommendations.append("💻 Consider adding code examples to illustrate concepts")

    # Check for images
    if structure['images'] == 0 and word_count > 1000:
        recommendations.append("🖼️  Long articles benefit from diagrams or screenshots")

    # Check for lists
    if structure['bullet_list_items'] + structure['numbered_list_items'] == 0:
        recommendations.append("📋 Use lists to break up dense paragraphs")

    if recommendations:
        for rec in recommendations:
            print(f"   {rec}")
    else:
        print("   ✅ Looking good! No major issues detected.")

    print(f"\n{'='*60}\n")

    # Target audience guide
    print("🎯 TARGET AUDIENCE GUIDE")
    print("   Flesch Reading Ease Scores:")
    print("   90-100: Very Easy - General audience")
    print("   80-90:  Easy - 6th grade")
    print("   70-80:  Fairly Easy - 7th grade")
    print("   60-70:  Standard - 8th-9th grade (ideal for most technical blogs)")
    print("   50-60:  Fairly Difficult - High school")
    print("   30-50:  Difficult - College level")
    print("   0-30:   Very Difficult - Graduate level")
    print("\n   Technical blogs should aim for 50-70 for broad accessibility.")
    print(f"\n{'='*60}\n")


def main():
    """Main entry point."""
    if len(sys.argv) != 2:
        print("Usage: ./readability-analyzer.py <file.md>")
        sys.exit(1)

    analyze_readability(sys.argv[1])


if __name__ == "__main__":
    main()
