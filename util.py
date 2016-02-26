#!/usr/bin/python
# -*- coding: utf-8 -*-

from tamagotchi import Tamagotchi
import random
from config import *
import os

class Util:
    def make_Tamagotchi(self):
        name = self.generateName()
        hunger = random.randrange(statrange[0],statrange[1],1)
        happiness = random.randrange(statrange[0],statrange[1],1)
        hygiene = random.randrange(statrange[0],statrange[1],1)
        sleep = random.randrange(statrange[0],statrange[1],1)
        decayspeed = random.randrange(decay[0],decay[1],1)
        potential = random.randrange(workpower[0], workpower[1],1)
        recoveryspeed = random.randrange(recovery[0], recovery[1], 1)
        lifetime = random.randrange(life[0], life[1], 1)

        return Tamagotchi(name,hunger,happiness,hygiene,sleep,decayspeed,potential,recoveryspeed,lifetime)

    def make_list_of_Tamagotchis(self, number):
        tmp = []
        for n in range(0,number):
            tmp.append(self.make_Tamagotchi())
        return tmp

    @staticmethod
    def generateName():
        # Load syllables from file
        min_syllable_count = 0
        max_syllable_count = 3

        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        syllables = []
        with open(os.path.join(__location__, 'syllables.txt')) as syllable_file:
            for line in syllable_file:
                line = line.strip()
                if len(line) == 0:
                    continue
                if line[0] == "#":
                    continue
                syllables.append(line)

        # Generate the name
        name = ""
        name += syllables[random.randint(0, len(syllables) - 1)].capitalize()
        for i in range(0, random.randint(int(min_syllable_count), int(max_syllable_count))):
            name += syllables[random.randint(0, len(syllables) - 1)]
        return name
