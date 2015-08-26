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
king = Kinggotchi()
ui = cursesUI(True)

for n in range(0, 30):
    king.add_village(Mayorgotchi(Util().make_list_of_Tamagotchis(startnr)))

while True:
    ui.build_screen(king, ticks)

    if not ui.paused:
        king.step()
        ticks += 1
    if not ui.running:
        break
        