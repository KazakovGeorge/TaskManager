import datetime


class Task():
    def __init__(self, header):
        """init task"""
        self.header = header
        self.body = ""
        self.status = False
        self.date = ""
        self.time = ""

    def printAll(self):
        print(self.header, "\n", self.body, "\n", self.date, "\n", self.time)

    def changeHeader(self):
        self.header = "Changed"