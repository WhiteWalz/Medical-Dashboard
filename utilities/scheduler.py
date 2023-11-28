

class doctorDay:
    
    def __init__(self, doctorID, startTime, endTime):
        self.id = doctorID
        self.start = startTime
        self.end = endTime

    def __init__(self, doctorID):
        self.id = doctorID
        self.start = 0
        self.end = 0

class employeeDay:

    def __init__(self, employeeID, maxHours):
        self.id = employeeID
        self.maxHours = maxHours

    def __init__(self, employeeID):
        self.id = employeeID
        self.maxHours = 0