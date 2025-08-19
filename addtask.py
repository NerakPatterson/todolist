from data import tasks

def add_task():
    task = input("Enter a task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added.")
    else:
        print("No task entered.")
