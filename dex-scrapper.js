// puppeteer-extra is a drop-in replacement for puppeteer,
// it augments the installed puppeteer with plugin functionality
const puppeteer = require("puppeteer-extra");

// add stealth plugin and use defaults (all evasion techniques)
const StealthPlugin = require("puppeteer-extra-plugin-stealth");
puppeteer.use(StealthPlugin());

(async () => {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto(
    "https://dexscreener.com/base?rankBy=trendingScoreH1&order=desc"
  );

  // Wait for the div with class 'ds-table-data-cell' to load

  // Function to periodically print the page content
  const printPageContent = async () => {
    console.log("Current page content:");
    console.log(await page.content());
  };

  // Set an interval to print the page content every 5 seconds
  setInterval(printPageContent, 5000);

  await page.waitForSelector(".ds-dex-table");

  // Extract text content of divs with class 'ds-table-data-cell'
  const data = await page.evaluate(() => {
    const divs = Array.from(document.querySelectorAll(".ds-table-data-cell"));
    return divs.map((div) => div.textContent.trim());
  });

  console.log(data);

  await browser.close();
})();
