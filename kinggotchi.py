#!/usr/bin/python

from config import *
from mayorgotchi import Mayorgotchi
import names
import random

class Kinggotchi:
	myvillages = []
	name = ''

	def __init__(self):
		self.name = names.get_last_name()

	def add_village(self, mayor):
		self.myvillages.append(mayor)

	def show_kingdom(self):
		result = 'I am Kinggotchi '+str(self.name)+'.\nIn my Kingdom live '+str(self.all_tamagotchis())+' Tamagotichs.\nIn my Kingdom '+str(self.all_dead())+' Tamagotchis have died so far.\n\nThese are the '+str(len(self.myvillages))+' Villages in my Kingdom:\n'

		for n in self.myvillages:
			result += '-------------------------------------------------------------------------------\n'
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

		