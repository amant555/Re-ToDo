from typing import List


def accept_task():
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
