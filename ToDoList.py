import os
import sys

from ToDo_Helper_Functions import add_task, save_to_file, mark_as_complete, load_session


class ToDoList:
    def __init__(self, formatter):
        self.incomplete_tasks, self.completed_tasks = load_session()
        self.formatter = formatter

    def add_task(self):
        add_task(self.incomplete_tasks)

    def view_and_save_tasks(self, file_name):
        content = self.formatter(self)
        save_to_file(file_name, content)

    def mark_completed(self):
        if len(self.incomplete_tasks):
            self.view_and_save_tasks(sys.stdout)
            mark_as_complete(self)
        else:
            message = "\nYour TODO list is empty!"
            save_to_file(sys.stdout, message)
