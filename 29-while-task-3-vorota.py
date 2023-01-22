print("---------- Автоматические ворота ----------")
is_open = False
while True:
    command = input("Command: ").lower()
    if command == "open":
        if is_open:
            print("It's already open.")
        else:
            print("Opening...")
        is_open = True
    elif command == "close":
        if is_open:
            print("Closing...")
        else:
            print("It's already closed.")
        is_open = False
    elif command == 'help':
        print("""Help menu:
open: открывает ворота 
close: закрывает ворота
stop: останавливает программу""")
    elif command == 'stop':
        print("Stopping...")
        break
    else:
        print("Incorrect command.")
print("Stopped.")