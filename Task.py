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

    def changeStatus(self):
        self.status = not self.status

    def printAll(self):
        print("Header: " +  self.header, "\n","Body: " + self.body, "\n", "Date: " + self.date, "\n", "Time: " + self.time, "\n", "Status: " + str(self.status))

    def fill(self, body, date, time):
        self.body = body
        self.date = date
        self.time = time
