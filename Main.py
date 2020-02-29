import sys
from formatter_todo import console_format
from ToDoList import ToDoList

todo = ToDoList(console_format)


def invalid():
    print("Invalid option")


def view_tasks():
    todo.view_and_save_tasks(sys.stdout)


def task_options(i):
    switcher = {
        1: todo.add_task,
        2: view_tasks,
    }
    return switcher.get(i, invalid)()


def main():
    global todo
    todo = ToDoList(console_format)
    options = """
    0. Exit
    1. Add task
    2. View task
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
