#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "anthropic>=0.39.0",  # Claude API
#     "playwright>=1.48.0",  # Browser automation
#     "pillow>=11.0.0",  # Image processing
#     "imagehash>=4.3.1",  # Perceptual hashing
# ]
# ///
"""
Example 6: Hybrid AI Visual Testing Approach

This example combines multiple testing strategies:
1. Perceptual hashing for quick similarity checks
2. Pixel-by-pixel comparison for precise matching
3. Claude Vision API for semantic analysis

This hybrid approach provides:
- Fast initial screening (perceptual hash)
- Precise validation (pixel comparison)
- Intelligent analysis (AI)

Setup:
1. Set your API key: export ANTHROPIC_API_KEY=your-key-here
2. Run: uv run example-6-hybrid-approach.py
"""

import anthropic
import base64
import os
from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image
import imagehash


class VisualTestResult:
    """Container for visual test results."""

    def __init__(self):
        self.perceptual_hash_match = None
        self.pixel_diff_percentage = None
        self.ai_analysis = None
        self.passed = False
        self.issues = []


class HybridVisualTester:
    """Hybrid visual testing using multiple techniques."""

    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        self.client = anthropic.Anthropic(api_key=self.api_key) if self.api_key else None

    def capture_screenshot(self, url: str, output_path: str) -> str:
        """Capture screenshot using Playwright."""
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(url)
            page.wait_for_load_state('networkidle')
            page.screenshot(path=output_path, full_page=True)
            browser.close()
        return output_path

    def compute_perceptual_hash(self, image_path: str) -> str:
        """Compute perceptual hash of image."""
        img = Image.open(image_path)
        return str(imagehash.average_hash(img))

    def compare_perceptual_hashes(
        self,
        hash1: str,
        hash2: str,
        threshold: int = 5
    ) -> bool:
        """Compare two perceptual hashes."""
        h1 = imagehash.hex_to_hash(hash1)
        h2 = imagehash.hex_to_hash(hash2)
        distance = h1 - h2
        return distance <= threshold

    def compare_pixels(self, image1_path: str, image2_path: str) -> float:
        """
        Compare two images pixel by pixel.
        Returns percentage of different pixels.
        """
        img1 = Image.open(image1_path).convert('RGB')
        img2 = Image.open(image2_path).convert('RGB')

        # Ensure same size
        if img1.size != img2.size:
            img2 = img2.resize(img1.size)

        # Compare pixels
        pixels1 = list(img1.getdata())
        pixels2 = list(img2.getdata())

        different = sum(1 for p1, p2 in zip(pixels1, pixels2) if p1 != p2)
        total = len(pixels1)

        return (different / total) * 100

    def analyze_with_ai(
        self,
        baseline_path: str,
        current_path: str
    ) -> str:
        """Analyze screenshots using Claude Vision API."""
        if not self.client:
            return "AI analysis skipped (no API key)"

        with open(baseline_path, "rb") as f:
            baseline_b64 = base64.b64encode(f.read()).decode("utf-8")

        with open(current_path, "rb") as f:
            current_b64 = base64.b64encode(f.read()).decode("utf-8")

        message = self.client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=4096,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Baseline screenshot (expected):"
                        },
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/png",
                                "data": baseline_b64,
                            },
                        },
                        {
                            "type": "text",
                            "text": "Current screenshot:"
                        },
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/png",
                                "data": current_b64,
                            },
                        },
                        {
                            "type": "text",
                            "text": """
                            Compare these screenshots and provide:

                            1. VISUAL REGRESSIONS: List any broken layouts, misalignments, or visual bugs
                            2. INTENTIONAL CHANGES: List changes that appear intentional
                            3. SEVERITY ASSESSMENT: Rate each issue as CRITICAL, MAJOR, or MINOR
                            4. RECOMMENDATION: Should this pass or fail the visual test?

                            Focus on meaningful differences that affect user experience.
                            Ignore minor rendering variations (anti-aliasing, font hinting).
                            """
                        }
                    ],
                }
            ],
        )

        return message.content[0].text

    def run_hybrid_test(
        self,
        baseline_path: str,
        current_path: str,
        perceptual_threshold: int = 5,
        pixel_threshold: float = 0.1,
        use_ai: bool = True
    ) -> VisualTestResult:
        """
        Run hybrid visual test using multiple techniques.

        Args:
            baseline_path: Path to baseline screenshot
            current_path: Path to current screenshot
            perceptual_threshold: Max perceptual hash distance (0-64)
            pixel_threshold: Max allowed pixel difference percentage (0-100)
            use_ai: Whether to use AI analysis

        Returns:
            VisualTestResult with test results
        """
        result = VisualTestResult()

        # Step 1: Quick perceptual hash check
        print("Step 1: Perceptual hash comparison...")
        baseline_hash = self.compute_perceptual_hash(baseline_path)
        current_hash = self.compute_perceptual_hash(current_path)
        result.perceptual_hash_match = self.compare_perceptual_hashes(
            baseline_hash, current_hash, perceptual_threshold
        )

        print(f"  Baseline hash: {baseline_hash}")
        print(f"  Current hash:  {current_hash}")
        print(f"  Match: {result.perceptual_hash_match}")

        # If perceptual hashes don't match, proceed with detailed analysis
        if not result.perceptual_hash_match:
            # Step 2: Pixel-by-pixel comparison
            print("\nStep 2: Pixel comparison...")
            result.pixel_diff_percentage = self.compare_pixels(
                baseline_path, current_path
            )
            print(f"  Pixel difference: {result.pixel_diff_percentage:.2f}%")

            # Step 3: AI analysis (if differences exceed threshold)
            if result.pixel_diff_percentage > pixel_threshold and use_ai:
                print("\nStep 3: AI analysis...")
                result.ai_analysis = self.analyze_with_ai(baseline_path, current_path)
                print("\n" + result.ai_analysis)

                # Determine if test passes based on AI analysis
                if "CRITICAL" in result.ai_analysis or "fail" in result.ai_analysis.lower():
                    result.passed = False
                    result.issues.append("AI detected critical visual issues")
                else:
                    result.passed = True
            elif result.pixel_diff_percentage <= pixel_threshold:
                result.passed = True
                print("  ✓ Pixel difference within acceptable threshold")
            else:
                result.passed = False
                result.issues.append(f"Pixel difference ({result.pixel_diff_percentage:.2f}%) exceeds threshold ({pixel_threshold}%)")
        else:
            result.passed = True
            result.pixel_diff_percentage = 0.0
            print("  ✓ Perceptual hashes match - images are very similar")

        return result


