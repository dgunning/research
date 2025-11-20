#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "anthropic>=0.39.0",  # Claude API client
#     "playwright>=1.48.0",  # Browser automation
# ]
# ///
"""
Example 4: Claude Vision API for Visual Testing

This script demonstrates how to use Claude's vision capabilities to analyze
screenshots and perform intelligent visual testing. Claude can understand
UI elements, detect visual bugs, and provide detailed feedback.

Setup:
1. Set your API key: export ANTHROPIC_API_KEY=your-key-here
2. Run: uv run example-4-claude-vision.py

Key benefits:
- Semantic understanding of UI (not just pixel comparison)
- Natural language feedback on visual issues
- Can detect accessibility issues, layout problems, design inconsistencies
"""

import anthropic
import base64
import os
from playwright.sync_api import sync_playwright


def capture_screenshot(url: str, output_path: str = "screenshot.png") -> str:
    """Capture a screenshot of a URL using Playwright."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.wait_for_load_state('networkidle')
        page.screenshot(path=output_path, full_page=True)
        browser.close()
    return output_path


def encode_image(image_path: str) -> str:
    """Encode image to base64."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def analyze_screenshot_with_claude(
    image_path: str,
    prompt: str = "Analyze this UI screenshot and identify any visual bugs or issues."
) -> str:
    """Send screenshot to Claude for analysis."""
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    # Read image and encode
    with open(image_path, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode("utf-8")

    # Send to Claude
    message = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=4096,
        messages=[
            {
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
                    {
                        "type": "text",
                        "text": prompt
                    }
                ],
            }
        ],
    )

    return message.content[0].text


def test_ui_consistency(url: str):
    """Test UI for visual consistency."""
    print(f"Testing {url}...")

    # Capture screenshot
    screenshot_path = capture_screenshot(url)
    print(f"Screenshot captured: {screenshot_path}")

    # Analyze with Claude
    prompt = """
    Analyze this UI screenshot and check for:
    1. Visual inconsistencies (misaligned elements, spacing issues)
    2. Accessibility issues (contrast, text size, clickable areas)
    3. Responsive design problems
    4. Broken layouts or overlapping elements
    5. Missing or incorrectly rendered images
    6. Typography issues (inconsistent fonts, sizes)

    Provide a detailed report with severity levels (Critical, Major, Minor).
    """

    result = analyze_screenshot_with_claude(screenshot_path, prompt)
    print("\n=== Claude Visual Analysis ===")
    print(result)


def test_design_compliance(url: str, design_requirements: str):
    """Test if UI matches design requirements."""
    screenshot_path = capture_screenshot(url)

    prompt = f"""
    Design Requirements:
    {design_requirements}

    Analyze this UI screenshot and check if it complies with the above requirements.
    List any deviations or issues found.
    """

    result = analyze_screenshot_with_claude(screenshot_path, prompt)
    print("\n=== Design Compliance Report ===")
    print(result)


def compare_screenshots(screenshot1: str, screenshot2: str):
    """Compare two screenshots and identify differences."""
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    # Read both images
    with open(screenshot1, "rb") as f1:
        image1_data = base64.b64encode(f1.read()).decode("utf-8")

    with open(screenshot2, "rb") as f2:
        image2_data = base64.b64encode(f2.read()).decode("utf-8")

    # Send both to Claude
    message = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=4096,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "I'm going to show you two screenshots. The first is the baseline (expected), and the second is the current version."
                    },
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/png",
                            "data": image1_data,
                        },
                    },
                    {
                        "type": "text",
                        "text": "Now here's the current version:"
                    },
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/png",
                            "data": image2_data,
                        },
                    },
                    {
                        "type": "text",
                        "text": """
                        Compare these two screenshots and identify:
                        1. Visual differences (layout, colors, spacing, typography)
                        2. Missing or added elements
                        3. Changes in component positioning
                        4. Any regressions or improvements

                        Focus on meaningful differences, not minor rendering variations.
                        """
                    }
                ],
            }
        ],
    )

    print("\n=== Screenshot Comparison ===")
    print(message.content[0].text)


def test_cross_browser_consistency():
    """Test visual consistency across different browsers."""
    url = "https://example.com"
    browsers = ["chromium", "firefox", "webkit"]

    with sync_playwright() as p:
        screenshots = {}

        for browser_name in browsers:
            browser = getattr(p, browser_name).launch()
            page = browser.new_page()
            page.goto(url)
            page.wait_for_load_state('networkidle')

            screenshot_path = f"screenshot_{browser_name}.png"
            page.screenshot(path=screenshot_path, full_page=True)
            screenshots[browser_name] = screenshot_path

            browser.close()

    # Compare chromium (baseline) with others
    for browser_name in ["firefox", "webkit"]:
        print(f"\n=== Comparing Chromium vs {browser_name} ===")
        compare_screenshots(screenshots["chromium"], screenshots[browser_name])


def test_responsive_design(url: str):
    """Test responsive design across different viewport sizes."""
    viewports = {
        "mobile": {"width": 375, "height": 667},
        "tablet": {"width": 768, "height": 1024},
        "desktop": {"width": 1920, "height": 1080}
    }

    with sync_playwright() as p:
        browser = p.chromium.launch()

        for device, size in viewports.items():
            page = browser.new_page(viewport=size)
            page.goto(url)
            page.wait_for_load_state('networkidle')

            screenshot_path = f"screenshot_{device}.png"
            page.screenshot(path=screenshot_path, full_page=True)

            # Analyze each viewport
            prompt = f"""
            This is a screenshot at {device} size ({size['width']}x{size['height']}).
            Check for:
            1. Proper responsive behavior
            2. Readability of text
            3. Touch-friendly interactive elements (for mobile/tablet)
            4. Layout issues or overlapping elements
            5. Proper use of available space
            """

            result = analyze_screenshot_with_claude(screenshot_path, prompt)
            print(f"\n=== {device.capitalize()} Analysis ===")
            print(result)

        browser.close()


if __name__ == "__main__":
    # Example usage
    print("Claude Vision API Visual Testing Examples\n")

    # Example 1: Basic UI consistency test
    test_ui_consistency("https://example.com")

    # Example 2: Design compliance test
    # design_spec = """
    # - Primary color: #007bff
    # - Font: Inter, sans-serif
    # - Heading size: 32px
    # - Button border-radius: 8px
    # - Minimum contrast ratio: 4.5:1
    # """
    # test_design_compliance("https://example.com", design_spec)

    # Example 3: Responsive design test
    # test_responsive_design("https://example.com")

    # Example 4: Cross-browser consistency
    # test_cross_browser_consistency()
