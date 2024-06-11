def add_task(tasks):
    task = input("Enter task description: ")
    tasks.append({"description": task, "completed": False})
    print("Task added!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return

    for index, task in enumerate(tasks):
        status = "✓" if task["completed"] else "✗"
        print(f"{index + 1}. {status} {task['description']}")

def mark_complete(tasks):
    view_tasks(tasks)

    try:
        task_index = int(input("Enter task number to mark complete: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["completed"] = True
            print("Task marked complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    tasks = []

    while True:
        print("\nChoose an action:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task complete")
        print("4. Exit")

        choice = input("> ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
