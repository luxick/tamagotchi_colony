#!/usr/bin/python
# -*- coding: utf-8 -*-

class Tamagotchi:
    status      = ''
    name        = ''
    hunger      = []
    happiness   = []
    hygiene     = []
    sleep       = []
    dead        = False
    decayspeed  = 0
    potential   = 0
    power       = 0
    recovery    = 0

    def __init__(self, name, hunger, happiness, hygiene, sleep, decayspeed, potential,recovery):
        self.name       = name
        self.hunger     = [hunger, hunger]
        self.happiness  = [happiness, happiness]
        self.hygiene    = [hygiene, hygiene]
        self.sleep      = [sleep, sleep]
        self.dead       = False
        self.status     = 'Idle'
        self.decayspeed = decayspeed
        self.potential  = potential
        self.power      = potential
        self.recovery   = recovery

    def feed_other(self, tamagotchi):
        self.status = 'Working'
        tamagotchi.status = 'Eating'

    def play_with(self, tamagotchi):
        self.status = 'Working'
        tamagotchi.status = 'Playing'

    def wash_other(self,tamagotchi):
        self.status = 'Working'
        tamagotchi.status = 'Bathing'

    def update_stat(self,stat,recovering):
        if recovering:
            if stat[0] >= stat[1]:
                self.status = 'Idle'
            if stat[0] >= stat[1] - self.recovery:
                stat[0] = stat[1]
                self.status = 'Idle'
            else:
                stat[0] += self.recovery
        else:
            if stat[0] <= 0 + self.decayspeed:
                stat[0] = 0
            else:
                stat[0] -= self.decayspeed

    def update_status(self):
        if not self.dead:
            if self.hunger[0] <= 0:
                self.status = 'Dead'
                self.dead = True
            if self.sleep[0] <= 0:
                self.status = 'Sleeping'
            if self.status is 'Working':
                if self.power <= 0:
                    self.status = 'Idle'
                    self.power = self.potential
                else:
                    self.power -= 1

    def step(self):
            self.update_status()

            if self.status is 'Eating':
                self.update_stat(self.hunger,True)
            else:
                self.update_stat(self.hunger,False)

            if self.status is 'Sleeping':
                self.update_stat(self.sleep,True)
            else:
                self.update_stat(self.sleep,False)

            if self.status is 'Bathing':
                self.update_stat(self.hygiene,True)
            else:
                self.update_stat(self.hygiene,False)

            if self.status is 'Playing':
                self.update_stat(self.happiness,True)
            else:
                self.update_stat(self.happiness,False)

    def is_dead(self):
        if self.dead:
            return True
        else:
            return False

    def percentage(self, part, whole):
        return 100 * float(part)/float(whole)

    def status_abs(self):
        return '{0:15} {1:10} Hunger:{2:10} Happiness:{3:10} Hygiene:{4:10} Sleep:{5:10}\n'.format(self.name,self.status,str(self.hunger[0])+'/'+str(self.hunger[1]),str(self.happiness[0])+'/'+str(self.happiness[1]),str(self.hygiene[0])+'/'+str(self.hygiene[1]),str(self.sleep[0])+'/'+str(self.sleep[1]))

    def status_pct(self):
        hunger_pct = '%.0f%%' %(self.percentage(self.hunger[0], self.hunger[1]))
        happiness_pct = '%.0f%%' %self.percentage(self.happiness[0], self.happiness[1])
        hygiene_pct = '%.0f%%' %self.percentage(self.hygiene[0], self.hygiene[1])
        sleep_pct = '%.0f%%' %self.percentage(self.sleep[0], self.sleep[1])

        return '{0:20} {1:10} Hunger:{2:5} Happiness:{3:5} Hygiene:{4:5} Sleep:{5:5}\n'.format(self.name,self.status,hunger_pct,happiness_pct,hygiene_pct,sleep_pct)
