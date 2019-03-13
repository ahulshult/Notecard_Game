#!/usr/bin/env python
import pytest
import coverage
from notecard import NotecardClass

def test_check_verb():
    note = NotecardClass("wow", "mom")
    assert note.getVerb() == "wow"

def test_check_def():
    note = NotecardClass("I", "saw")
    assert note.getDefinition() == "saw"

def test_prelim_level():
    note = NotecardClass("a", "cow")
    assert note.getLevel() == 0

def test_level_name_zero():
    note = NotecardClass("mom", "and")
    note.setLevel(0)
    assert note.getLevelName() == "No"

def test_level_name_one():
    note = NotecardClass("it", "was")
    note.setLevel(1)
    assert note.getLevelName() == "Maybe"
