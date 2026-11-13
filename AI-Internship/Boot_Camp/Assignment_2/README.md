# Mini Task Tracker
AI Engineering Bootcamp | Assignment-02

**Student:** Mahwish Arooj  |  **Training ID:** TRN-2026-002056
**GitHub repository:** https://github.com/m-arooj/Internship-Projects/tree/main/AI-Internship/Boot_Camp/Assignment_2

## What is inside

A menu-based task manager written in Python. Tasks are saved in a JSON file (`tasks.json`), so they are still there the next time you run the program.

Built for **AI Engineering | Week 1, Day 2** (Mini Project: Build a Task Tracker).

## Features

| Menu option | What it does |
|---|---|
| **1. Add** | Asks for a title and stores the task as *Pending* |
| **2. View** | Shows a numbered list, each task marked `[Pending]` or `[Done]` |
| **3. Complete** | Marks the chosen task number as done |
| **4. Delete** | Removes the chosen task number |
| **5. Exit** | Leaves the program (the menu repeats until you choose this) |

- **Save and load:** the list is saved to `tasks.json` with `json.dump()` after every add, complete and delete, and loaded with `json.load()` at startup.
- **Error handling:** empty titles, invalid menu choices, invalid task numbers (letters, 0, or too large) and a missing or damaged `tasks.json` are all handled with a clear message instead of a crash.

Each task is stored like this:

```json
{"title": "Read notes", "done": false}
```

## How to run

**On your computer**
```bash
python mini_task_tracker.py
```
`tasks.json` is created in the same folder the first time you add a task.

**In Google Colab**
1. Upload `mini_task_tracker.py`, or paste its code into a cell.
2. Run the cell and use the menu.
3. Run the cell again in the same runtime to see your saved tasks reload.

> Files in a Colab runtime are temporary. Download `tasks.json` or save it to Google Drive to keep your tasks permanently.

## Sample session

```
--- TASK TRACKER ---

1. Add   2. View   3. Complete   4. Delete   5. Exit
Choice: 1
Task title: Read notes
Task added.
Choice: 2
1. Read notes [Pending]
Choice: 3
Task number: 1
Task completed.
Choice: 2
1. Read notes [Done]
Choice: 5
Goodbye!
```

## Code structure

`load_tasks()`, `save_tasks()`, `add_task()`, `view_tasks()`, `complete_task()` and `delete_task()` each do one job. A `while True` loop in `main()` shows the menu until Exit is chosen.
