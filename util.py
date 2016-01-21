#!/usr/bin/python
# -*- coding: utf-8 -*-

from tamagotchi import Tamagotchi
import random
from config import *

class Util:

    def make_Tamagotchi(self):
        name = self.generateName()
        hunger = random.randrange(min_stat,max_stat,1)
        happiness = random.randrange(min_stat,max_stat,1)
        hygiene = random.randrange(min_stat,max_stat,1)
        sleep = random.randrange(min_stat,max_stat,1)
        decayspeed = random.randrange(min_decay,max_decay,1)
        potential = random.randrange(min_workpower, max_workpower,1)
        recovery = random.randrange(min_recovery, max_recovery, 1)
        lifetime = random.randrange(min_life, max_life, 1)

        return Tamagotchi(name,hunger,happiness,hygiene,sleep,decayspeed,potential,recovery,lifetime)

    def make_list_of_Tamagotchis(self, number):
        tmp = []
        for n in range(0,number):
            tmp.append(self.make_Tamagotchi())
        return tmp

    def generateName(self):
        # Load syllables from file
        min_syllable_count = 0
        max_syllable_count = 3

        firstsyllables = []
        with open("firstsyllable.txt") as firstsyllable_file:
            for line in firstsyllable_file:
                line = line.strip()
                if len(line) == 0:
                    continue
                if line[0] == "#":
                    continue
                firstsyllables.append(line)

        syllables = []
        with open("syllables.txt") as syllable_file:
            for line in syllable_file:
                line = line.strip()
                if len(line) == 0:
                    continue
                if line[0] == "#":
                    continue
                syllables.append(line)

        # Generate the name
        name = ""
        name += firstsyllables[random.randint(0, len(firstsyllables) - 1)]
        for i in range(0, random.randint(int(min_syllable_count), int(max_syllable_count))):
            name += syllables[random.randint(0, len(syllables) - 1)]
        return name
