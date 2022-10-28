from Task import Task
import taskList

import help_command

tasks = taskList.createTaskList(0)

def readCommand(command):

    if command != "":

        if command[0] == "/":

            if command == "/help":
                print(help_command.help_text)

            if command == "/":
                print("Empty command")

            elif command == "/task -create":
                tmp = Task.newTask(input("Enter the header\n"))
                taskList.addTask(tmp, tasks)

            elif command == "/taskList -show":
                taskList.show(tasks)

            elif command == "/task -search":
                task = taskList.searchTask(input("Enter task name:\n"), tasks)
                task.printAll()

            else:
                print("Command not exist: \"" + command + "\"")

        else:
            print("not a command")