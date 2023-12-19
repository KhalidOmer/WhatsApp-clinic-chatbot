# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 15:32:22 2023

@author: Khalid Omer
"""

class Bot:
    def __init__(self, botId, botName, commandList):
        self.botId = botId
        self.botName = botName
        self.commandList = commandList

    def getbotId(self):
        return self.botId

    def getbotName(self):
        return self.botName

    def interpretMessages(self, user_input):
        if user_input in self.commandList:
            response = self.commandList[user_input]
            return response
        else:
            return "Sorry, I don't understand that could rephrase."
