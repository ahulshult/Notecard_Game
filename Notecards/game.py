#!/usr/bin/env python
import io
import os
import random
from notecard import NotecardClass
from stack import StackClass

class GameClass: 

    def __init__(self):
        self.correctStack = StackClass()
        self.incorrectStack = StackClass()
        self.setUpDone = False
        #self.currentNotecard

    def setUp(self, file):
        self.file = file
        lines = self.openFile()
        self.parseFile(lines)
        self.setUpDone = True
        self.currentNotecard = self.incorrectStack.getNotecard(0)

    def play(self):
        if self.setUpDone != True:
            print("Error. Game was either incorrectly setup or not set up. Please read the README.md and try again. \n Exiting...")
            exit(-1)
        correct_input = False
        print("welcome! \n This is a flashcard game to learn and study Italian verbs. \n")
        print("At any point in this game that you want to quit, press 'Q' and then <Enter>. \n")
        print("To start, press 1 and then <Enter>.")

        while(not correct_input):
            user = input()
            self.checkQuit(user)
            if user == "1":
                count = 0
                correct_input = True
                
                while(self.incorrectStack.getStackCount() > 0):
                    if count > (self.incorrectStack.getStackCount() - 1):
                        count = 0
                    self.currentNotecard = self.incorrectStack.getNotecard(count)
                    print(self.currentNotecard.getVerb())
                    cont = self.checkInput(self.currentNotecard.getDefinition())                     
                    if cont == True:
                        print("Correct!")
                        if self.currentNotecard.getLevel() == 0:
                            self.currentNotecard.setLevel(1)
                        elif self.currentNotecard.getLevel() == 1:
                            self.currentNotecard.setLevel(2)
                            self.addToCorrectStack(self.currentNotecard)
                            self.deleteFromIncorrectStack(self.currentNotecard)
                    else:
                        print("Incorrect")
                        if self.currentNotecard.getLevel() == 1:
                            self.currentNotecard.setLevel(0)
                        elif self.currentNotecard.getLevel() == 2:
                            self.currentNotecard.setLevel(1)
                    count += 1    
                          
            else:
                print("Please enter 1 to start or Q to quit.") 
    
    def openFile(self):
        if not os.path.isfile(self.file):
            raise FileNotFoundError
        else:
            try:
                f = open(self.file)
                lines = f.read().split()
                return lines
            except OSError as e:
                raise OSError
                print (e)
        return
    
    def parseFile(self, lines):
        definition = ""
        verb = False
        for word in lines:
            if verb == True:
                self.incorrectStack.addNotecard(NotecardClass(word, definition))
                verb = False
            else:
                definition = word
                verb = True 

    def getCurrentNotecard(self):
        return self.currentNotecard

    def getNextNotecard(self):
        curIndex = self.incorrectStack.getCurNoteIndex()
        if curIndex < (self.incorrectStack.getStackCount()-1):
             curIndex += 1
             self.currentNotecard = self.incorrectStack.getNotecard(curIndex)
        
        else:
            curIndex = 0
            self.currentNotecard = self.incorrectStack.getNotecard(curIndex)
        self.incorrectStack.setCurNoteIndex(curIndex)    
        return self.currentNotecard
    
    def getPreviousNotecard(self):
        curIndex = self.incorrectStack.getCurNoteIndex()
        if curIndex == 0:
            curIndex = self.incorrectStack.getStackCount() - 1
        else:
            curIndex -= 1
            
        self.currentNotecard = self.incorrectStack.getNotecard(curIndex)
        self.incorrectStack.setCurNoteIndex(curIndex)    
        return self.currentNotecard

    def getNextNotecardRand(self):
        self.currentNotecard = self.incorrectStack.getRandomNotecard()
        return self.currentNotecard

    def checkInput(self, answer):
        #user = input()
        #self.checkQuit(user)
        definition = self.currentNotecard.getDefinition()
        if answer == definition:
            return True
        else:
            return False

    def addToIncorrectStack(self, notecard):
        self.incorrectStack.addNotecard(notecard)

    def addToCorrectStack(self, notecard):
        self.correctStack.addNotecard(notecard)
    
    def deleteFromIncorrectStack(self, notecard):
        self.incorrectStack.deleteNotecard(notecard)
    
    def deleteFromCorrectStack(self, notecard):
        self.correctStack.deleteNotecard(notecard)
    
    def getIncorrectStack(self):
        return self.incorrectStack
    
    def getCorrectStack(self):
        return self.correctStack

    def printIncorrectStack(self):
        self.incorrectStack.printStack()
    
    def printCorrectStack(self):
        self.correctStack.printStack()
    
    def getFile(self):
        return self.file
    
    def setFile(self, file):
        self.file = file
        return

    def checkQuit(self, user):
        if user == "Q" or user == "q":
            print("'Q' entered. Exiting...")
            exit(0)
        return