
def click_cookie(driver):
    driver.execute_script("Game.ClickCookie();")
def click_cookie_100(driver):
    for _ in range(100):
        driver.execute_script("Game.ClickCookie();")