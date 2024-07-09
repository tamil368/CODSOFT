class Todo:
    def __init__(self):
        self.Tasks = []

    def add_task(self, task):
        self.Tasks.append(task)

    def remove_task(self, task):
        self.Tasks.remove(task)

    def update_task(self, old_task, new_task):
        if old_task in self.Tasks:
            index = self.Tasks.index(old_task)
            self.Tasks[index] = new_task

    def display_tasks(self):
        print("TO-Do list")
        for task in self.Tasks:
            print(task)

def add_task(todo):
    task = input("Enter task to add: ")
    todo.add_task(task)

def remove_task(todo):
    task = input("Enter task to remove: ")
    todo.remove_task(task)

def update_task(todo):
    old_task = input("Enter task to update: ")
    new_task = input("Enter new task: ")
    todo.update_task(old_task, new_task)

def display_tasks(todo):
    todo.display_tasks()

to_do = Todo()

while True:
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Update Task")
    print("4. Display Tasks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_task(to_do)
    elif choice == '2':
        remove_task(to_do)
    elif choice == '3':
        update_task(to_do)
    elif choice == '4':
        display_tasks(to_do)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
