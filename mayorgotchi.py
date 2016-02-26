#!/usr/bin/python
# -*- coding: utf-8 -*-

from tamagotchi import Tamagotchi
import random
from config import *
from util import Util

class Mayorgotchi:
    mygotchis = []
    name = ''
    graveyard = 0

    def __init__(self, list_of_tamagotchis):
        self.mygotchis = list_of_tamagotchis
        self.name = Util.generateName()

    def remove_corpses(self):
        for n in self.mygotchis:
            if n.is_dead():
                self.graveyard += 1
                self.mygotchis.remove(n)

    def give_status(self,show_pct):
        result = 'I am Mayorgotchi ' + self.name + '.\nIn my Village live '+str(len(self.mygotchis))+' Tamagotchis.\nIn my Village '+str(self.graveyard)+' Tamagotchis died so far.\n\n'
        for n in self.mygotchis:
            if show_pct:
                result += n.status_pct()
            else:
                result += n.status_abs()
        return result

    def give_overview(self):
        result = ''
        tmp = self.get_status_list()        
        result += 'Village of Mayor {0:13} Population:{1:5} Dead:{2:5} Idle:{3:5} Eating:{4:5} Sleeping:{5:5} Bathing:{6:5} Playing:{7:5} Working:{8:5}\n'.format(self.name,str(len(self.mygotchis)),str(self.graveyard),str(len(tmp[0])), str(len(tmp[1])), str(len(tmp[2])), str(len(tmp[3])), str(len(tmp[4])), str(len(tmp[5])))

        return result
    def get_status_list(self):
        # A list containing lists of Tamagotchis and their statuses
        # 0 = Idle
        # 1 = Eating
        # 2 = Sleeping
        # 3 = Bathing
        # 4 = Playing
        # 5 = Working
        result = [[] for x in range(6)]

        for n in self.mygotchis:
            if n.status is 'Idle':
                result[0].append(n)
            if n.status is 'Eating':
                result[1].append(n)
            if n.status is 'Sleeping':
                result[2].append(n)
            if n.status is 'Bathing':
                result[3].append(n)
            if n.status is 'Playing':
                result[4].append(n)
            if n.status is 'Working':
                result[5].append(n)

        return result

    def get_free(self):
        freegotchis = []
        for n in self.mygotchis:
            if n.status is 'Idle':
                freegotchis.append(n)
        if len(freegotchis) > 0:
            return freegotchis[random.randrange(0, len(freegotchis), 1)]
        else:
            return None

    def get_hungry(self):
        for n in self.mygotchis:
            if n.status is 'Idle':
                if n.hunger[0] <= feeding_point:
                    return n

    def get_dirty(self):
        dirties = []
        for n in self.mygotchis:
            if n.status is 'Idle':
                if n.hygiene[0] <= washing_point:
                    dirties.append(n)
        if len(dirties) > 0:
            return dirties[random.randrange(0,len(dirties),1)]
        else:
            return None

    def get_unhappy(self):
        unhappies = []
        for n in self.mygotchis:
            if n.status is 'Idle':
                if n.happiness[0] <= play_point:
                    unhappies.append(n)
        if len(unhappies) > 0:
            return unhappies[random.randrange(0,len(unhappies), 1)]
        else:
            return None

    def order_feed(self):
        hungry = self.get_hungry()
        if hungry is not None:
            self.get_free().feed_other(hungry)

    def order_wash(self):
        dirty = self.get_dirty()
        if dirty is not None:
            self.get_free().wash_other(dirty)

    def order_play(self):
        unhappy = self.get_unhappy()
        if unhappy is not None:
            self.get_free().play_with(unhappy)


    def step(self):
        for n in self.mygotchis:
            n.step()
        self.remove_corpses()


        self.order_feed()
        self.order_wash()
        self.order_play()
