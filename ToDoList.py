import sys

from ToDoHelperFunctions import save_to_file, load_session


class ToDoList:
    def __init__(self, formatter):
        self.incomplete_tasks, self.completed_tasks = load_session()
        self.formatter = formatter

    def add_task(self, task):
        task = task.strip()
        if task:
            self.incomplete_tasks.append(task)
        else:
            print("Empty Task")

    def write_tasks(self, file_name):
        content = self.formatter(self)
        save_to_file(file_name, content)

    def mark_completed(self, task_number):
        if len(self.incomplete_tasks):
            self.write_tasks(sys.stdout)
            if task_number in range(1, len(self.incomplete_tasks) + 1):
                self.completed_tasks.append(self.incomplete_tasks[task_number - 1])
                del self.incomplete_tasks[task_number - 1]
            else:
                message = "\nThe task you're trying to mark is not present in the list"
                save_to_file(sys.stdout, message)
        else:
            message = "\nYour TODO list is empty!"
            save_to_file(sys.stdout, message)
