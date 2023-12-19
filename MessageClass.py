# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 14:24:47 2023

@author: Khalid Omer
"""

class Message:
    def __init__(self, messageId, senderId, receiverId, timestamp, content):
        self.messageId = messageId
        self.senderId = senderId
        self.receiverId = receiverId
        self.timestamp = timestamp
        self.content = content

    def getMessageId(self):
        return self.messageId

    def getSenderId(self):
        return self.senderId
    
    def getReceiverId(self):
        return self.receiverId
    def getTimestamp(self):
        return self.timestamp

    def getContent(self):
        return self.content

    def sendMessage(self):
        #I think this has to do with bot class 
        pass

    def receiveMessage(self):
        #This is the same as the sendMessage method
        pass