def test_workflow_example():
    """Example testing workflow."""
    tester = HybridVisualTester()

    # Test scenario: Homepage visual regression
    print("=== Homepage Visual Regression Test ===\n")

    # Capture baseline (first time)
    baseline_path = "homepage_baseline.png"
    if not Path(baseline_path).exists():
        print("Capturing baseline screenshot...")
        tester.capture_screenshot("https://example.com", baseline_path)
        print(f"Baseline saved to {baseline_path}\n")

    # Capture current state
    print("Capturing current screenshot...")
    current_path = "homepage_current.png"
    tester.capture_screenshot("https://example.com", current_path)
    print(f"Current saved to {current_path}\n")

    # Run hybrid test
    result = tester.run_hybrid_test(
        baseline_path,
        current_path,
        perceptual_threshold=5,
        pixel_threshold=0.5,  # 0.5% pixel difference allowed
        use_ai=True
    )

    # Report results
    print("\n" + "="*50)
    print("TEST RESULTS")
    print("="*50)
    print(f"Status: {'✓ PASSED' if result.passed else '✗ FAILED'}")
    if result.issues:
        print("\nIssues:")
        for issue in result.issues:
            print(f"  - {issue}")


def test_responsive_workflow():
    """Test responsive design at multiple breakpoints."""
    tester = HybridVisualTester()
    url = "https://example.com"

    breakpoints = {
        "mobile": (375, 667),
        "tablet": (768, 1024),
        "desktop": (1920, 1080)
    }

    print("=== Responsive Design Testing ===\n")

    with sync_playwright() as p:
        browser = p.chromium.launch()

        for device, (width, height) in breakpoints.items():
            print(f"\nTesting {device} ({width}x{height})...")

            # Capture screenshots
            page = browser.new_page(viewport={"width": width, "height": height})
            page.goto(url)
            page.wait_for_load_state('networkidle')

            baseline = f"{device}_baseline.png"
            current = f"{device}_current.png"

            # For demo, we'll create baseline if not exists
            if not Path(baseline).exists():
                page.screenshot(path=baseline)
                print(f"  Created baseline: {baseline}")

            page.screenshot(path=current)
            print(f"  Captured current: {current}")

            # Run test
            result = tester.run_hybrid_test(baseline, current, use_ai=False)
            print(f"  Result: {'✓ PASSED' if result.passed else '✗ FAILED'}")

        browser.close()


def test_ci_cd_integration():
    """Example of how to integrate with CI/CD pipeline."""
    tester = HybridVisualTester()

    # This would run in CI/CD
    test_cases = [
        ("https://example.com", "homepage"),
        ("https://example.com/about", "about"),
        ("https://example.com/contact", "contact")
    ]

    failed_tests = []

    for url, name in test_cases:
        baseline = f"baselines/{name}.png"
        current = f"current/{name}.png"

        # Ensure directories exist
        Path("baselines").mkdir(exist_ok=True)
        Path("current").mkdir(exist_ok=True)

        # Capture current
        tester.capture_screenshot(url, current)

        # Test only if baseline exists
        if Path(baseline).exists():
            result = tester.run_hybrid_test(
                baseline,
                current,
                perceptual_threshold=5,
                pixel_threshold=1.0,
                use_ai=True  # Use AI for final validation
            )

            if not result.passed:
                failed_tests.append(name)
        else:
            print(f"No baseline for {name}, creating...")
            Path(current).rename(baseline)

    # Exit with appropriate code for CI/CD
    if failed_tests:
        print(f"\n✗ {len(failed_tests)} tests failed: {', '.join(failed_tests)}")
        exit(1)
    else:
        print("\n✓ All visual tests passed!")
        exit(0)


if __name__ == "__main__":
    # Run example workflow
    test_workflow_example()

    # Uncomment to test other scenarios:
    # test_responsive_workflow()
    # test_ci_cd_integration()
