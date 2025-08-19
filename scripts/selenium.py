from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import base64
import time

# Setup Chrome in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

# Open Cookie Clicker
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Wait for the game to load (adjust if needed)
time.sleep(10)

# Retrieve the save from localStorage
save_base64 = driver.execute_script("return localStorage.getItem('CookieClickerGame');")

# Decode the save
save_data = base64.b64decode(save_base64).decode('utf-8')

# Save to a file
with open("cookie_clicker_save.txt", "w", encoding="utf-8") as f:
    f.write(save_data)

print("Save retrieved successfully!")

driver.quit()
