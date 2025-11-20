#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "playwright>=1.48.0",  # Browser automation
#     "anthropic>=0.39.0",   # Claude API for AI analysis
#     "pillow>=11.0.0",      # Image processing
# ]
# ///
"""
Example 8: Chrome DevTools + AI Vision Hybrid Approach

This example demonstrates combining Chrome DevTools capabilities with
AI vision analysis for comprehensive visual testing.

Workflow:
1. Use Chrome DevTools for precise, free checks (Lighthouse, contrast)
2. Use AI vision only when DevTools finds issues or for semantic analysis
3. Optimize costs by using free tools first

Setup:
1. Set your API key: export ANTHROPIC_API_KEY=your-key-here
2. Install Playwright: playwright install chromium
3. Run: uv run example-8-chrome-ai-hybrid.py
"""

import anthropic
import base64
import json
import os
from playwright.sync_api import sync_playwright
from PIL import Image


class ChromeDevToolsAnalyzer:
    """Analyzer using Chrome DevTools capabilities."""

    def __init__(self):
        self.results = {}

    def check_contrast(self, page):
        """Check color contrast using Chrome DevTools."""
        print("📊 Running Chrome DevTools contrast check...")

        # Inject contrast checking script
        contrast_issues = page.evaluate("""
            () => {
                const issues = [];

                function getContrastRatio(fg, bg) {
                    const getLuminance = (r, g, b) => {
                        const [rs, gs, bs] = [r, g, b].map(c => {
                            c = c / 255;
                            return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
                        });
                        return 0.2126 * rs + 0.7152 * gs + 0.0722 * bs;
                    };

                    const l1 = getLuminance(fg.r, fg.g, fg.b);
                    const l2 = getLuminance(bg.r, bg.g, bg.b);
                    return (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);
                }

                function parseColor(colorStr) {
                    const canvas = document.createElement('canvas');
                    canvas.width = canvas.height = 1;
                    const ctx = canvas.getContext('2d');
                    ctx.fillStyle = colorStr;
                    ctx.fillRect(0, 0, 1, 1);
                    const [r, g, b] = ctx.getImageData(0, 0, 1, 1).data;
                    return { r, g, b };
                }

                const textElements = document.querySelectorAll('p, h1, h2, h3, h4, h5, h6, span, a, button');

                textElements.forEach(element => {
                    const styles = window.getComputedStyle(element);
                    const color = parseColor(styles.color);
                    const bgColor = parseColor(styles.backgroundColor);
                    const ratio = getContrastRatio(color, bgColor);
                    const fontSize = parseFloat(styles.fontSize);
                    const minRatio = fontSize >= 18 ? 3 : 4.5;

                    if (ratio < minRatio) {
                        issues.push({
                            selector: element.tagName.toLowerCase(),
                            text: element.textContent.substring(0, 50),
                            ratio: ratio.toFixed(2),
                            required: minRatio
                        });
                    }
                });

                return issues;
            }
        """)

        self.results['contrast'] = contrast_issues

        if len(contrast_issues) == 0:
            print("  ✓ No contrast issues found")
        else:
            print(f"  ⚠️  Found {len(contrast_issues)} contrast issues")

        return contrast_issues

    def analyze_performance(self, cdp_session):
        """Get performance metrics via CDP."""
        print("⚡ Analyzing performance metrics...")

        metrics = cdp_session.send('Performance.getMetrics')

        key_metrics = {
            'LayoutDuration': 0,
            'RecalcStyleDuration': 0,
            'ScriptDuration': 0
        }

        for metric in metrics['metrics']:
            if metric['name'] in key_metrics:
                key_metrics[metric['name']] = metric['value']

        self.results['performance'] = key_metrics

        print(f"  Layout: {key_metrics['LayoutDuration']:.2f}ms")
        print(f"  Style: {key_metrics['RecalcStyleDuration']:.2f}ms")
        print(f"  Script: {key_metrics['ScriptDuration']:.2f}ms")

        return key_metrics

    def capture_vision_deficiency_screenshots(self, page, cdp_session, base_path="screenshot"):
        """Capture screenshots with vision deficiency simulations."""
        print("👁️  Capturing vision deficiency screenshots...")

        vision_types = {
            'none': 'Normal vision',
            'deuteranopia': 'Green-blind',
            'protanopia': 'Red-blind',
            'tritanopia': 'Blue-blind'
        }

        screenshots = {}

        for vision_type, description in vision_types.items():
            cdp_session.send('Emulation.setEmulatedVisionDeficiency', {
                'type': vision_type
            })

            filename = f"{base_path}_{vision_type}.png"
            page.screenshot(path=filename)
            screenshots[vision_type] = filename

            print(f"  ✓ {description}: {filename}")

        # Reset to normal
        cdp_session.send('Emulation.setEmulatedVisionDeficiency', {'type': 'none'})

        return screenshots


