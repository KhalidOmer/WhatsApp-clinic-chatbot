# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 14:11:35 2023

@author: Khalid Omer
"""


class Client:
    def __init__(self, user, insurance_status=False, insurance_information=""):
        self.user = user
        self.insurance_status = insurance_status
        self.insurance_information = insurance_information

    def getInsuranceStatus(self):
        return self.insurance_status

    def getInsuranceInformation(self):
        return self.insurance_information

    def getUserInformation(self):
        # infers to the User class for user information
        return self.user.getUserInformation()