class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added to the list.")

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
            return
        print("\nTo-Do List:")
        for i, task in enumerate(self.tasks, 1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{i}. {task['task']} [{status}]")

    def mark_task_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' deleted.")
        else:
            print("Invalid task number.")

    def run(self):
        while True:
            print("\nOptions: 1. Add Task  2. View Tasks  3. Mark Task Completed  4. Delete Task  5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                task = input("Enter the task: ")
                self.add_task(task)
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                task_number = int(input("Enter the task number to mark as completed: "))
                self.mark_task_completed(task_number)
            elif choice == "4":
                task_number = int(input("Enter the task number to delete: "))
                self.delete_task(task_number)
            elif choice == "5":
                print("Exiting the To-Do List application.")
                break
            else:
                print("Invalid choice, please try again.")


if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()