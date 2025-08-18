tasks = []

# Function to display options/main
def display_menu():
    print("\n1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Quit")
    
# Function to add a task to the list.
def add_task():
    task = input("Hurry up and enter task!: ")  
    tasks.append(task)  
    print(f"Task '{task}' added successfully.")
        
# Function to view all tasks in the tasks list.
def view_task():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to delete a task from the tasks list.
def delete_task():
    if not tasks:
        print("No tasks to delete.")
        return
    
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    
    try:
        choice = int(input("Which task do you want to delete? ")) - 1
        if 0 <= choice < len(tasks):
            removed = tasks.pop(choice)
            print(f"Task '{removed}' deleted.")
        else:
            print("Invalid choice. Please enter a valid number.")
    except ValueError:
        print("Error: Please enter a number, not text.")

# Main function (start of the program).
def main():
    while True:
        display_menu()
        choice = input("What would you like to do?: ").strip()

        # validate menu choice
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid input. Please enter 1, 2, 3, or 4.")
            continue
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break

main()
