# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 10:44:50 2023

@author: Sediqe
"""

class Clinic:
    
    def __init__(self, services, doctors, adressInformation, workingHours):
        self.services = services
        self.doctors = doctors # An instance of doctor class
        self.adressInformation = adressInformation
        self.workingHours = workingHours
        self.acceptedInsurances = []
    
    def getServices(self):
        return self.services

    def getWorkingHours(self):
        return self.workingHours

    def getDoctors(self):
        return self.doctors
    
    def getAdressInformation(self):
        return self.adressInformation
    
    def getInsurance(self):
        return self.acceptedInsurances

    def updateServices(self,  newService):
        pass

    def updateAdressInfo(self, newInformation):
        pass

    def removeService(self, service):
        return self.services.remove(service)
        

    def addService(self, newService):
        return self.service.append(newService)
    
    def checkinsurancePlan(self, insurancePlan):
        if insurancePlan in self.acceptedInsurances:
            return True
        else:
            return False
        
    def addInsurance(self, newInsurance):
        return self.acceptedInsurances.append(newInsurance)
        
    
    def removeInsurance(self, insurance):
        return self.acceptedInsurances.remove(insurance)
        

