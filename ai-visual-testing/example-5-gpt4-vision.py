#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "openai>=1.54.0",  # OpenAI API client
#     "playwright>=1.48.0",  # Browser automation
# ]
# ///
"""
Example 5: GPT-4 Vision API for Visual Testing

This script demonstrates how to use OpenAI's GPT-4 Vision (GPT-4o) to analyze
screenshots and perform visual testing with AI-powered analysis.

Setup:
1. Set your API key: export OPENAI_API_KEY=your-key-here
2. Run: uv run example-5-gpt4-vision.py

Key benefits:
- Multimodal understanding (visual + textual context)
- Can identify UI/UX issues, bugs, and inconsistencies
- Provides actionable feedback and suggestions
"""

import openai
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


def encode_image_to_base64(image_path: str) -> str:
    """Encode image to base64 for OpenAI API."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def analyze_with_gpt4_vision(
    image_path: str,
    prompt: str,
    model: str = "gpt-4o"
) -> str:
    """Analyze screenshot using GPT-4 Vision."""
    client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    # Encode image
    base64_image = encode_image_to_base64(image_path)

    # Create API request
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}",
                            "detail": "high"  # "low", "high", or "auto"
                        }
                    }
                ],
            }
        ],
        max_tokens=4096,
        temperature=0.1  # Lower temperature for more consistent analysis
    )

    return response.choices[0].message.content


def test_ui_element_detection(url: str):
    """Detect and validate UI elements."""
    print(f"Testing UI elements on {url}...")

    screenshot_path = capture_screenshot(url)

    prompt = """
    Analyze this UI screenshot and identify all major UI elements.
    For each element, provide:
    1. Element type (button, input, navigation, etc.)
    2. Approximate position
    3. Whether it appears functional and properly styled
    4. Any issues or concerns

    Also identify:
    - Missing critical elements (e.g., no navigation, no CTA)
    - Poorly placed elements
    - Accessibility concerns
    """

    result = analyze_with_gpt4_vision(screenshot_path, prompt)
    print("\n=== UI Element Analysis ===")
    print(result)


def test_visual_regression(baseline_path: str, current_path: str):
    """Compare baseline and current screenshots to detect regressions."""
    client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    baseline_b64 = encode_image_to_base64(baseline_path)
    current_b64 = encode_image_to_base64(current_path)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Here is the baseline screenshot (expected UI):"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{baseline_b64}",
                            "detail": "high"
                        }
                    },
                    {
                        "type": "text",
                        "text": "Here is the current screenshot:"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{current_b64}",
                            "detail": "high"
                        }
                    },
                    {
                        "type": "text",
                        "text": """
                        Compare these screenshots and identify:
                        1. Visual regressions (broken layouts, missing elements)
                        2. Intentional improvements vs. unintended changes
                        3. Critical issues that should block deployment
                        4. Minor cosmetic differences

                        Categorize findings as: CRITICAL, MAJOR, MINOR, or INFORMATIONAL.
                        """
                    }
                ],
            }
        ],
        max_tokens=4096,
        temperature=0.1
    )

    print("\n=== Visual Regression Report ===")
    print(response.choices[0].message.content)


def test_accessibility_issues(url: str):
    """Test for accessibility issues."""
    screenshot_path = capture_screenshot(url)

    prompt = """
    Analyze this UI for accessibility issues:

    Visual Accessibility:
    1. Color contrast ratios (text vs background)
    2. Text size and readability
    3. Use of color alone to convey information
    4. Focus indicators visibility
    5. Touch target sizes (for mobile)

    Layout Accessibility:
    1. Logical visual hierarchy
    2. Clear heading structure
    3. Form label visibility
    4. Button and link clarity

    Provide specific issues found with:
    - Issue description
    - WCAG guideline violated
    - Severity (A, AA, AAA)
    - Suggested fix
    """

    result = analyze_with_gpt4_vision(screenshot_path, prompt)
    print("\n=== Accessibility Analysis ===")
    print(result)


def test_responsive_breakpoints(url: str):
    """Test UI at different responsive breakpoints."""
    breakpoints = {
        "mobile_small": (320, 568),
        "mobile_large": (414, 896),
        "tablet": (768, 1024),
        "desktop": (1440, 900),
        "desktop_large": (1920, 1080)
    }

    with sync_playwright() as p:
        browser = p.chromium.launch()

        for name, (width, height) in breakpoints.items():
            page = browser.new_page(viewport={"width": width, "height": height})
            page.goto(url)
            page.wait_for_load_state('networkidle')

            screenshot_path = f"screenshot_{name}.png"
            page.screenshot(path=screenshot_path, full_page=True)

            prompt = f"""
            This is a screenshot at {width}x{height} ({name}).

            Check for responsive design issues:
            1. Proper content scaling
            2. No horizontal scrolling (unless intended)
            3. Readable text sizes
            4. Properly sized interactive elements
            5. Efficient use of screen space
            6. No overlapping or cut-off content

            Rate the responsive implementation: Excellent / Good / Needs Improvement / Poor
            Provide specific issues and recommendations.
            """

            result = analyze_with_gpt4_vision(screenshot_path, prompt)
            print(f"\n=== {name} ({width}x{height}) ===")
            print(result)

        browser.close()


def test_design_consistency(url_list: list[str]):
    """Test design consistency across multiple pages."""
    client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    screenshots = []
    with sync_playwright() as p:
        browser = p.chromium.launch()

        for url in url_list:
            page = browser.new_page()
            page.goto(url)
            page.wait_for_load_state('networkidle')

            screenshot_path = f"screenshot_{url.split('/')[-1]}.png"
            page.screenshot(path=screenshot_path, full_page=True)
            screenshots.append(screenshot_path)

        browser.close()

    # Prepare message with all screenshots
    content = [
        {
            "type": "text",
            "text": "I'm showing you screenshots from different pages of the same application. Analyze them for design consistency:"
        }
    ]

    for i, screenshot in enumerate(screenshots, 1):
        content.append({
            "type": "text",
            "text": f"\nPage {i} ({url_list[i-1]}):"
        })
        content.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:image/png;base64,{encode_image_to_base64(screenshot)}",
                "detail": "high"
            }
        })

    content.append({
        "type": "text",
        "text": """
        Check for consistency in:
        1. Color palette usage
        2. Typography (fonts, sizes, weights)
        3. Spacing and padding patterns
        4. Button and form styles
        5. Navigation patterns
        6. Overall visual language

        Identify inconsistencies and suggest improvements for better design cohesion.
        """
    })

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": content}],
        max_tokens=4096,
        temperature=0.1
    )

    print("\n=== Design Consistency Report ===")
    print(response.choices[0].message.content)


def test_ui_state_validation(url: str):
    """Test different UI states (hover, focus, error, etc.)."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)

        # Test form validation states
        page.fill("#email", "invalid-email")
        page.click("#submit")
        page.wait_for_selector(".error-message", timeout=5000)

        error_screenshot = "screenshot_error_state.png"
        page.screenshot(path=error_screenshot)

        prompt = """
        This screenshot shows a form in an error state.
        Evaluate:
        1. Clarity of error messages
        2. Visual prominence of errors (color, icons, placement)
        3. User guidance for fixing errors
        4. Accessibility of error states
        5. Overall error UX

        Provide specific feedback and recommendations.
        """

        result = analyze_with_gpt4_vision(error_screenshot, prompt)
        print("\n=== Error State Analysis ===")
        print(result)

        browser.close()


if __name__ == "__main__":
    print("GPT-4 Vision API Visual Testing Examples\n")

    # Example 1: UI element detection
    test_ui_element_detection("https://example.com")

    # Example 2: Accessibility testing
    # test_accessibility_issues("https://example.com")

    # Example 3: Responsive design testing
    # test_responsive_breakpoints("https://example.com")

    # Example 4: Visual regression testing
    # test_visual_regression("baseline.png", "current.png")

    # Example 5: Design consistency across pages
    # pages = [
    #     "https://example.com",
    #     "https://example.com/about",
    #     "https://example.com/contact"
    # ]
    # test_design_consistency(pages)
