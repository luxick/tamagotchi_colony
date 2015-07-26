#!/usr/bin/python

from mayorgotchi import Mayorgotchi
from util import Util
import time
import curses


# Temporary test section

# Variable Definition
decayaspeed = 1
ticks = 200000
show_pct = True

list = []

for n in range(0,50):
    list.append(Util().make_Tamagotchi())

mayor = Mayorgotchi(list)


screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
screen.keypad(1)
screen.nodelay(1)

for n in range (0, ticks):
    screen.move(0,0)
    mayor.step()
    screen.addstr('----------------------After '+str(n)+' ticks------------------------------\n')
    screen.addstr(mayor.give_status(show_pct))

    screen.clrtobot()
    key = screen.getch()
    if key == ord('q'):
        break
    elif key < 0:
        time.sleep(0.5)
curses.endwin()
