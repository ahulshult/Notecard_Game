#!/usr/bin/env python
import pytest
import coverage
from notecard import NotecardClass
from stack import StackClass
def test_create_stack():
    stack = StackClass()
    assert stack.getStackCount() == 0
   
def test_incorrect_stack():
    with pytest.raises(TypeError):
        stack = StackClass('Hello')

def test_stack_count():
    stack = StackClass()
    note = NotecardClass("verb", "definition")
    stack.addNotecard(note)
    assert stack.getStackCount() == 1

def test_return_stack():
    note = NotecardClass("verb", "definition")
    stack = StackClass()
    stack.addNotecard(note)
    assert stack.getAllNotecards() == [note]

def test_get_notecard():
    note = NotecardClass("verb", "definition")
    stack = StackClass()
    stack.addNotecard(note)
    assert stack.getNotecard(0) == note

def test_delete_notecard():
    note = NotecardClass("verb", "definition")
    stack = StackClass()
    stack.addNotecard(note)
    assert stack.deleteNotecard(note) == 0

def test_delete_invalid_notecard():
    note = NotecardClass("verb", "definition")
    stack = StackClass()
    assert stack.deleteNotecard(note) == 1

def test_count_decrement():
    note = NotecardClass("verb", "definition")
    stack = StackClass()
    stack.addNotecard(note)
    stack.deleteNotecard(note)
    assert stack.getStackCount() == 0

@pytest.mark.testthis
def test_print_stack():
    note = NotecardClass("verb", "definition")
    stack = StackClass()
    stack.addNotecard(note)
    output = "0: verb, definition \n"
    output = output + "Total printed: 1. Total in stack: 1"
    o = stack.printStack()
    assert o == output

def test_getPrevNum():
        stack = StackClass()
        assert stack.getPrevNoteIndex() == 0

def test_setPrevNum():
        stack = StackClass()
        stack.setPrevNoteIndex(3)
        assert stack.getPrevNoteIndex() == 3

def test_getCurNoteIndex():
        stack = StackClass()
        assert stack.getCurNoteIndex() == 0

def test_setCurNoteIndex():
        stack = StackClass()
        stack.setCurNoteIndex(3)
        assert stack.getCurNoteIndex() == 3

@pytest.mark.test_random
def test_getRandomNumber():
        stack = StackClass()
        stack.addNotecard(NotecardClass("v0", "d0"))
        stack.addNotecard(NotecardClass("v1", "d1"))
        number = stack.getRandomNumber()
        assert number <= (stack.getStackCount()-1)
        assert number >= 0
        assert number != 0

@pytest.mark.test_random
def test_getRandomNotecard():
        stack = StackClass()
        note = NotecardClass("v0", "d0")
        stack.addNotecard(NotecardClass("v2", "d2"))
        stack.addNotecard(NotecardClass("v1", "d1"))
        stack.addNotecard(note)
        stack.setPrevNoteIndex(2)
        assert stack.getRandomNotecard() != stack.getNotecard(2)