def boot_console(driver):
    while True:
        command = input("Enter command (type 'exit' to quit): ")
        command = command.lower()
        if command == 'exit':
            break
        elif command == 'save_lockal_load':
            from save_lockal import save_lockal_load
            local_save = save_lockal_load()
            print("Local save loaded:", local_save)
            driver.execute_script(f"Game.ImportSaveCode('{local_save}');")
            continue
        elif command == 'save_lockal_overwrite':
            from save_lockal import save_lockal_overwrite
            new_save_string = driver.execute_script("return Game.ExportSaveCode();")
            save_lockal_overwrite(new_save_string)
            print("Save file overwritten.")
            continue
        elif command == 'hello_world':
            print("Hello, World!")
            continue

        try:
            exec(command)
        except Exception as e:
            print(f"Error executing command: {e}")