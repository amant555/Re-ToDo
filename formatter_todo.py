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
    complete_task_length = len(todo.completed_tasks)
    incomplete_task_length = len(todo.incomplete_tasks)
    text_incomplete = "Incomplete Tasks:"
    text_complete = "Complete Tasks:"
    if incomplete_task_length == 0 and complete_task_length == 0:
        content = "Your TODO list is empty!"
    elif incomplete_task_length > 0 and complete_task_length == 0:
        content = text_incomplete + numeric_listing_of_tasks(todo.incomplete_tasks)
    elif complete_task_length > 0 and incomplete_task_length == 0:
        content = text_complete + numeric_listing_of_tasks(todo.completed_tasks)
    elif complete_task_length > 0 and incomplete_task_length > 0:
        content = text_incomplete + numeric_listing_of_tasks(todo.incomplete_tasks)
        content += "\n" + text_complete + numeric_listing_of_tasks(todo.completed_tasks)
    return content
