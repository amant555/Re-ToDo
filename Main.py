import os
import sys
from formatter_todo import console_format
from ToDoList import ToDoList

todo = ToDoList(console_format)
path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
save_file = path + "/MyTasks.txt"


def invalid():
    print("Invalid option")


def view_tasks():
    todo.view_and_save_tasks(sys.stdout)


def save_task():
    todo.view_and_save_tasks(save_file)


def task_options(i):
    switcher = {
        1: todo.add_task,
        2: view_tasks,
        3: todo.mark_completed,
        4: save_task,
    }
    return switcher.get(i, invalid)()


def main():
    global todo
    todo = ToDoList(console_format)
    options = """
    0. Exit
    1. Add task
    2. View task
    3. Mark a task as complete
    4. Save list to file
    """
    while 1:
        try:
            print(options)
            option = int(input("Enter option to proceed: "))
            if option == 0:
                break
            task_options(option)
        except ValueError:
            print("Invalid option")


if __name__ == '__main__':
    main()
