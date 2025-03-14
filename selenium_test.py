from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Enable Headless Mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Setup WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open CoinMarketCap Bitcoin page
url = "https://coinmarketcap.com/currencies/bitcoin/"
driver.get(url)

# Wait for the page to load
time.sleep(5)  # Give it a few seconds to load dynamically generated content

# Locate the price element
try:
    price_element = driver.find_element(By.XPATH, "//span[@data-test='text-cdp-price-display']")  # Updated selector for CoinMarketCap
    bitcoin_price = price_element.text
    print(f"Current Bitcoin Price: {bitcoin_price}")
except Exception as e:
    print("Error fetching Bitcoin price:", e)

# Close the browser
driver.quit()

