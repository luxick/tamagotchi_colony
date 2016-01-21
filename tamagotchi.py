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
    lifetime    = 0

    def __init__(self, name, hunger, happiness, hygiene, sleep, decayspeed, potential, recovery, lifetime):
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
        self.lifetime   = lifetime 

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
            if self.lifetime <= 0:
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
        self.lifetime -= 1

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
        rtn = '{0:15}'.format(self.name)
        rtn += '{0:10}'.format(self.status)
        rtn += 'Hunger: {0:10}'.format(str(self.hunger[0]) + '/' + str(self.hunger[1]))
        rtn += 'Happiness: {0:10}'.format(str(self.happiness[0]) + '/' + str(self.happiness[1]))
        rtn += 'Hygiene: {0:10}'.format(str(self.hygiene[0]) + '/' + str(self.hygiene[1]))
        rtn += 'Sleep: {0:10}'.format(str(self.sleep[0]) + '/' + str(self.sleep[1]))
        rtn += '\n'
        return rtn

    def status_pct(self):
        hunger_pct = '%.0f%%' %(self.percentage(self.hunger[0], self.hunger[1]))
        happiness_pct = '%.0f%%' %self.percentage(self.happiness[0], self.happiness[1])
        hygiene_pct = '%.0f%%' %self.percentage(self.hygiene[0], self.hygiene[1])
        sleep_pct = '%.0f%%' %self.percentage(self.sleep[0], self.sleep[1])

        rtn = '{0:20}'.format(self.name)
        rtn += '{0:10}'.format(self.status)
        rtn += 'Hunger: {0:5}'.format(hunger_pct)
        rtn += 'Happiness: {0:5}'.format(happiness_pct)
        rtn += 'Hygiene: {0:5}'.format(hygiene_pct)
        rtn += 'Sleep: {0:5}'.format(sleep_pct)
        rtn += '\n'
        return rtn
