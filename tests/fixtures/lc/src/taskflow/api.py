from . import service


def add_task(payload):
    if isinstance(payload, dict):
        title = payload.get("title", "")
    else:
        title = payload
    return service.create_task(title)


def list_tasks(include_done=True):
    return service.get_tasks(include_done=include_done)


def complete_task(task_id):
    return service.mark_done(task_id)


def delete_task(task_id):
    return service.purge(task_id)
