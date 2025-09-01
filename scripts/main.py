import os, sys, subprocess

VENV_PYTHON = os.path.abspath(
os.path.join(os.path.dirname(__file__), "..", ".venv", "Scripts", "python.exe")
)

# Normalize both paths to avoid string mismatch issues
current_python = os.path.abspath(sys.executable)

if current_python != VENV_PYTHON:
    print(f"[INFO] Relaunching script using venv Python: {VENV_PYTHON}")
    subprocess.run([VENV_PYTHON, *sys.argv])
    sys.exit()

print(f"[INFO] Running inside venv with: {sys.executable}")
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