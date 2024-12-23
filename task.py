import os

# Function to load tasks from file
def load_tasks(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            tasks = file.readlines()
        tasks = [task.strip() for task in tasks]
        return tasks
    return []

# Function to save tasks to file
def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

# Function to display the menu
def display_menu():
    print("\nTo-Do List")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")

# Function to add a task
def add_task(tasks):
    task = input("Enter the task description: ")
    tasks.append(f"[ ] {task}")

# Function to view tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available!")
    else:
        print("\nCurrent Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

# Function to mark a task as completed
def mark_completed(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1] = tasks[task_num - 1].replace("[ ]", "[X]")
            print("Task marked as completed.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            print(f"Deleted task: {deleted_task}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

# Main function to run the To-Do list app
def todo_app():
    tasks_filename = "tasks.txt"
    tasks = load_tasks(tasks_filename)

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks_filename, tasks)
            print("Tasks saved successfully. Exiting the app.")
            break
        else:
            print("Invalid choice, please try again.")

# Run the application
if __name__ == "__main__":
    todo_app()
