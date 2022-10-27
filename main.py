import os
from Task import Task
from taskList import createTaskList, printTaskList, addTaskToList
from commands import readCommand

print("Start the program")

list = createTaskList(0)

while 1:
    command = input()

    if command == "/exit":
        break

    readCommand(command)

"""
#commented
addTaskToList(list, "Buy")

list[0].date = "02.03.2022"
list[0].body = "Need buy a ketchup"

list[0].printAll()
"""