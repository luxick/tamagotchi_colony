#!/usr/bin/python

from tamagotchi import Tamagotchi
import random
import names

class Util:

    def make_Tamagotchi(self):
        name = names.get_last_name()
        hunger = random.randrange(80,120,1)
        happiness = random.randrange(80,120,1)
        hygiene = random.randrange(80,120,1)
        sleep = random.randrange(80,120,1)
        decayspeed = random.randrange(1,3,1)
        potential = random.randrange(1,5,1)

        return Tamagotchi(name,hunger,happiness,hygiene,sleep,decayspeed,potential)
