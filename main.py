# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 22:00:35 2023

@author: Khalid Omer
"""

import UserClass
import BotClass 
import MessageClass
import DoctorClass  
import ClientClass
import appointment
import clinic

# create instances of each of these classes

#create an instance or the user class 
user = UserClass(name="John Doe", user_id=1, address="123 Main St", email="john@example.com", phone="123-456-7890")
# create an instace of the client class 
client = ClientClass(user, insurance_status=True, insurance_information="Health insurance - Plan A")
#create an instance of the doctors class 
doctor_1 = DoctorClass("Dr. Smith", "Dentist") 
doctor_2 = DoctorClass("Dr. Salma", "Dentist")
doctor_3 = DoctorClass("Dr. Amr", "Dentist")
schedule = {doctor_1:['dd/mm:8-9', 'dd/mm:9-10', 'dd/mm:10:15-11:15','dd/mm:11:15-12'],
                              doctor_2:['dd/mm:8-9', 'dd/mm:9-10', 'dd/mm:10:15-11:15','dd/mm:11:15-12'],
                              doctor_3:['dd/mm:8-9', 'dd/mm:9-10', 'dd/mm:10:15-11:15','dd/mm:11:15-12'],
                              }




booking_1 = appointment.bookAppo()





