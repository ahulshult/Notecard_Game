#!/usr/bin/env python
import pytest
import coverage
from notecard import NotecardClass


def test_level_name_two():
    note = NotecardClass("cool", "cause")
    note.setLevel(2)
    assert note.getLevelName() == "Yes" 

def test_set_level():
    note = NotecardClass("it", "said")
    note.setLevel(1)
    assert note.getLevel() == 1

def test_too_few_args():
    with  pytest.raises(TypeError):
        note = NotecardClass("moo")

def test_no_args():
    with pytest.raises(TypeError):
        note = NotecardClass()

def test_too_many_args():
    with pytest.raises(TypeError):
        note = NotecardClass("thats", "the", "end")
