# Adding a new task
python task_cli.py add ``<description>`
```bash
python task_cli.py add "Buy groceries"
```

# Updating a task
python task_cli.py update `<task ID>` `<new description>` 
```bash
python task_cli.py update id_0 "Buy groceries and cook dinner"
```

# Deleting a task
python task_cli.py delete `<task ID>` 
```bash
python task_cli.py delete id_1
```

# Marking a task
python task_cli.py mark-todo `<task ID>`
```bash
python task_cli.py mark-todo id_2
```

python task_cli.py mark-in-progress `<task ID>`
```bash
python task_cli.py mark-in-progress id_2
```

python task_cli.py mark-done `<task ID>`
```bash
python task_cli.py mark-done id_2
```

# Listing tasks
```bash
python task_cli.py list
```

# Listing tasks by status
```bash
python task_cli.py list done
```
```bash
python task_cli.py list todo
```
```bash
python task_cli.py list in-progress
```