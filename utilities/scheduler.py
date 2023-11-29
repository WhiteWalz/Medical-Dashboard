

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
    #   doctorWeights is a dictionary where the keys are doctorIDs and the values are weights based on how often the person has worked that doctor
    #       or manually set.

    def __init__(self, id: int, daysWorked: dict, doctorWeights: dict):
        self.id = id
        self.daysWorked = daysWorked
        self.doctorWeights = doctorWeights

    def __init__(self, id: int):
        self.id = id
        self.daysWorked = dict()
        self.doctorWeights = dict()