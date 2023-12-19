# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 14:01:56 2023

@author: Khalid Omer
"""

class Appointment:
    def __init__(self, workingSchedule, appointmentId):
        self.workingSchedule = workingSchedule
        self.appointmentId = appointmentId

    def getWorkingSchedule(self):
        return self.workingSchedule

    def getAvailSpot(self):
        pass

    def bookAppo(self, doctorId, patientId, appoTime):
        pass

    def updateAppo(self):
        pass

    def cancelAppo(self):
        pass

    def getAppoId(self):
        return self.appointmentId
