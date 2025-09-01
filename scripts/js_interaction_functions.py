
def click_cookie(driver):
    driver.execute_script("Game.ClickCookie();")
def click_cookie_100(driver):
    for _ in range(100):
        driver.execute_script("Game.ClickCookie();")
def save_lockal_load(driver):
    from save_lockal import save_lockal_load
    local_save = save_lockal_load()
    print("Local save loaded:", local_save)
    driver.execute_script(f"Game.ImportSaveCode('{local_save}');")
    
def save_lockal_overwrite(driver):
    from save_lockal import save_lockal_overwrite
    new_save_string = driver.execute_script("return Game.WriteSave(1);")
    save_lockal_overwrite(new_save_string)
    print("Save file overwritten.")