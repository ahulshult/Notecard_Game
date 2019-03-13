#!/usr/bin/env python
import os
from game import GameClass 
   
if __name__ == '__main__':
    game  = GameClass()
    game.setUp(r'C:\Users\j51780\Documents\Notecards\words.txt')
    game.play()
    