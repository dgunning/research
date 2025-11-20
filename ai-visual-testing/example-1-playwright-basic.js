/**
 * Example 1: Basic Playwright Visual Testing
 *
 * This example demonstrates Playwright's built-in visual comparison using toHaveScreenshot().
 * No external AI services required - uses pixel-by-pixel comparison with configurable thresholds.
 *
 * Installation:
 * npm install -D @playwright/test
 * npx playwright install
 *
 * Run tests:
 * npx playwright test
 */

import { test, expect } from '@playwright/test';

test.describe('Visual Regression Tests', () => {

  test('full page screenshot comparison', async ({ page }) => {
    // Navigate to your application
    await page.goto('https://example.com');

    // Wait for page to be fully loaded
    await page.waitForLoadState('networkidle');

    // Take a screenshot and compare with baseline
    // First run: creates baseline screenshot
    // Subsequent runs: compares against baseline
    await expect(page).toHaveScreenshot('homepage.png');
  });

  test('element-specific screenshot comparison', async ({ page }) => {
    await page.goto('https://example.com');

    // Test a specific element (e.g., navigation bar)
    const navbar = page.locator('nav');
    await expect(navbar).toHaveScreenshot('navbar.png');
  });

  test('screenshot with configuration options', async ({ page }) => {
    await page.goto('https://example.com');

    // Advanced options for handling dynamic content
    await expect(page).toHaveScreenshot('homepage-tolerant.png', {
      // Allow up to 100 pixels to be different
      maxDiffPixels: 100,

      // Threshold for pixel comparison (0-1, where 1 is identical)
      threshold: 0.2,

      // Mask dynamic elements (timestamps, ads, etc.)
      mask: [
        page.locator('.timestamp'),
        page.locator('.advertisement')
      ],

      // Full page screenshot
      fullPage: true,

      // Animations handling
      animations: 'disabled'
    });
  });

  test('mobile viewport screenshot', async ({ page }) => {
    // Set mobile viewport
    await page.setViewportSize({ width: 375, height: 667 });
    await page.goto('https://example.com');

    await expect(page).toHaveScreenshot('homepage-mobile.png');
  });

  test('dark mode screenshot', async ({ page }) => {
    await page.goto('https://example.com');

    // Emulate dark color scheme
    await page.emulateMedia({ colorScheme: 'dark' });

    await expect(page).toHaveScreenshot('homepage-dark.png');
  });
});

/**
 * Configuration in playwright.config.js:
 *
 * import { defineConfig } from '@playwright/test';
 *
 * export default defineConfig({
 *   expect: {
 *     toHaveScreenshot: {
 *       maxDiffPixels: 100,
 *       threshold: 0.2,
 *       animations: 'disabled'
 *     },
 *   },
 *   use: {
 *     screenshot: 'only-on-failure',
 *   },
 * });
 */
