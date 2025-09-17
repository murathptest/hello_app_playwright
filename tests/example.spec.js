const { test, expect } = require('@playwright/test');

test('homepage has form', async ({ page }) => {
  await page.goto('http://127.0.0.1:5000'); // Flask app must be running
  await expect(page.locator('input[name="name"]')).toBeVisible();
  await expect(page.locator('input[name="agree"]')).toBeVisible();
});
