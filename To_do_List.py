# a basic to_do_List using python
#Creating a list to store the tasks
tasks = []
while True:

    print("\nWelcome to To-do List:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")

    try:
        # Get the user's choice
        choice = input("Enter your choice (1-5): ").strip()

        # Validate if the input is a number
        if not choice.isdigit():
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        choice = int(choice)  # Convert to integer
        if choice < 1 or choice > 5:
            print("Choice out of range. Please select between 1 and 5.")
            continue

        if choice == 1:  # Add a task
            task = input("Enter the task description: ").strip()
            if task:
                tasks.append({"task": task, "completed": False})
                print(f"Task '{task}' added successfully!")
            else:
                print("Task description cannot be empty.")

        elif choice == 2:  # View tasks
            if not tasks:
                print("No tasks available! Add some tasks first.")
            else:
                print("\n Tasks:")
                for id, task in enumerate(tasks, start=1):
                    status = "[X]" if task["completed"] else "[ ]"
                    print(f"{id}. {status} {task['task']}")

        elif choice == 3:  # Mark completed task
            if not tasks:
                print("No tasks available to mark as completed.")
            else:
                print("\n Tasks:")
                for id, task in enumerate(tasks, start=1):
                    status = "[X]" if task["completed"] else "[ ]"
                    print(f"{id}. {status} {task['task']}")
                task_num = input("Enter the task number to mark as completed: ").strip()

                # Validate if the input is a number
                if not task_num.isdigit():
                    print("Invalid input. Please enter a valid number.")
                    continue

                task_num = int(task_num)
                if task_num < 1 or task_num > len(tasks):
                    print("Task number out of range. Please select a valid task.")
                else:
                    tasks[task_num - 1]["completed"] = True
                    print(f"Task {task_num} marked as completed!")

        elif choice == 4:  # Delete a task
            if not tasks:
                print("No tasks available to delete.")
            else:
                print("\n Tasks:")
                for id, task in enumerate(tasks, start=1):
                    status = "[X]" if task["completed"] else "[ ]"
                    print(f"{id}. {status} {task['task']}")
                task_num = input("Enter the task number to delete: ").strip()

                # Validate if the input is a number
                if not task_num.isdigit():
                    print("Invalid input. Please enter a valid number.")
                    continue

                task_num = int(task_num)
                if task_num < 1 or task_num > len(tasks):
                    print("Task number out of range. Please select a valid task.")
                else:
                    deleted_task = tasks.pop(task_num - 1)
                    print(f"Task '{deleted_task['task']}' deleted successfully!")

        elif choice == 5:  # Exit
            print("Exiting the to do list")
            break

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

#Problem faced while doing this were
#invalid input handling solved by choice.isdigit().
#validation for task number solved by creating message for invalid or out of range task
#unexpected error :for this except block at final was created to handle them
