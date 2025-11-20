/**
 * Example 7: Chrome DevTools Integration with Playwright
 *
 * This example demonstrates how to leverage Chrome DevTools capabilities
 * for visual testing, including Lighthouse, CDP (Chrome DevTools Protocol),
 * and accessibility checks.
 *
 * Installation:
 * npm install -D @playwright/test lighthouse
 * npx playwright install chromium
 *
 * Run:
 * npx playwright test example-7-chrome-devtools.js
 */

import { test, expect, chromium } from '@playwright/test';
import lighthouse from 'lighthouse';
import { URL } from 'url';

test.describe('Chrome DevTools Integration', () => {

  test('Lighthouse accessibility audit', async ({ page }) => {
    // Navigate to the page
    await page.goto('https://example.com');

    // Get the browser's WebSocket endpoint for Lighthouse
    const browser = page.context().browser();
    const port = new URL(browser.wsEndpoint()).port;

    // Run Lighthouse audit
    const result = await lighthouse('https://example.com', {
      port: port,
      output: 'json',
      onlyCategories: ['accessibility', 'best-practices'],
    });

    // Parse results
    const { lhr } = result;

    console.log('\n=== Lighthouse Scores ===');
    console.log(`Accessibility: ${lhr.categories.accessibility.score * 100}`);
    console.log(`Best Practices: ${lhr.categories['best-practices'].score * 100}`);

    // Assert minimum scores
    expect(lhr.categories.accessibility.score).toBeGreaterThan(0.9); // 90+
    expect(lhr.categories['best-practices'].score).toBeGreaterThan(0.9);

    // Check for specific accessibility issues
    const contrastAudit = lhr.audits['color-contrast'];
    if (contrastAudit.score < 1) {
      console.log('\n⚠️  Contrast Issues Found:');
      contrastAudit.details.items.forEach(item => {
        console.log(`  - ${item.node.selector}: ${item.node.explanation}`);
      });
    }
  });

  test('CDP: Performance metrics during visual test', async ({ page }) => {
    // Get CDP session
    const client = await page.context().newCDPSession(page);

    // Enable performance tracking
    await client.send('Performance.enable');

    // Navigate and take screenshot
    await page.goto('https://example.com');
    await page.waitForLoadState('networkidle');

    // Get performance metrics
    const metrics = await client.send('Performance.getMetrics');

    console.log('\n=== Performance Metrics ===');
    metrics.metrics.forEach(metric => {
      if (metric.name.includes('Duration') || metric.name.includes('Time')) {
        console.log(`${metric.name}: ${metric.value.toFixed(2)}`);
      }
    });

    // Take screenshot only after performance check
    await page.screenshot({ path: 'performance-validated.png' });

    // Verify key metrics
    const layoutDuration = metrics.metrics.find(m => m.name === 'LayoutDuration');
    if (layoutDuration) {
      expect(layoutDuration.value).toBeLessThan(1000); // Less than 1 second
    }
  });

  test('CDP: Block resources for consistent screenshots', async ({ page }) => {
    // Get CDP session
    const client = await page.context().newCDPSession(page);

    // Block ads and analytics for consistent visual tests
    await client.send('Network.setBlockedURLs', {
      urls: [
        '*google-analytics.com*',
        '*doubleclick.net*',
        '*facebook.com/tr*',
        '*ads*',
        '*.gif', // Block animated GIFs
      ]
    });

    // Navigate and screenshot
    await page.goto('https://example.com');
    await page.screenshot({ path: 'blocked-resources.png' });

    console.log('✓ Screenshot taken with ads/analytics blocked');
  });

  test('CDP: CSS coverage analysis', async ({ page }) => {
    // Get CDP session
    const client = await page.context().newCDPSession(page);

    // Start CSS coverage
    await client.send('CSS.startRuleUsageTracking');

    // Navigate and interact
    await page.goto('https://example.com');
    await page.click('button'); // Simulate interaction

    // Stop coverage and get results
    const coverage = await client.send('CSS.stopRuleUsageTracking');

    // Analyze unused CSS
    let totalBytes = 0;
    let usedBytes = 0;

    coverage.ruleUsage.forEach(rule => {
      totalBytes += rule.endOffset - rule.startOffset;
      if (rule.used) {
        usedBytes += rule.endOffset - rule.startOffset;
      }
    });

    const usagePercentage = (usedBytes / totalBytes) * 100;

    console.log('\n=== CSS Coverage ===');
    console.log(`Total CSS: ${(totalBytes / 1024).toFixed(2)} KB`);
    console.log(`Used CSS: ${(usedBytes / 1024).toFixed(2)} KB`);
    console.log(`Coverage: ${usagePercentage.toFixed(2)}%`);

    // Warn if too much unused CSS (affects screenshot performance)
    if (usagePercentage < 50) {
      console.log('⚠️  Warning: Less than 50% CSS coverage - consider optimizing');
    }
  });

  test('Vision deficiency simulation', async ({ page }) => {
    const client = await page.context().newCDPSession(page);
    await page.goto('https://example.com');

    const visionTypes = [
      'none',
      'protanopia',    // Red-blind
      'deuteranopia',  // Green-blind
      'tritanopia',    // Blue-blind
      'achromatopsia'  // No color
    ];

    console.log('\n=== Vision Deficiency Screenshots ===');

    for (const visionType of visionTypes) {
      // Set vision deficiency emulation
      await client.send('Emulation.setEmulatedVisionDeficiency', {
        type: visionType
      });

      // Take screenshot
      const filename = `vision-${visionType}.png`;
      await page.screenshot({ path: filename });
      console.log(`✓ Captured: ${filename}`);
    }

    // Reset to normal
    await client.send('Emulation.setEmulatedVisionDeficiency', {
      type: 'none'
    });
  });

  test('Automated contrast checking', async ({ page }) => {
    await page.goto('https://example.com');

    // Inject script to check all text elements for contrast
    const contrastIssues = await page.evaluate(() => {
      const issues = [];

      // Helper to get contrast ratio
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

      // Parse RGB color
      function parseColor(colorStr) {
        const canvas = document.createElement('canvas');
        canvas.width = canvas.height = 1;
        const ctx = canvas.getContext('2d');
        ctx.fillStyle = colorStr;
        ctx.fillRect(0, 0, 1, 1);
        const [r, g, b] = ctx.getImageData(0, 0, 1, 1).data;
        return { r, g, b };
      }

      // Check all text elements
      const textElements = document.querySelectorAll('p, h1, h2, h3, h4, h5, h6, span, a, button, label');

      textElements.forEach(element => {
        const styles = window.getComputedStyle(element);
        const color = parseColor(styles.color);
        const bgColor = parseColor(styles.backgroundColor);

        const ratio = getContrastRatio(color, bgColor);
        const fontSize = parseFloat(styles.fontSize);

        // WCAG AA requirements
        const minRatio = fontSize >= 18 || (fontSize >= 14 && styles.fontWeight >= 700) ? 3 : 4.5;

        if (ratio < minRatio) {
          issues.push({
            selector: element.tagName + (element.id ? '#' + element.id : '') + (element.className ? '.' + element.className.split(' ')[0] : ''),
            text: element.textContent.substring(0, 50),
            ratio: ratio.toFixed(2),
            required: minRatio,
            color: styles.color,
            bgColor: styles.backgroundColor
          });
        }
      });

      return issues;
    });

    console.log('\n=== Contrast Issues ===');
    if (contrastIssues.length === 0) {
      console.log('✓ No contrast issues found');
    } else {
      console.log(`⚠️  Found ${contrastIssues.length} contrast issues:`);
      contrastIssues.slice(0, 10).forEach(issue => {
        console.log(`  ${issue.selector}: ${issue.ratio}:1 (need ${issue.required}:1)`);
        console.log(`    Text: "${issue.text}"`);
        console.log(`    Colors: ${issue.color} on ${issue.bgColor}\n`);
      });
    }

    // Optionally fail test if critical issues found
    expect(contrastIssues.filter(i => i.required === 4.5).length).toBeLessThan(5);
  });

  test('Full DevTools audit workflow', async ({ page }) => {
    const client = await page.context().newCDPSession(page);

    console.log('\n=== Full DevTools Audit ===\n');

    // Step 1: Enable performance and coverage tracking
    await client.send('Performance.enable');
    await client.send('CSS.startRuleUsageTracking');
    await client.send('Profiler.enable');
    await client.send('Profiler.startPreciseCoverage', {
      callCount: true,
      detailed: true
    });

    // Step 2: Navigate
    console.log('1. Loading page...');
    await page.goto('https://example.com');
    await page.waitForLoadState('networkidle');

    // Step 3: Get performance metrics
    console.log('2. Collecting performance metrics...');
    const metrics = await client.send('Performance.getMetrics');
    const layoutDuration = metrics.metrics.find(m => m.name === 'LayoutDuration');
    console.log(`   Layout Duration: ${layoutDuration?.value.toFixed(2)}ms`);

    // Step 4: Check CSS coverage
    console.log('3. Analyzing CSS coverage...');
    const cssCoverage = await client.send('CSS.stopRuleUsageTracking');
    let usedCSS = 0, totalCSS = 0;
    cssCoverage.ruleUsage.forEach(rule => {
      const size = rule.endOffset - rule.startOffset;
      totalCSS += size;
      if (rule.used) usedCSS += size;
    });
    console.log(`   CSS Coverage: ${((usedCSS / totalCSS) * 100).toFixed(1)}%`);

    // Step 5: Take baseline screenshot
    console.log('4. Capturing baseline screenshot...');
    await page.screenshot({ path: 'devtools-audit-baseline.png' });

    // Step 6: Test vision deficiencies
    console.log('5. Testing vision accessibility...');
    await client.send('Emulation.setEmulatedVisionDeficiency', {
      type: 'deuteranopia'
    });
    await page.screenshot({ path: 'devtools-audit-colorblind.png' });

    // Step 7: Stop coverage
    const jsCoverage = await client.send('Profiler.takePreciseCoverage');
    let usedJS = 0, totalJS = 0;
    jsCoverage.result.forEach(script => {
      script.functions.forEach(func => {
        func.ranges.forEach(range => {
          const size = range.endOffset - range.startOffset;
          totalJS += size;
          if (range.count > 0) usedJS += size;
        });
      });
    });
    console.log(`   JS Coverage: ${((usedJS / totalJS) * 100).toFixed(1)}%`);

    console.log('\n✓ Audit complete!\n');
  });
});

/**
 * Configuration tips for playwright.config.js:
 *
 * export default defineConfig({
 *   use: {
 *     // Use Chromium for DevTools features
 *     browserName: 'chromium',
 *
 *     // Enable DevTools
 *     devtools: true,
 *
 *     // Collect trace for debugging
 *     trace: 'on-first-retry',
 *   },
 * });
 */
