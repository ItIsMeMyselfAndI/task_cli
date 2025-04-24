# Adding a new task
python task_cli.py add <description>
ex: python task_cli.py add "Buy groceries"

# Updating a task
python task_cli.py update <task ID> <new description> 
ex: python task_cli.py update id_0 "Buy groceries and cook dinner"

# Deleting a task
python task_cli.py delete <task ID> 
ex: python task_cli.py delete id_1

# Marking a task
python task_cli.py mark-todo <task ID>
ex: python task_cli.py mark-todo id_2

python task_cli.py mark-in-progress <task ID>
ex: python task_cli.py mark-in-progress id_2

python task_cli.py mark-done <task ID>
ex: python task_cli.py mark-done id_2

# Listing tasks
python task_cli.py list

# Listing tasks by status
python task_cli.py list done
python task_cli.py list todo
python task_cli.py list in-progress