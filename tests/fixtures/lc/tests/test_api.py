from taskflow.api import add_task, complete_task, list_tasks


def test_create_and_complete_happy_path():
    created = add_task({"title": "learn skill"})
    assert created["title"] == "learn skill"

    done = complete_task(created["id"])
    assert done["ok"] is True


def test_list_tasks_returns_data():
    data = list_tasks()
    assert isinstance(data, list)
