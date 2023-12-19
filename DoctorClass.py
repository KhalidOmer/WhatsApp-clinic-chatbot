# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 14:05:32 2023

@author: Khalid Omer
"""

class Doctor:
    def __init__(self, doctorId, name, specialty, schedule, services):
        self.doctorId = doctorId
        self.name = name
        self.specialty = specialty
        self.schedule = schedule
        self.services = services

    def getSpeciality(self):
        return self.specialty

    def getSchedule(self):
        return self.schedule

    def getServices(self):
        return self.services

    def updateSchedule(self, newSchedule):
        self.schedule = newSchedule

