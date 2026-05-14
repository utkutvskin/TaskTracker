# Task Tracker CLI

A simple command-line tool to manage your tasks. Built with Python, no external dependencies.

## Requirements

- Python 3

## Usage

```bash
python task_cli.py <command> [arguments]
```

## Commands

| Command | Description |
|---|---|
| `add "description"` | Add a new task |
| `update <id> "description"` | Update a task's description |
| `delete <id>` | Delete a task |
| `mark-done <id>` | Mark a task as done |
| `mark-in-progress <id>` | Mark a task as in progress |
| `list` | List all tasks |
| `list todo` | List tasks with status: todo |
| `list done` | List tasks with status: done |
| `list in-progress` | List tasks with status: in progress |

## Examples

```bash
python task_cli.py add "Buy groceries"
# Task added successfully: Buy groceries

python task_cli.py list
# [1] Buy groceries (todo) - 2026-05-14T21:21:00

python task_cli.py mark-done 1
# Task: Buy groceries marked as done.

python task_cli.py list done
# [1] Buy groceries (done) - 2026-05-14T21:21:00

python task_cli.py delete 1
# Buy groceries deleted successfully.
```

## Task Properties

Each task is stored in `tasks.json` with the following fields:

- `id` — unique identifier
- `description` — task description
- `status` — `todo`, `in-progress`, or `done`
- `createdAt` — creation timestamp
- `updatedAt` — last update timestamp

https://roadmap.sh/projects/task-tracker
