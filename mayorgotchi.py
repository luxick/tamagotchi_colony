#!/usr/bin/python

from tamagotchi import Tamagotchi
import names
import random

class Mayorgotchi:
    mygotchis = []
    name = ''
    graveyard = 0

    def __init__(self, list_of_tamagotchis):
        self.mygotchis = list_of_tamagotchis
        self.name = names.get_last_name()

    def remove_corpses(self):
        for n in self.mygotchis:
            if n.is_dead():
                self.graveyard += 1
                self.mygotchis.remove(n)

    def give_status(self,show_pct):
        result = 'I am Mayorgotchi ' + self.name + '.\nIn my Village '+str(self.graveyard)+' Tamagotchis died so far.\nThese are the '+str(len(self.mygotchis))+' Tamagotchis living in my Village:\n\n'
        for n in self.mygotchis:
            if show_pct:
                result += n.status_pct()
            else:
                result += n.status_abs()
        return result

    def get_free(self):
        freegotchis = []
        for n in self.mygotchis:
            if n.status is 'Idle':
                freegotchis.append(n)
        if len(freegotchis) > 0:
            return freegotchis[random.randrange(0,len(freegotchis),1)]
        else:
            return None

    def get_hungry(self):
        for n in self.mygotchis:
            if n.status is 'Idle':
                if n.hunger[0] <= 20:
                    return n

    def get_dirty(self):
        dirties = []
        for n in self.mygotchis:
            if n.hygiene[0] <= 20:
                dirties.append(n)
        if len(dirties) > 0:
            return dirties[random.randrange(0,len(dirties),1)]
        else:
            return None

    def get_unhappy(self):
        unhappies = []
        result = []
        for n in self.mygotchis:
            if n.happiness[0] <= 20:
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
