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
                header = Task.newTask(input("Enter the header\n"))
                taskList.addTask(header, tasks)
                print("Task: \"" + header + "\" was create")

            elif command == "/taskList -show":
                taskList.show(tasks)

            elif command == "/task -search":
                header = input("Enter task name:\n")
                task = taskList.searchTask(header, tasks)
                if task != None:
                    task.printAll()
                else:
                    print("Task \"" + header + "\" not found")

            else:
                print("Command not exist: \"" + command + "\"")

        else:
            print("not a command")