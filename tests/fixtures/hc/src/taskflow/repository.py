from __future__ import annotations

from typing import Dict, Iterable

from .models import Task


class InMemoryTaskRepository:
    def __init__(self) -> None:
        self._items: Dict[int, Task] = {}
        self._next_id = 1

    def create(self, title: str) -> Task:
        task = Task(id=self._next_id, title=title)
        self._items[task.id] = task
        self._next_id += 1
        return task

    def list_all(self) -> Iterable[Task]:
        return list(self._items.values())

    def get(self, task_id: int) -> Task | None:
        return self._items.get(task_id)

    def delete(self, task_id: int) -> bool:
        if task_id not in self._items:
            return False
        del self._items[task_id]
        return True
