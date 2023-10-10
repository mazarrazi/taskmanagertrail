# task_manager.py
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added successfully.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

def main():
    task_manager = TaskManager()

    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. List tasks")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            task_manager.add_task(task)
        elif choice == "2":
            task_manager.list_tasks()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
