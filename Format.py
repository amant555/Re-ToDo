from typing import List


def numeric_listing_of_tasks(task_list: List) -> str:
    msg = ""
    task_number = 1
    for task in task_list:
        msg += "\n" + str(task_number) + ". " + task
        task_number += 1
    return msg


def console_format(todo) -> str:

    content = ""
    text_incomplete = "Incomplete Tasks:"
    text_complete = "Complete Tasks:"
    if todo.incomplete_tasks:
        content += text_incomplete + numeric_listing_of_tasks(todo.incomplete_tasks) + "\n"
    if todo.completed_tasks:
        content += text_complete + numeric_listing_of_tasks(todo.completed_tasks) + "\n"
    if not todo.incomplete_tasks and not todo.completed_tasks:
        content = "Your TODO list is empty!"
    return content
