#!/usr/bin/python

from tamagotchi import Tamagotchi
from util import Util
import names

decayaspeed = 1
ticks = 50
show_pct = True

class Mayorgotchi:
    mygotchis = []
    name = ''

    def __init__(self, list_of_tamagotchis):
        self.mygotchis = list_of_tamagotchis
        self.name = names.get_last_name()

    def remove_corpses(self):
        for n in self.mygotchis:
            if n.is_dead():
                self.mygotchis.remove(n)

    def give_status(self):
        result = 'I am Mayorgotchi ' + self.name + '. These are the Tamagotchis in my Village:\n\n'
        for n in self.mygotchis:
            if show_pct:
                result += n.status_pct()
            else:
                result += n.status_abs()
        return result

    def step(self):
        for n in self.mygotchis:
            n.step()
        self.remove_corpses()


# Temoprarty Test Section
list = []
for n in range(0,10):
    list.append(Util().make_Tamagotchi())

mayor = Mayorgotchi(list)

print mayor.give_status()

for n in range (0, ticks):
    mayor.step()

print '----------------------After '+str(ticks)+' ticks------------------------------\n'

print mayor.give_status()

for n in range (0, ticks):
    mayor.step()

print '----------------------After another '+str(ticks)+' ticks------------------------------\n'

print mayor.give_status()
