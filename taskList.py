from Task import Task

def createTaskList(q):
    taskList = []
    for i in range(q):
        taskList.append(Task(header="Task " + str(i)))
    return taskList

def addTaskToList(taskList, header):
    taskList = taskList.append(Task(header=header))

def printTaskList(taskList):
    for task in taskList:
        print(task.header)
    print("\n")