import time
def boot_console(driver,stop_event):
    global running
    while True:
        command = input("Enter command (type 'exit' to quit): ")
        command = command.lower()
        if command == 'exit':
            break

        elif command == 'hello_world':
            print("Hello, World!")
            continue
         
            
        elif command.strip().lower() == "exit":
            print("Stopping maintenance...")
            stop_event.set()   # ✅ this tells maintain() to stop
            break
            
            continue

        try:
            exec(command)
        except Exception as e:
            print(f"Error executing command: {e}")