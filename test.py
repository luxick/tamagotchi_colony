#!/usr/bin/python

from mayorgotchi import Mayorgotchi
from kinggotchi import Kinggotchi
from util import Util
from config import *
import time
import curses

# Temporary test section
ticks = 0

def make_list(number):
	list = []
	for n in range(0,number):
	    list.append(Util().make_Tamagotchi())
	return list

king = Kinggotchi()
for n in range(0, 10):
	king.add_village(Mayorgotchi(make_list(startnr)))

screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
screen.keypad(1)
screen.nodelay(1)

while True:
    screen.move(0,0)
    screen.addstr('Simulation running. Press [q] to exit.\n')
    screen.addstr('----------------------After '+str(ticks)+' ticks------------------------------\n')
    screen.addstr(king.show_kingdom())
    king.step()
    ticks += 1

    screen.clrtobot()
    key = screen.getch()
    if key == ord('q'):
        break
    elif key < 0:
        time.sleep(ticklenght)
curses.endwin()
