# Create an empty list
tsks = []

while True:  # Keep asking user for input until exiting
    # Print out options to user
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")
    print("=" * 50)
    # Ask user for choice
    x = input("Enter your choice: ")
    # Begin and if-elif-else block
    if x == "1":  # Add task
        # Ask user to input task
        tsk = input("Enter task: ")
        # Append to list
        tsks.append(tsk)
        print("-" * 50)
    elif x == "2":  # View tasks
        print("Tasks:")
        # Iterate through tasks and print for user
        for i, t in enumerate(tsks):
            print(f"{i+1}. {t}")
        print("-" * 50)
    elif x == "3":  # Mark task as done
        # Ask user for task index and check if number is within the length of tasks
        usr_input = input("Enter task number to mark as done: ")
        if 0 <= int(usr_input) - 1 < len(tsks):
            # Delete that task index if index is present
            tsks.pop(int(usr_input) - 1)
            print("Task marked as done.")
        else:  # If task is not in list then it is invalid
            print("Invalid task number.")
    elif x == "4":  # Exits out of the loop
        print("Exiting.")
        print("-" * 50)
        break
    # Print that the user has made an invalid choice
    # This will start the while loop again and get the user for a choice again
    else:
        print("Invalid choice.")
        print("-" * 50)
