from Task import Task
import taskList

import help_command

tasks = taskList.createTaskList(0)

def readCommand(command):

    if command != "":

        if command[0] == "/":

            #++++++++++++++++++++++++++++++++++++++++

            if command == "/help":
                print(help_command.help_text)

            elif command == "/task -create":
                task = Task.newTask(input("Enter the header\n")) # create task obj
                body = input("Body: ")
                date = input("Date: ")
                time = input("Time: ")
                task.fill(body,date,time) # fill the task fields
                taskList.addTask(task, tasks) # append task to  taskList
                print("Task: \"" + task.header + "\" was create")

            elif command == "/taskList -show":
                taskList.show(tasks)

            elif command == "/task -status -change":
                header = input("Enter a task header: \n")
                task = taskList.searchTask(header, tasks)
                if task != None:
                    task.changeStatus()
                    print(str(not task.status) + " changed on " + str(task.status))
                else: print("Task \"" + header + "\" not found")

            elif command == "/task -search":
                header = input("Enter task header:\n")
                task = taskList.searchTask(header, tasks)
                if task != None:
                    task.printAll()
                else:
                    print("Task \"" + header + "\" not found")

            #++++++++++++++++++++++++++++++++++++++++

            else:
                print("Command not exist: \"" + command + "\"")

        else:
            print("\"" + command + "\" is not a command")