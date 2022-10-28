from Task import Task

def createTaskList(q):
    taskList = []
    for i in range(q):
        taskList.append(Task(header="Task " + str(i)))
    return taskList

def addTask(task, taskList):
    taskList.append(task)

def show(taskList):
    for task in taskList:
        print(task.header)

def searchTask(header, tasks):
    for task in tasks:
        if task.header.lower() == header.lower():
            return task