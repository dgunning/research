/**
 * Example 2: Applitools Eyes AI-Powered Visual Testing
 *
 * Applitools uses Visual AI to intelligently detect visual bugs while ignoring
 * acceptable differences (anti-aliasing, font rendering, dynamic content).
 *
 * Installation:
 * npm install -D @applitools/eyes-playwright
 *
 * Setup:
 * npx eyes-playwright setup
 * # This will prompt for your Applitools API key
 *
 * Run tests:
 * npx playwright test
 */

import { test } from '@applitools/eyes-playwright/fixture';

test.describe('Applitools AI Visual Tests', () => {

  test('AI-powered visual validation', async ({ page, eyes }) => {
    // Navigate to application
    await page.goto('https://example.com');

    // Applitools will use AI to validate the entire page
    // It automatically handles:
    // - Font rendering differences
    // - Anti-aliasing
    // - Minor positioning shifts
    // - Browser rendering differences
    await eyes.check('Homepage');
  });

  test('responsive design testing', async ({ page, eyes }) => {
    await page.goto('https://example.com');

    // Test multiple viewports automatically
    const viewports = [
      { width: 1920, height: 1080, name: 'Desktop' },
      { width: 768, height: 1024, name: 'Tablet' },
      { width: 375, height: 667, name: 'Mobile' }
    ];

    for (const viewport of viewports) {
      await page.setViewportSize({
        width: viewport.width,
        height: viewport.height
      });
      await eyes.check(viewport.name);
    }
  });

  test('specific element validation', async ({ page, eyes }) => {
    await page.goto('https://example.com/dashboard');

    // Check specific regions
    await eyes.check('Dashboard Header', {
      region: page.locator('#header')
    });

    await eyes.check('Main Content', {
      region: page.locator('#main-content')
    });
  });

  test('ignore dynamic regions', async ({ page, eyes }) => {
    await page.goto('https://example.com');

    // Ignore regions that change frequently
    await eyes.check('Homepage', {
      ignore: [
        page.locator('.timestamp'),
        page.locator('.live-updates'),
        page.locator('.advertisement')
      ]
    });
  });

  test('layout-only validation', async ({ page, eyes }) => {
    await page.goto('https://example.com');

    // Validate only layout, ignore content changes
    await eyes.check('Layout Check', {
      layout: [page.locator('#content')]
    });
  });
});

/**
 * Alternative: Using Applitools Classic API
 */
import { test as baseTest } from '@playwright/test';
import { Eyes, Target } from '@applitools/eyes-playwright';

baseTest.describe('Applitools Classic API', () => {
  let eyes;

  baseTest.beforeEach(async ({ page }) => {
    eyes = new Eyes();
    await eyes.open(page, 'My App', baseTest.info().title);
  });

  baseTest.afterEach(async () => {
    await eyes.close();
  });

  baseTest('full page check', async ({ page }) => {
    await page.goto('https://example.com');
    await eyes.check('Homepage', Target.window().fully());
  });
});

/**
 * Configuration in .applitools.config.js:
 *
 * module.exports = {
 *   appName: 'My Frontend App',
 *   batchName: 'Visual Regression Tests',
 *   browser: [
 *     { width: 1920, height: 1080, name: 'chrome' },
 *     { width: 1920, height: 1080, name: 'firefox' },
 *     { width: 1920, height: 1080, name: 'safari' }
 *   ],
 *   // Run on Applitools' Ultrafast Grid for parallel cross-browser testing
 *   concurrency: 5
 * };
 */
