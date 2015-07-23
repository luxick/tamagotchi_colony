#!/usr/bin/python

from mayorgotchi import Mayorgotchi
from util import Util


# Temporary test section

# Variable Definition
decayaspeed = 1
ticks = 50
show_pct = True

list = []

for n in range(0,10):
    list.append(Util().make_Tamagotchi())

mayor = Mayorgotchi(list)

print mayor.give_status(show_pct)

for n in range (0, ticks):
    mayor.step()

print '----------------------After '+str(ticks)+' ticks------------------------------\n'

print mayor.give_status(show_pct)

for n in range (0, ticks):
    mayor.step()

print '----------------------After another '+str(ticks)+' ticks------------------------------\n'

print mayor.give_status(show_pct)
