from __future__ import annotations

from .service import TaskService


class TaskAPI:
    def __init__(self, service: TaskService | None = None) -> None:
        self._service = service or TaskService()

    def add_task(self, title: str) -> dict:
        task = self._service.create_task(title)
        return {"id": task.id, "title": task.title, "done": task.done}

    def list_tasks(self) -> list[dict]:
        return [
            {"id": task.id, "title": task.title, "done": task.done}
            for task in self._service.list_tasks()
        ]

    def complete_task(self, task_id: int) -> dict:
        task = self._service.complete_task(task_id)
        return {"id": task.id, "title": task.title, "done": task.done}

    def delete_task(self, task_id: int) -> bool:
        return self._service.delete_task(task_id)
