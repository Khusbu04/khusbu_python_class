## Todo list using pythin class and object
class TodoList:
    def __init__(self):
        self.tasks=[]
    def add_tasks(self, task): ## Create
        self.tasks.append(task)
        print(f"Task '{task}'added to the list.")
    def remove_task(self, task): ## Delete
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed from the list.")
        else:
            print(f"Tasks '{tasks}' not found in the list.")
    def update_task(self,old_task, new_task): ## Update
        if old_task in self.tasks:
            index = self.tasks.index(old_task)
            self.tasks[index] = new_task
            print(f"Task update to '{new_tasks}'.")
        else:
            print(f"Tasks '{old_task}' not found in the list.")
    def show_tasks(self): ## Get
        if self.tasks:
            print("Your Todo List:")
            for index, tasks in enumerate(self.tasks):
                print(f"{index + 1}. {tasks}")
        else:
            print("Your Todo List is empty.")  
todo_list = TodoList()

todo_list.add_tasks("Buy groceries")
todo_list.add_tasks("Finish the report")
todo_list.add_tasks("Call mom")

todo_list.show_tasks()
todo_list.remove_task("Finish the report")
todo_list.update_task("But groceries", "Go for a walk")
todo_list.show_tasks()

        