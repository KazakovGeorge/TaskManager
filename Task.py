import datetime


class Task():
    def __init__(self, header):
        """init task"""
        self.header = header
        self.body = ""
        self.status = False
        self.date = ""
        self.time = ""

    def newTask(header):
        return Task(header=header)

    def printAll(self):
        print("Header: " +  self.header, "\n","Body: " + self.body, "\n", "Date: " + self.date, "\n", "Time: " +  self.time)

    def changeHeader(self):
        self.header = "Changed"