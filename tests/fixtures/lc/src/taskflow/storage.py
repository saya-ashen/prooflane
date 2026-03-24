_TASKS = []


def insert(task):
    _TASKS.append(task)
    return task


def all_items():
    return _TASKS


def find_by_id(task_id):
    for task in _TASKS:
        if task["id"] == task_id:
            return task
    return None


def remove(task_id):
    idx = 0
    for task in _TASKS:
        if task["id"] == task_id:
            del _TASKS[idx]
            return True
        idx += 1
    return False
