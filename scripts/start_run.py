from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
def start_run():
    chromedriver_path = r"C:\Dev\cookie_clicker\chromedriver\chromedriver.exe"
    chrome_binary_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    chrome_options = Options()
    chrome_options.binary_location = chrome_binary_path
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # <- hides automation
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Extra: execute JS to remove webdriver flag
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
      "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
      """
    })

    driver.get("https://orteil.dashnet.org/cookieclicker/")
    # Wait until the button appears, then click
    try:
        consent_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.fc-button.fc-cta-consent.fc-primary-button"))
        )
        consent_button.click()
        print("Consent clicked!")
    except Exception as e:
        print("Consent button not found or clickable:", e)
    time.sleep(1)
    lang_button = driver.find_element(By.ID, "langSelect-EN")
    actions = ActionChains(driver)
    time.sleep(0.3)  
    actions.move_to_element(lang_button).perform()
    time.sleep(0.3)
    english_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "langSelect-EN"))
    )
    english_button.click()
    driver.execute_script("console.log('Hello from Selenium!')")
    return driver

