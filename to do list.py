class TodoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task index!")

    def display_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")
        else:
            print("Your To-Do List is empty!")

def main():
    todo_list = TodoList()
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Display Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter the index of the task to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo_list.update_task(index, new_task)
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please try again.")

if _name_ == "_main_":
    main()
