#!/usr/bin/python
# -*- coding: utf-8 -*-

class Egg:
    alive = True
    age = 0
    care = 100

    def __init__(self):
        self.alive = True
        self.age = 0
        self.care = 100

    def step(self):
        if self.alive:
            if self.care >= 0:
                age += 1
            else:
                self.alive = False


