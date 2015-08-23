#!/usr/bin/python

# The lenght of one game cycle in milliseconds
ticklenght = 0.005
# Number of Tamagotchis to be created at the start of the simulation
startnr = 100
# The amount of points a Tamagotchi loses per tick
decayaspeed = 1
# If the hunger stat falls below this level Tamagotchis can be fed
feeding_point = 50
# If the hygiene stat falls below this level Tamagotchis can be washed
washing_point = 50
# If the happiness stat falls below this level Tamagotchis can be played with
play_point = 50
# Controls if Tamagotchi stats are shown in absolute vlaues or precentage (Possible values: True/False)
show_pct = True
# When new Tamagotchis are created their stats will be be created randomly between these.
min_stat = 100
max_stat = 200
# Tamagotchis decay at a set rate per tick. The value of decay is randomly chosen between these two.
min_decay = 1
max_decay = 3
# These two define how long it takes a Tamagotchi to perform work (preparing food/washing someone/playing with someone)
# The value is choosen randomly between these two. Obviously a lower number is better.
min_workpower = 3
max_workpower = 6
# This defines the bounds of how much a Tamagotchi can recover when eating/sleeping/playing etc.
min_recovery = 10
max_recovery = 20
