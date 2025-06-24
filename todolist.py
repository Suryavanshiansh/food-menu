tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Task to add: ").strip()
    if task:
        tasks.append(task)
        print("Added!")
    else:
        print("Can't add empty task.")

def mark_task_done():
    show_tasks()
    if not tasks:
        return
    try:
        idx = int(input("Task number done: "))
        if 1 <= idx <= len(tasks):
            print(f'Removed: {tasks[idx-1]}')
            tasks.pop(idx-1)
        else:
            print("No such task.")
    except ValueError:
        print("Enter a number.")

def delete_task():
    show_tasks()
    if not tasks:
        return
    try:
        idx = int(input("Task number to delete: "))
        if 1 <= idx <= len(tasks):
            print(f'Deleted: {tasks[idx-1]}')
            tasks.pop(idx-1)
        else:
            print("No such task.")
    except ValueError:
        print("Enter a number.")

def todo_list_app():
    print("To-Do List Manager")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Mark done")
    print("4. Delete task")
    print("5. Exit")
    while True:
        choice = input("Choice (1-5): ")
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_task_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Pick 1-5.")

# Uncomment to run: