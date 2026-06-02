# Initialize an empty list to store the tasks
todo_list = []

while True:
    # Display the menu options
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit Application")
    
    choice = input("Select an option (1-4): ")
    
    if choice == '1':
        if not todo_list:
            print("\nYour to-do list is empty!")
        else:
            print("\nYour Current Tasks:")
            for index, task in enumerate(todo_list, start=1):
                print(f"{index}. {task}")
                
    elif choice == '2':
        new_task = input("\nEnter the task you want to add: ")
        todo_list.append(new_task)
        print(f"'{new_task}' has been added successfully.")
        
    elif choice == '3':
        if not todo_list:
            print("\nNothing to delete! Your list is empty.")
        else:
            print("\nYour Current Tasks:")
            for index, task in enumerate(todo_list, start=1):
                print(f"{index}. {task}")
            
            try:
                task_num = int(input("\nEnter the number of the task to delete: "))
                removed = todo_list.pop(task_num - 1)
                print(f"'{removed}' has been deleted successfully.")
            except (ValueError, IndexError):
                print("Invalid task number! Please try again.")
                
    elif choice == '4':
        print("\nExiting To-Do List application. Goodbye!")
        break
        
    else:
        print("Invalid choice! Please choose a number from 1 to 4.")
