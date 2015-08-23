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
		result = 'I am Kinggotchi '+str(self.name)+'.\nThese are the '+str(len(self.myvillages))+' Villages in my Kingdom:\n'
		