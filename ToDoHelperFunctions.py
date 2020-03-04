import pickle


def accept_task() -> str:
    task_head = input("Enter the task: ")
    task_body = input()
    task = task_head + "\n" + task_body
    return task.strip()


def save_to_file(file: str or object, content: str) -> None:
    if type(file) == str:
        with open(file, 'w') as file:
            file.write(content)
    else:
        file.write(content)


def load_session():
    try:
        with open("dump.pkl", 'rb') as dump_handler:
            data = pickle.load(dump_handler)
        completed_tasks = data["completed_tasks"]
        incomplete_tasks = data["incomplete_tasks"]
    except FileNotFoundError:
        completed_tasks = []
        incomplete_tasks = []
    return incomplete_tasks, completed_tasks
