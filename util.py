#!/usr/bin/python

from tamagotchi import Tamagotchi
import random
import names
from config import *

class Util:

    def make_Tamagotchi(self):
        name = names.get_last_name()
        hunger = random.randrange(min_stat,max_stat,1)
        happiness = random.randrange(min_stat,max_stat,1)
        hygiene = random.randrange(min_stat,max_stat,1)
        sleep = random.randrange(min_stat,max_stat,1)
        decayspeed = random.randrange(min_decay,max_decay,1)
        potential = random.randrange(min_workpower, max_workpower,1)
        recovery = random.randrange(min_recovery, max_recovery, 1)

        return Tamagotchi(name,hunger,happiness,hygiene,sleep,decayspeed,potential,recovery)
