import os, sys, subprocess
def selectVenv():
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