# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 14:09:43 2023

@author: Khalid Omer
"""

class User:
    def __init__(self, name, user_id, address=None, email=None, phone=None):
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.user_id = user_id

    def getUserInformation(self):
        return {
            "Name": self.name,
            "Address": self.address,
            "Email": self.email,
            "Phone": self.phone,
            "ID": self.user_id
        }

    def updateInformation(self, name=None, address=None, email=None, phone=None):
        if name:
            self.name = name
        if address:
            self.address = address
        if email:
            self.email = email
        if phone:
            self.phone = phone