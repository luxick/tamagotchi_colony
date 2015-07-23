#!/usr/bin/python

class Tamagotchi:
    status      = ''
    name        = ''
    hunger      = 0
    happiness   = 0
    hygiene     = 0
    sleep       = 0
    dead        = False
    decayspeed  = 0

    def __init__(self, name, hunger, happiness, hygiene, sleep, decayspeed):
        self.name       = name
        self.hunger     = [hunger, hunger]
        self.happiness  = [happiness, happiness]
        self.hygiene    = [hygiene, hygiene]
        self.sleep      = [sleep, sleep]
        self.dead       = False
        self.status     = 'Idle'
        self.decayspeed = decayspeed

    def feed_other(self, tamagotchi):
        tamagotchi.hunger += 5

    def play_with(self, tamagotchi):
        tamagotchi.happiness += 5
        self.happiness += 5

    def wash_other(self,tamagotchi):
        tamagotchi.hygiene += 5

    def sleep(self):
        self.sleep += 5

    def decay(self, amount):
        if not self.dead:
            if self.hunger[0] < amount:
                self.hunger[0] = 0
                self.dead = True
                self.status = 'Dead'
            else:
                self.hunger[0] -= amount

            if self.happiness[0] < amount:
                self.happiness[0] = 0
            else:
                self.happiness[0] -= amount

            if self.hygiene[0] < amount:
                self.hygiene[0] = 0
            else:
                self.hygiene[0] -= amount

            if self.sleep[0] <= 0:
                self.status = "Sleeping"

            if self.status is 'Sleeping':
                if self.sleep[0] <= self.sleep[1] - amount:
                    self.sleep[0] += 5
                if self.sleep[0] >= self.sleep[1]:
                    self.status = 'Idle'
            else:
                self.sleep[0] -= amount

    def step(self):
        self.decay(self.decayspeed)

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
