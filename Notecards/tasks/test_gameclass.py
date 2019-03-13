#!/usr/bin/env python
import pytest
import coverage
from unittest import mock
from notecard import NotecardClass
from stack import StackClass
from game import GameClass

def test_game_init():
    game = GameClass()

def test_game_setup():
    """ set up sub-functions tested in test_filereader"""
    game = GameClass()
    game.setUp(r'C:\Users\j51780\Documents\Notecards\words.txt')

def test_initialSetupFail():
    game = GameClass()
    with pytest.raises(SystemExit) as cm:
        game.play()
    assert cm.type == SystemExit 

@pytest.mark.test_parsefile
def test_parseFile():
    game = GameClass()
    game.setUp(r'C:\Users\j51780\Documents\Notecards\test_files\words_test.txt')
    stack = StackClass()
    stack.addNotecard(NotecardClass("accettare", "accept"))
    stack.addNotecard(NotecardClass("permettere", "allow"))
    assert stack.printStack() == game.incorrectStack.printStack()

def test_getIncorrectStack():
    """only checks for error. look at test_addToIncorrectStack"""
    game = GameClass()
    game.getIncorrectStack()

def test_addToIncorrectStack():
    """tests addToIncoreectStack and getIncorrectStack"""
    note = NotecardClass("verb", "definition")
    stack = StackClass()
    stack.addNotecard(note)
    game = GameClass()
    game.addToIncorrectStack(note)
    assert stack.getNotecard(0) == game.getIncorrectStack().getNotecard(0)

def test_getIncorrectStack():
    """only checks for error. look at test_addCncorrectStack"""
    game = GameClass()
    game.getCorrectStack()

def test_addToCorrectStack():
    note = NotecardClass("verb", "definition")
    stack = StackClass()
    stack.addNotecard(note)
    game = GameClass()
    game.addToCorrectStack(note)
    assert stack.getNotecard(0) == game.getCorrectStack().getNotecard(0)

@pytest.mark.xfail
def test_callgetVerb():
    note = NotecardClass("verb", "definition")
    game = GameClass()
    game.addToIncorrectStack(note)
    verb = game.callGetVerb(0, 0)
    assert verb == "verb"

@pytest.mark.xfail
def test_callGetDefinition():
    note = NotecardClass("verb", "definition")
    game = GameClass()
    game.addToIncorrectStack(note)
    definition = game.callGetDefinition(0, 0)
    assert definition == "definition"

def test_checkInputTrue():
    game = GameClass()
    note = NotecardClass("verb", "definition")
    game.addToIncorrectStack(note)
    with mock.patch('builtins.input', return_value="definition"):
        assert game.checkInput("definition")  == True

def test_checkInputFalse():
    game = GameClass()
    note = NotecardClass("verb", "definition")
    game.addToIncorrectStack(note)
    with mock.patch('builtins.input', return_value="definition"):
        assert game.checkInput("notdefinition")  == False

def test_checkQuit():
        game=GameClass()
        with pytest.raises(SystemExit):
                game.checkQuit('q')

def test_checkQuitFalse():
        game=GameClass()
        game.checkQuit('Hello!')

def test_getPrevNum():
        game = GameClass()
        assert game.getPrevNum() == 0

def test_setPrevNum():
        game = GameClass()
        game.setPrevNum(3)
        assert game.getPrevNum() == 3
        