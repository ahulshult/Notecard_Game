#!/usr/bin/env python
import random
from notecard import NotecardClass


class StackClass:

    def __init__(self):
        self.count = 0
        self.stack = []
        self.prevNote = 0
        self.curNote = 0

    def addNotecard(self, notecard):
        self.stack.append(notecard)
        self.count += 1
    
    def getNotecard(self, index):
        return self.stack[index]
    
    def getAllNotecards(self):
        return self.stack

    def getStackCount(self):
        return self.count

    def deleteNotecard(self, notecard):
        for notecards in self.stack:
            if notecards.getVerb() == notecard.getVerb():
                self.stack.remove(notecard)
                self.count -= 1
                return 0
        return 1
    
    def getStack(self):
        return self.stack
    
    def getRandomNotecard(self):
        number = self.getRandomNumber()
        self.setPrevNoteIndex(self.curNote)
        self.setCurNoteIndex(number)
        return self.getNotecard(number)

    def getPrevNoteIndex(self):
        return self.prevNote

    def setPrevNoteIndex(self, num):
        self.prevNote = num
        return

    def getCurNoteIndex(self):
        return self.curNote
    
    def setCurNoteIndex(self, num):
        self.curNote = num
        return

    def printStack(self):
        count = 0
        output = ""
        for notecards in self.stack:
            verb = notecards.getVerb()
            definition = notecards.getDefinition()
            output += ("%s: %s, %s \n" % (count, verb , definition ) )
            count += 1
        output += ("Total printed: %s. Total in stack: %s" % (count, self.getStackCount()))
        print (output)
        return output

    def getRandomNumber(self):
        count = self.getStackCount()-1
        if count == 0:
            return 0
        number = random.randint(0, count)
        while number == self.curNote:
            number = random.randint(0, count)
        print('CurNote %s, rand %s' % (self.curNote, number))
        return number