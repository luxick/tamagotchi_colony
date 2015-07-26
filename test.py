#!/usr/bin/python

from mayorgotchi import Mayorgotchi
from util import Util
from config import *
import time
import curses


# Temporary test section

list = []
ticks = 0

for n in range(0,50):
    list.append(Util().make_Tamagotchi())

mayor = Mayorgotchi(list)


screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
screen.keypad(1)
screen.nodelay(1)

while True:
    screen.move(0,0)
    mayor.step()
    screen.addstr('Simulation running. Press [q] to exit.\n')
    screen.addstr('----------------------After '+str(ticks)+' ticks------------------------------\n')
    screen.addstr(mayor.give_status(show_pct))
    ticks += 1

    screen.clrtobot()
    key = screen.getch()
    if key == ord('q'):
        break
    elif key < 0:
        time.sleep(ticklenght)
curses.endwin()