class AIVisualAnalyzer:
    """Analyzer using Claude Vision API."""

    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        self.client = anthropic.Anthropic(api_key=self.api_key) if self.api_key else None

    def analyze_contrast_issues(self, screenshot_path, contrast_issues):
        """Use AI to provide actionable fixes for contrast issues."""
        if not self.client:
            print("⚠️  Skipping AI analysis (no API key)")
            return None

        print("\n🤖 Analyzing contrast issues with Claude Vision...")

        with open(screenshot_path, "rb") as f:
            image_data = base64.b64encode(f.read()).decode("utf-8")

        # Create focused prompt based on DevTools findings
        issue_list = "\n".join([
            f"- {issue['selector']}: {issue['ratio']}:1 (needs {issue['required']}:1)"
            for issue in contrast_issues[:5]
        ])

        prompt = f"""
        Chrome DevTools detected {len(contrast_issues)} color contrast issues:

        {issue_list}

        Analyze this screenshot and provide:
        1. Which contrast issues are most critical for users
        2. Specific color suggestions to fix each issue
        3. Whether there are accessibility issues DevTools might have missed
        4. Overall accessibility rating (1-10)

        Be specific and actionable.
        """

        message = self.client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=2048,
            messages=[{
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/png",
                            "data": image_data,
                        },
                    },
                    {"type": "text", "text": prompt}
                ],
            }],
        )

        analysis = message.content[0].text
        print("\n" + analysis)
        return analysis

    def analyze_vision_deficiency(self, screenshots):
        """Analyze if UI is usable across vision deficiencies."""
        if not self.client or len(screenshots) < 2:
            return None

        print("\n🤖 Analyzing vision deficiency accessibility with Claude...")

        # Compare normal vs deuteranopia (most common color blindness)
        normal_path = screenshots.get('none')
        colorblind_path = screenshots.get('deuteranopia')

        if not normal_path or not colorblind_path:
            return None

        with open(normal_path, "rb") as f:
            normal_data = base64.b64encode(f.read()).decode("utf-8")

        with open(colorblind_path, "rb") as f:
            colorblind_data = base64.b64encode(f.read()).decode("utf-8")

        message = self.client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=2048,
            messages=[{
                "role": "user",
                "content": [
                    {"type": "text", "text": "Normal vision:"},
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/png",
                            "data": normal_data,
                        },
                    },
                    {"type": "text", "text": "Deuteranopia (green-blind) vision:"},
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/png",
                            "data": colorblind_data,
                        },
                    },
                    {
                        "type": "text",
                        "text": """
                        Compare these screenshots and identify:
                        1. UI elements that lose meaning for colorblind users
                        2. Information conveyed only by color
                        3. Whether critical actions are still distinguishable
                        4. Recommendations for improvement

                        Rate the colorblind accessibility (1-10).
                        """
                    }
                ],
            }],
        )

        analysis = message.content[0].text
        print("\n" + analysis)
        return analysis


