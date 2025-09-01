from js_interaction_functions import click_cookie, click_cookie_100,save_lockal_load,save_lockal_overwrite
import time

def maintain(driver, stop_event):
    save_lockal_load(driver)
    while not stop_event.is_set():
        time.sleep(5)  # wait for 1 second before next click
        save_lockal_overwrite(driver)

        click_cookie(driver)
        # do something with driver
    print("Stopped maintain loop.")

    