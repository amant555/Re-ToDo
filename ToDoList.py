from utility_functions import add_task


class ToDoList:
    def __init__(self):
        self.incomplete_tasks = []

    def add_task(self):
        add_task(self.incomplete_tasks)
