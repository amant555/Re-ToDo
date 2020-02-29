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
