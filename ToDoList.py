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
