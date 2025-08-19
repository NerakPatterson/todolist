from addtask import add_task
from viewtask import view_task
from delete import delete_task

def display_menu():
    print("\n1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Quit")   

def main():
    while True:
        display_menu()
        choice = input("What would you like to do?: ").strip()

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

if __name__ == "__main__":
    main()
