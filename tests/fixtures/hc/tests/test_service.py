import pytest

from taskflow.service import TaskService, TaskValidationError


def test_create_task_rejects_empty_title():
    service = TaskService()
    with pytest.raises(TaskValidationError):
        service.create_task("   ")


def test_complete_task_marks_done():
    service = TaskService()
    task = service.create_task("read docs")
    done = service.complete_task(task.id)
    assert done.done is True


def test_delete_task_returns_false_for_missing_task():
    service = TaskService()
    assert service.delete_task(999) is False
