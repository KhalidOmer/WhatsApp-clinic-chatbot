"""
Created on Tue Dec 19 13:00:42 2023

@author: Sediqe
"""
import itertools
import DoctorClass
class Appointment:
    
    def __init__(self, workingSchedule, doctors):
        self.workingSchedule = workingSchedule
        self.doctors = doctors # list of doctor from doctor class
        self.availableSpot = {doctors[0]:['dd/mm:8-9', 'dd/mm:9-10', 'dd/mm:10:15-11:15','dd/mm:11:15-12'],
                              doctors[1]:['dd/mm:8-9', 'dd/mm:9-10', 'dd/mm:10:15-11:15','dd/mm:11:15-12'],
                              doctors[2]:['dd/mm:8-9', 'dd/mm:9-10', 'dd/mm:10:15-11:15','dd/mm:11:15-12'],
                              }
        self.appoList = {}
        
    def getWorkingSchedule(self):
        return self.workingSchedule

    def getAvailSpot(self):
        return self.availableSpot

    """ We have a schedule, then the client books an appointment, then the working schedule will updated, when another client wishes to make an appointment, 
    only the remaining spots will be shown, the function takeAppo does this job, updating the working schedule
    """ 
       
    def takeAppo(self):
        availableSpot = self.getAvailSpot()
        print("Please choose the doctor")
        print(self.doctors)
        chosenDoctor = input("type your doctor name: ").lower().strip()
        doctorSpot = availableSpot[chosenDoctor]
        print('These are empty spot for dr', chosenDoctor)
        print(doctorSpot)
        appoTime = input("Take a spot from the list")
        availableSpot[chosenDoctor].remove(appoTime)
        return appoTime, chosenDoctor
        
''' the function bookAppo() generates an id for the appointment and also calls the function takeApp(), and it adds the booking to the doctor schedule
and it return an appointment for the client'''

    def bookAppo(self):
        newid  = itertools.count().next
        appoTime, doctorName = self.takeAppo()
        statement1 = 'Your appointment is at : '+ str(appoTime)+ 'with' + doctorName
        statement2 = 'Your numberId is: '+ str(newid)
        self.appoList[newid]= {doctorName : appoTime}
        print(statement1)
        print(statement2)
        
'''
the function cancelAppo() takes the appointment id and then remove it from the working schedule, and adds this cleared spot to
the available spots.
'''

    def cancelAppo(self):
        paitentId = int(input('enter your id: ').strip())
        dicD = self.appoList[paitentId]
        x = dicD.getkey()
        self.availableSpot[x] = dicD[x]
        del self.appoList[paitentId]
        print('Your appointment is cancelled')
        
