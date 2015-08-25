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

stdscr = curses.initscr()
curses.noecho()
curses.curs_set(0)
stdscr.keypad(1)
stdscr.nodelay(1)

height,width = stdscr.getmaxyx()
win = curses.newpad(16383, width)

while True:
	win.move(0,0)
	win.addstr(0,0,'Simulation running. Press [q] to exit.\n')
	win.addstr(1,0,'----------------------After '+str(ticks)+' ticks------------------------------\n')
	win.addstr(3,0,king.show_kingdom())
	king.step()
	ticks += 1
	win.clrtoeol()
	win.clrtobot()
	win.refresh(0, 0, 0, 0, height-1, width-1)

	key = stdscr.getch()
	if key == ord('q'):
		break
	elif key < 0:
	    time.sleep(ticklenght)

curses.endwin()
