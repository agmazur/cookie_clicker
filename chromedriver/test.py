from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os

# Path to your ChromeDriver
chromedriver_path = r"C:\Dev\cookie_clicker\chromedriver\chromedriver.exe"

# (Optional) Specify your Chrome binary if it's not in the default location
chrome_binary_path = r"C:\Dev\cookie_clicker\chromedriver\chrome.exe"

# Setup Chrome options
chrome_options = Options()
chrome_options.binary_location = chrome_binary_path  # tell Selenium where Chrome is
chrome_options.add_argument("--start-maximized")      # optional: open maximized

# Create service object
service = Service(executable_path=chromedriver_path)

# Launch Chrome
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open Cookie Clicker
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Wait a bit to see it load
time.sleep(10)

# Print page title to confirm it opened
print(driver.title)

# Close the browser
driver.quit()