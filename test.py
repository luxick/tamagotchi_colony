#!/usr/bin/python
# coding=UTF-8

from mayorgotchi import Mayorgotchi
from kinggotchi import Kinggotchi
from util import Util
from config import *
from cli import *
import time
import curses

# Temporary test section
ticks = 0

def make_list(number):
    tmp = []
    for n in range(0,number):
        tmp.append(Util().make_Tamagotchi())
    return tmp

king = Kinggotchi()
for n in range(0, 30):
    king.add_village(Mayorgotchi(make_list(startnr)))

ui = cursesUI(True)

while True:
    ui.build_screen(king,ticks)

    if not ui.paused:
        king.step()
        ticks += 1
    if not ui.running:
        break