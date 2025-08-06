def load_tasks(filename):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks, task):
    tasks.append(task)
    print(f"Task added: {task}")

def remove_task(tasks, task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task removed: {task}")
    else:
        print("Task not found.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def main():
    filename = "tasks.txt"
    tasks = load_tasks(filename)

    while True:
        print("\nOptions: add / remove / view / exit")
        choice = input("Choose an option: ").strip().lower()

        if choice == "add":
            task = input("Enter a new task: ").strip()
            add_task(tasks, task)
            save_tasks(tasks, filename)

        elif choice == "remove":
            task = input("Enter task to remove: ").strip()
            remove_task(tasks, task)
            save_tasks(tasks, filename)

        elif choice == "view":
            view_tasks(tasks)

        elif choice == "exit":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
