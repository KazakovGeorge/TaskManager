from Task import Task
from taskList import createTaskList, printTaskList, addTaskToList

list = createTaskList(0)
printTaskList(list)

addTaskToList(list, "Buy")

list[0].date = "02.03.2022"
list[0].body = "Need buy a ketchup"

list[0].printAll()