def hybrid_visual_testing_workflow(url: str):
    """
    Complete hybrid workflow: Chrome DevTools → AI Vision
    Uses free tools first, AI only when needed.
    """
    print("="*60)
    print("HYBRID VISUAL TESTING WORKFLOW")
    print("="*60)
    print(f"Testing: {url}\n")

    # Initialize analyzers
    chrome_analyzer = ChromeDevToolsAnalyzer()
    ai_analyzer = AIVisualAnalyzer()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Get CDP session
        cdp_session = page.context.new_cdp_session(page)

        # Enable performance tracking
        cdp_session.send('Performance.enable')

        # Navigate
        print(f"🌐 Loading {url}...")
        page.goto(url)
        page.wait_for_load_state('networkidle')

        print("\n" + "="*60)
        print("PHASE 1: Chrome DevTools Analysis (Free)")
        print("="*60 + "\n")

        # Step 1: Performance analysis
        performance = chrome_analyzer.analyze_performance(cdp_session)

        # Step 2: Contrast checking
        contrast_issues = chrome_analyzer.check_contrast(page)

        # Step 3: Take baseline screenshot
        baseline_path = "hybrid_baseline.png"
        page.screenshot(path=baseline_path)
        print(f"\n📸 Baseline screenshot: {baseline_path}")

        # Step 4: Vision deficiency screenshots
        vision_screenshots = chrome_analyzer.capture_vision_deficiency_screenshots(
            page, cdp_session, "hybrid_vision"
        )

        # Determine if AI analysis is needed
        needs_ai_analysis = (
            len(contrast_issues) > 0 or  # Found accessibility issues
            performance['LayoutDuration'] > 500  # Slow rendering
        )

        if needs_ai_analysis:
            print("\n" + "="*60)
            print("PHASE 2: AI Vision Analysis (Targeted)")
            print("="*60)

            # Only use AI for specific issues found by DevTools
            if len(contrast_issues) > 0:
                ai_analyzer.analyze_contrast_issues(baseline_path, contrast_issues)

            # Analyze vision deficiency accessibility
            ai_analyzer.analyze_vision_deficiency(vision_screenshots)

        else:
            print("\n" + "="*60)
            print("✓ All Chrome DevTools checks passed - No AI analysis needed")
            print("="*60)
            print("\nCost savings: $0 (AI API not called)")

        # Generate report
        print("\n" + "="*60)
        print("FINAL REPORT")
        print("="*60)

        report = {
            "url": url,
            "timestamp": "2025-11-20",
            "chrome_devtools": {
                "performance": performance,
                "contrast_issues": len(contrast_issues),
                "vision_screenshots": list(vision_screenshots.keys())
            },
            "ai_analysis_triggered": needs_ai_analysis,
            "cost_optimization": "AI used only when DevTools found issues"
        }

        print(json.dumps(report, indent=2))

        browser.close()


def compare_workflows():
    """
    Compare costs: All-AI vs. Hybrid approach
    """
    print("\n" + "="*60)
    print("COST COMPARISON")
    print("="*60 + "\n")

    print("All-AI Approach:")
    print("  - AI analysis for every screenshot: ~$0.01-0.05 per image")
    print("  - 100 tests/day × 3 screenshots = 300 images = $3-15/day")
    print("  - Monthly cost: $90-450\n")

    print("Hybrid Approach (Chrome DevTools + AI):")
    print("  - Chrome DevTools checks: $0 (free)")
    print("  - AI only when issues found: ~20% of tests")
    print("  - 100 tests/day × 20% × 3 screenshots = 60 images = $0.60-3/day")
    print("  - Monthly cost: $18-90")
    print("\n  💰 Savings: 70-80% reduction in AI costs\n")


if __name__ == "__main__":
    # Example usage
    print("Chrome DevTools + AI Vision Hybrid Testing\n")

    # Run hybrid workflow
    hybrid_visual_testing_workflow("https://example.com")

    # Show cost comparison
    compare_workflows()

    print("\n" + "="*60)
    print("Key Takeaways:")
    print("="*60)
    print("1. Chrome DevTools provides free, precise accessibility checks")
    print("2. Use AI vision only for semantic analysis and complex issues")
    print("3. 70-80% cost reduction vs. all-AI approach")
    print("4. Better coverage: DevTools precision + AI understanding")
    print("="*60)
