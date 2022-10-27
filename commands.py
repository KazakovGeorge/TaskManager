import Task
import taskList


def readCommand(command):

    if command[0] == "/":

        if command == "/":
            print("Empty command")
        elif command == "/xyi":
            print("Haha. it's funny")

        else:
            print("Command not exist: \"" + command + "\"")

    else:
        print("not a command")