import os
import sys

from utility_functions import add_task, save_to_file


class ToDoList:
    def __init__(self, formatter):
        self.incomplete_tasks = []
        self.complete_tasks = []
        self.formatter = formatter

    def add_task(self):
        add_task(self.incomplete_tasks)

    def view_tasks(self):
        content = self.formatter(self)
        save_to_file(sys.stdout, content)

    def save_task(self):
        content = self.formatter(self)
        path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        file_path = path + "/MyTasks.txt"
        save_to_file(file_path, content)
