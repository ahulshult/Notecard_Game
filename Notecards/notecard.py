#!/usr/bin/env python

class NotecardClass:

    def __init__(self, verb, definition):
        self.verb = verb
        self.definition = definition
        self.level = 0
        self.level_names = ["No", "Maybe", "Yes"]
        self.count = 0
    
    def getVerb(self):
        return self.verb
    
    def getDefinition(self):
        return self.definition
    
    def getLevel(self):
        return self.level
    
    def getLevelName(self):
        return self.level_names[self.level]
    
    def setLevel(self, level):
        self.level = level