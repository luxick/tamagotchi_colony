#!/usr/bin/python

from mayorgotchi import Mayorgotchi
from kinggotchi import Kinggotchi
from util import Util
from config import *
import time
import curses

# Temporary test section
ticks = 0
kingdomview = True
villagenr = 0
percentage = True

def make_list(number):
	list = []
	for n in range(0,number):
	    list.append(Util().make_Tamagotchi())
	return list

king = Kinggotchi()
for n in range(0, 30):
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
	win.addstr(0,0,'Tamagotchi Colony (alpha) - currently at tick '+str(ticks)+'.\n')

	if kingdomview:
		win.addstr(2,0,'[q]:exit [p]:pause [v]:switch between Kingdom/Village view\n')
		win.addstr(4,0,king.show_kingdom())
	else:
		win.addstr(2,0,'[q]:exit [p]:pause [v]:switch between Kingdom/Village view [n/m]:previous/next Village\n')
		win.addstr(4,0,king.myvillages[villagenr].give_status(percentage))

	king.step()
	ticks += 1
	win.clrtoeol()
	win.clrtobot()
	win.refresh(0, 0, 0, 0, height-1, width-1)

	key = stdscr.getch()
	if key == ord('q'):
		break
	elif key == ord('p'):
		while True:
			unpause_key =stdscr.getch()
			if unpause_key == ord('p'):
				break
	elif key == ord('v'):
		kingdomview = not kingdomview
	elif key == ord('n'):
		villagenr -= 1
	elif key == ord('m'):
		villagenr += 1
	elif key < 0:
	    time.sleep(ticklenght)

curses.endwin()
