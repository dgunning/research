/**
 * Example 3: Percy (BrowserStack) Visual Testing
 *
 * Percy provides visual testing with smart baseline management and
 * visual diffing. Great for catching unintended visual changes.
 *
 * Installation:
 * npm install -D @percy/playwright @percy/cli
 *
 * Setup:
 * 1. Create a Percy project at percy.io
 * 2. Get your PERCY_TOKEN from project settings
 * 3. Export: export PERCY_TOKEN=your-token-here
 *
 * Run tests:
 * npx percy exec -- npx playwright test
 */

import { test } from '@playwright/test';
import percySnapshot from '@percy/playwright';

test.describe('Percy Visual Tests', () => {

  test('basic percy snapshot', async ({ page }) => {
    await page.goto('https://example.com');

    // Take a Percy snapshot
    // Percy handles cross-browser rendering automatically
    await percySnapshot(page, 'Homepage');
  });

  test('snapshot with custom widths', async ({ page }) => {
    await page.goto('https://example.com');

    // Test multiple responsive breakpoints
    await percySnapshot(page, 'Homepage - Responsive', {
      widths: [375, 768, 1280, 1920]
    });
  });

  test('snapshot with Percy-specific CSS', async ({ page }) => {
    await page.goto('https://example.com');

    // Apply custom CSS only for Percy snapshots
    await percySnapshot(page, 'Homepage - Clean', {
      percyCSS: `
        .advertisement { display: none !important; }
        .timestamp { visibility: hidden !important; }
        .animation { animation: none !important; }
      `
    });
  });

  test('full page snapshot', async ({ page }) => {
    await page.goto('https://example.com/long-page');

    // Capture full scrollable page
    await percySnapshot(page, 'Long Page', {
      fullPage: true
    });
  });

  test('snapshot with minimum height', async ({ page }) => {
    await page.goto('https://example.com');

    // Ensure minimum viewport height
    await percySnapshot(page, 'Homepage - Tall', {
      minHeight: 2000
    });
  });

  test('enable JavaScript for dynamic content', async ({ page }) => {
    await page.goto('https://example.com');

    // Wait for dynamic content to load
    await page.waitForSelector('.dynamic-content');

    await percySnapshot(page, 'With Dynamic Content', {
      enableJavaScript: true
    });
  });

  test('test multiple pages in sequence', async ({ page }) => {
    // Homepage
    await page.goto('https://example.com');
    await percySnapshot(page, 'Homepage');

    // Navigate to about page
    await page.click('a[href="/about"]');
    await percySnapshot(page, 'About Page');

    // Navigate to contact page
    await page.click('a[href="/contact"]');
    await percySnapshot(page, 'Contact Page');
  });

  test('snapshot after interaction', async ({ page }) => {
    await page.goto('https://example.com');

    // Before interaction
    await percySnapshot(page, 'Modal - Closed');

    // Open modal
    await page.click('#open-modal');
    await page.waitForSelector('.modal.open');

    // After interaction
    await percySnapshot(page, 'Modal - Open');
  });

  test('ignore regions with specific selectors', async ({ page }) => {
    await page.goto('https://example.com');

    // Ignore specific regions that change frequently
    await percySnapshot(page, 'Homepage - Stable', {
      percyCSS: `
        [data-percy-ignore] { visibility: hidden !important; }
      `
    });
  });
});

/**
 * Integration with BrowserStack Automate:
 * Combine functional and visual testing
 */
test.describe('Percy + BrowserStack Integration', () => {

  test('functional + visual testing', async ({ page }) => {
    await page.goto('https://example.com/form');

    // Visual test - before
    await percySnapshot(page, 'Form - Empty');

    // Functional test
    await page.fill('#name', 'John Doe');
    await page.fill('#email', 'john@example.com');

    // Visual test - filled
    await percySnapshot(page, 'Form - Filled');

    // Submit form
    await page.click('#submit');
    await page.waitForSelector('.success-message');

    // Visual test - success state
    await percySnapshot(page, 'Form - Success');
  });
});

/**
 * Configuration in percy.config.yml:
 *
 * version: 2
 * snapshot:
 *   widths:
 *     - 375
 *     - 768
 *     - 1280
 *   min-height: 1024
 *   enable-javascript: true
 * static:
 *   include: public/**
 *   exclude:
 *     - public/videos/**
 */
