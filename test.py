#!/usr/bin/python

from mayorgotchi import Mayorgotchi
from util import Util
import time


# Temporary test section

# Variable Definition
decayaspeed = 1
ticks = 200000
show_pct = True

list = []

for n in range(0,50):
    list.append(Util().make_Tamagotchi())

mayor = Mayorgotchi(list)
for n in range (0, ticks):
    mayor.step()
    print(chr(27) + "[2J")
    print '----------------------After '+str(n)+' ticks------------------------------\n'

    print mayor.give_status(show_pct)

    time.sleep(0.5)
