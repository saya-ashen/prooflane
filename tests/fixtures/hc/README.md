# taskflow-core

`taskflow-core` is a small in-memory task manager used for examples and local tools.

## What it does

- create a task with non-empty title
- list tasks
- mark a task as done
- delete a task by id

## What it does not do

- no persistence (data resets on process restart)
- no concurrency guarantees
- no auth or API server

## Run tests

```bash
python -m pip install -e .
pytest -q
```

## Notes

The code favors explicit errors and typed interfaces over extra features.
