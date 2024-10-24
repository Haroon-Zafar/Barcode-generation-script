from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Setup Chrome options to connect to the existing session
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")

# Path to your ChromeDriver
driver_service = Service('path/to/chromedriver')

# Create a WebDriver instance and connect to the running browser
driver = webdriver.Chrome(service=driver_service, options=chrome_options)

# List all open tabs (window handles)
windows = driver.window_handles

# Find and switch to the correct window handle (JIRA tab)
for window in windows:
    driver.switch_to.window(window)
    if "JIRA" in driver.title:  # Adjust this condition to match your JIRA tab
        break

# Now, you're controlling the JIRA tab, perform any Selenium actions
driver.get('https://jira.yourdomain.com')  # or interact directly