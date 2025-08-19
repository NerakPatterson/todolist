from data import tasks

def delete_task():
    if not tasks:
        print("No tasks to delete.")
        return

    print("\nTasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

    choice = input("Enter task number to delete: ").strip()

    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Task '{removed}' deleted.")
        else:
            print("Invalid task number.")
    else:
        print("Invalid input. Enter a number.")
