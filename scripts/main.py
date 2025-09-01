
from selectVENV import selectVenv
selectVenv()
import threading
from start_run import start_run
from maintainence_loop import maintain
from console import boot_console

driver = start_run()

stop_event = threading.Event()



# Start the background maintenance task
threading.Thread(
    target=maintain,
    args=(driver, stop_event),
    daemon=True
).start()

# Start the console listener (in main thread)
boot_console(driver, stop_event)