import time
from js_interaction_functions import click_cookie, click_cookie_100,save_lockal_load,save_lockal_overwrite,buy_structure

def boot_console(driver,stop_event):
    while True:
        command = input("Enter command (type 'exitc' to quit): ")
        command = command.lower()

        if command == 'hello_world':
            print("Hello, World!")
            continue
        elif command == 'save_lockal_load':
            save_lockal_load(driver)
            print("Local save loaded.")
            continue
        elif command == 'save_lockal_overwrite':
            save_lockal_overwrite(driver)
            print("Local save overwritten.")
            continue
        elif command == 'click_cookie':
            click_cookie(driver)
            print("Cookie clicked once.")
            continue
        elif command.strip() == "exitc":
            print("Stopping maintenance...")
            stop_event.set()   # ✅ this tells maintain() to stop
            break
        elif command == 'buy_structure':
            buy_structure(driver)
            print("Structure purchased.")
           
            # Add your buy_structure logic here
            continue
        try:
            exec(command)
        except Exception as e:
            print(f"Error executing command: {e}")