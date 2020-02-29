import sys
from typing import List


def accept_task() -> str:
    task_head = input("Enter the task: ")
    task_body = input()
    task = task_head + "\n" + task_body
    return task.strip()


def add_task(target_list: List) -> str or None:
    task = accept_task()
    if task:
        target_list.append(task)
    else:
        print("Empty Task")


def save_to_file(file_name: str or object, content: str) -> None:
    try:
        with open(file_name, 'w') as file:
            file.write(content)
    except TypeError:
        file_name.write(content)


def mark_as_complete(target_list):
    task_number = int(input("Enter the task number of task to be marked as completed: "))
    if task_number < 1 or task_number > len(target_list.incomplete_tasks):
        message = "\nThe task you're trying to mark is not present in the list"
        save_to_file(sys.stdout, message)
    else:
        target_list.completed_tasks.append(target_list.incomplete_tasks[task_number - 1])
        del target_list.incomplete_tasks[task_number - 1]
