#!/usr/bin/env python
import pytest
import coverage
from game import GameClass

def test_setFile():
    game = GameClass()
    game.setFile(r'C:\Users\j51780\Documents\Notecards\test_files\test.txt')

def test_raises_exception_on_file_permissions():
    """test for permission errors on file"""
    game = GameClass()
    game.setFile(r'C:\Users\j51780\Documents\Notecards\test_files\blocked.txt')
    with pytest.raises(OSError):
        game.openFile()

def test_raises_exception_on_incorrect_files():
    """Test for wrong file name"""
    game = GameClass()
    game.setFile(r'C:\Users\j51780\Documents\Notecards\w.txt')
    with pytest.raises(FileNotFoundError):
        game.openFile()

def test_getFile():
    game = GameClass()
    game.setFile(r'C:\Users\j51780\Documents\Notecards\test_files\test.txt')
    assert game.getFile() == r'C:\Users\j51780\Documents\Notecards\test_files\test.txt'

def test_openFile():
    game = GameClass()
    game.setFile(r'C:\Users\j51780\Documents\Notecards\test_files\test.txt')
    game.openFile()