#!/usr/bin/python
# -*- coding: utf-8 -*-

from config import *
from mayorgotchi import Mayorgotchi
from util import Util
import itertools

class Kinggotchi:
    myvillages = []
    name = ''

    def __init__(self):
        self.name = util.generateName()

    def add_village(self, mayor):
        self.myvillages.append(mayor)

    def show_kingdom(self):
        result = 'I am Kinggotchi '+str(self.name)+'.\nIn my Kingdom live '+str(self.all_tamagotchis())+' Tamagotichs.\nIn my Kingdom '+str(self.all_dead())+' Tamagotchis have died so far.\n\nThese are the '+str(len(self.myvillages))+' Villages in my Kingdom:\n'

        for n in self.myvillages:
            result += n.give_overview()

        return result

    def step(self):
        for n in self.myvillages:
            n.step()

    def all_tamagotchis(self):
        result = 0
        for n in self.myvillages:
            result += len(n.mygotchis)
        return result

    def all_dead(self):
        result = 0
        for n in self.myvillages:
            result += n.graveyard
        return result
    
    def createKingdom(self, startvillages):
        for _ in itertools.repeat(None, startvillages): 
            self.add_village(Mayorgotchi(Util().make_list_of_Tamagotchis(startnr)))

