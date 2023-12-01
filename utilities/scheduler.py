

class DoctorDay:
    
    def __init__(self, doctorID: int, startTime: int, endTime: int):
        self.id = doctorID
        self.start = startTime
        self.end = endTime

    def __init__(self, doctorID: int):
        self.id = doctorID
        self.start = 0
        self.end = 0

class Employee:
    #   daysWorked should be a dictionary of dictionaries where the keys are the days worked, and the values are dicts where the keys are
    #       keywords like start, end, max representing the start time, end time, and max hours for a given day, in integer form.

    def __init__(self, id: int, daysWorked: dict):
        self.id = id
        self.daysWorked = daysWorked
        self.hoursWorked = 0

    def __init__(self, id: int):
        self.id = id
        self.daysWorked = dict()
        self.hoursWorked = 0

class Node:

    def __init__(self, children: list, score: float, parentContext: dict, doctors: list, employees: list):
        self.children = Node.expand(self)
        self.score = score
        self.possScore = Node.calcBestScore(self)
        self.parentContext = parentContext
        self.doctors = doctors
        self.employees = employees
