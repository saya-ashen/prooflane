from __future__ import annotations

from .models import Task
from .repository import InMemoryTaskRepository


class TaskValidationError(ValueError):
    pass


class TaskService:
    def __init__(self, repo: InMemoryTaskRepository | None = None) -> None:
        self._repo = repo or InMemoryTaskRepository()

    def create_task(self, title: str) -> Task:
        normalized = title.strip()
        if not normalized:
            raise TaskValidationError("title must not be empty")
        return self._repo.create(normalized)

    def list_tasks(self) -> list[Task]:
        return list(self._repo.list_all())

    def complete_task(self, task_id: int) -> Task:
        task = self._repo.get(task_id)
        if task is None:
            raise KeyError(f"task {task_id} not found")
        task.done = True
        return task

    def delete_task(self, task_id: int) -> bool:
        return self._repo.delete(task_id)
