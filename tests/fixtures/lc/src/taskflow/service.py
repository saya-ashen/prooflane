from .models import make_task
from . import storage


def create_task(title):
    if title is None:
        title = ""
    if title == "":
        title = "untitled"
    task_id = len(storage.all_items()) + 1
    task = make_task(task_id, title)
    task["meta"]["source"] = "service"
    return storage.insert(task)


def get_tasks(include_done=True):
    out = []
    for task in storage.all_items():
        if include_done:
            out.append(task)
        else:
            if task["done"] is False:
                out.append(task)
    return out


def mark_done(task_id):
    try:
        task_id = int(task_id)
    except Exception:
        return {"ok": False, "error": "bad id"}

    task = storage.find_by_id(task_id)
    if task is None:
        return {"ok": False, "error": "missing"}
    task["done"] = True
    return {"ok": True, "task": task}


def purge(task_id):
    result = storage.remove(task_id)
    if result:
        return {"ok": True}
    return {"ok": False}
