#!/usr/bin/python
# -*- coding: utf-8 -*-

# Define if simulation should be started paused or running
start_paused = True
# The lenght of one game cycle in milliseconds
ticklenght = 0.001
# Controls if Tamagotchi stats are shown in absolute vlaues or precentage (Possible values: True/False)
show_pct = True
# Number of Tamagotchis to be created at the start of the simulation
startnr = 60
startNrVillages = 50
# If the value of a Tamagotchis stats drops below this he will be fed/washed/etc
# Synatx [Hunger, Hygiene, Happiness]
interventionPoints = [50, 50, 50]
# If the hunger stat falls below this level Tamagotchis can be fed
feeding_point = 50
# If the hygiene stat falls below this level Tamagotchis can be washed
washing_point = 50
# If the happiness stat falls below this level Tamagotchis can be played with
play_point = 50
# When new Tamagotchis are created their stats will be be created randomly between these.
statrange = [100, 200]
# Tamagotchis decay at a set rate per tick. The value of decay is randomly chosen between these two.
decay = [1, 3]
# These two define how long it takes a Tamagotchi to perform work (preparing food/washing someone/playing with someone)
# The value is choosen randomly between these two. Obviously a lower number is better.
workpower = [3, 6]
# This defines the bounds of how much a Tamagotchi can recover when eating/sleeping/playing etc.
recovery = [10, 20]
# Defines the range in witch the lifetime of Tamagotichs will be created in ticks
life = [2000, 3000]


