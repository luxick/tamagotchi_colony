#!/usr/bin/python

# The amount of points a Tamagotchi loses per tick
decayaspeed = 1
# Controls if Tamagotchi stats are shown in absolute vlaues or precentage (Possible values: True/False)
show_pct = False
# When new Tamagotchis are created their stats will be be created randomly between these.
min_stat = 100
max_stat = 200
# Tamagotchis decay at a set rate per tick. The value of decay is randomly chosen between these two.
min_decay = 1
max_decay = 3
# These two define how long it takes a Tamagotchi to perform work (preparing food/washing someone/playing with someone)
# The value is choosen randomly between these two. Obviously a lower number is better.
min_workpower = 1
max_workpower = 3
# This defines the bounds of how much a Tamagotchi can recover when eating/sleeping/playing etc.
min_recovery = 10
max_recovery = 20
