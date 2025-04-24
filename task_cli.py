import json
import os
import time
import sys


CLEAR = "cls" if os.name == "nt" else "clear"
WIDTH, HEIGHT= os.get_terminal_size() 


class Tracker:
    def __init__(self):
        self.tasksDict = self._getTasksDict()
    
    def _getTasksDict(self) -> dict:
        json_file = "tasks.json"
        if not os.path.exists(json_file):
            return {}
        with open(json_file, "r") as file:
            tasks = json.load(file)
        return tasks
    
    def _makeID(self) -> str:
        if len(self.tasksDict) == 0:
            return "id_0"
        ids_str = self.tasksDict.keys()
        ids_num = [int(task_id.split("_")[1]) for task_id in ids_str]
        last = max(ids_num)
        return f"id_{last+1}"

    def _getCurrentTime(self) -> str:
        months = {
            1:"Jan", 2:"Feb", 3:"Mar", 4:"Apr", 5:"May", 6:"Jun", 
            7:"Jul", 8:"Aug", 9:"Sep", 10:"Oct", 11:"Nov", 12:"Dec",
        }
        local = time.localtime()
        current_date = f"{months[local.tm_mon]} {local.tm_mday}, {local.tm_year}"
        current_time = f"{local.tm_hour:0>2}:{local.tm_min:0>2}:{local.tm_sec:0>2}"
        return f"{current_date} ({current_time})"

    def addTask(self, description:str) -> None:
        task_id = self._makeID()
        status = "todo"
        createdTime = self._getCurrentTime()
        self.tasksDict[task_id] = {
            "description":description,
            "status":status,
            "createdAt":createdTime,
            "updatedAt":createdTime
        }
        print(f"Task added successfully (ID: {task_id})")

    def updateTask(self, task_id:str, description:str) -> None:
        updatedTime = self._getCurrentTime()
        self.tasksDict[task_id]["description"] = description
        self.tasksDict[task_id]["updatedAt"] = updatedTime 
        print(f"Task updated successfully (ID: {task_id})")

    def deleteTask(self, task_id:str) -> None:
        del self.tasksDict[task_id]
        print(f"Task deleted successfully (ID: {task_id})")

    def markTask(self, task_id:str, mark:str) -> None:
        updatedTime = self._getCurrentTime()
        self.tasksDict[task_id]["status"] = mark
        self.tasksDict[task_id]["updatedAt"] = updatedTime 
        print(f"Task marked successfully (ID: {task_id})")

    def listTasks(self, mark=None) -> None:
        ids = self.tasksDict.keys()
        if mark:
            ids = [task_id for task_id in ids if self.tasksDict[task_id]["status"] == mark]
        print("="*WIDTH)
        print(f"{"Tasks".center(WIDTH)}")
        print("="*WIDTH + "\n")
        
        if len(ids) == 0:
            print(f"{"No available task(s).".center(WIDTH)}\n")

        for task_id in ids:
            p = self.tasksDict[task_id]
            lines = (
                f"[ID: {task_id}] - \"{p["status"]}\"\n"
                f"\tDescription: {p["description"]}\n"
                f"\tCreated: {p["createdAt"]}\n"
                f"\tUpdated: {p["updatedAt"]}\n"
            )
            print(lines)

        print("="*WIDTH)

    def updateTasksJSON(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasksDict, file, indent=4)


def isValidCommand(argv:list, ids:list) -> bool:
    statuses = ["todo", "in-progress", "done"]
    if (len(argv) == 4) and (argv[1] == "update") and (argv[2] in ids):
        return True
    elif (len(argv) == 3) and (argv[1] == "add"):
        return True
    elif (len(argv) == 3) and (argv[1] == "delete") and (argv[2] in ids):
        return True
    elif (len(argv) == 3) and (("mark" in argv[1]) and (argv[1][5:] in statuses)) and (argv[2] in ids):
        return True
    elif (len(argv) == 3) and (argv[1] == "list") and (argv[2] in statuses):
        return True
    elif (len(argv) == 2) and (argv[1] == "list"):
        return True
    return False

def main() -> None:
    tracker = Tracker()
    argv = sys.argv
    if not isValidCommand(argv, tracker.tasksDict.keys()):
        print("="*WIDTH)
        print("\n[!] Invalid command/task ID or No task available.")
        print("\tCheck README.md file for valid commands.")
        print("\tCheck tasks list for valid task ID.\n")
        print("="*WIDTH)
        return
    
    if "list" in argv:
        if len(argv) == 2:
            mark = None
        else:
            mark = argv[2]
        tracker.listTasks(mark)
    elif "add" in argv:
        description = argv[2]
        tracker.addTask(description)
    elif "update" in argv:
        task_id = argv[2]
        description = argv[3]
        tracker.updateTask(task_id, description)
    elif "delete" in argv:
        task_id = argv[2]
        tracker.deleteTask(task_id)
    elif "mark" in argv[1]:
        mark = argv[1][5:]
        task_id = argv[2]
        tracker.markTask(task_id, mark)
    
    tracker.updateTasksJSON()

if __name__ == "__main__":
    print()
    main()
    print()
   