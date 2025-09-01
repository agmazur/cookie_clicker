from js_interaction_functions import click_cookie, click_cookie_100
import time

def maintain(driver, stop_event):
    time.sleep(10)  
    while not stop_event.is_set():
        time.sleep(5)  # wait for 1 second before next click

        click_cookie(driver)
        # do something with driver
    print("Stopped maintain loop.")