#!/usr/bin/python

from tamagotchi import Tamagotchi
import names

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

    def give_status(self,show_pct):
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
