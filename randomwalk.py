"""
Monte Carlo Walk Simulation
CS550 Kevin Xie

1. The longest walk that can be taken with at least a 50% chance of walking home is
22 units in distance. I used a recursive loop to test each walk distance up to a user-
inputted maximum at a user-inputted maximum iteration. As such, the simulation could
work through each walk distance and I can discern which walk distance is the farthest
while maintaining a walk frequency of more than 50%. It may have also been easier if
I recorded each resulting percentage and returned the walk distance closest to 50% 
while still being above it. More comments in the code.

2. A Monte Carlo simulation is a computerized mathematical technique used to account for
risk in quantitative analysis and decision making. It has been used to model an atomic bomb,
a casino's win outcomes, economic outcomes, and many more physical and conceptual systems. 
Today they are used for particle physics, engineering, and finance. Since the world is not 
a "linear" and "predictable" system, Monte Carlo simulations uses random inputs (within 
realistic limits) to model a system and predict more realistic and probable outcome
probablities.

On My Honor, I have neither given nor received unauthorized aid.
Kevin Xie 
"""

import random, sys

# user-inputted maximum walk distance (n) and number of iteratinos per walk distance (t)
n = int(sys.argv[1])
t = int(sys.argv[2])

for x in range(n+1):
	# keeps track of frequency of possible "return lengths," resets after each walk distance
	walklengths = [0 for i in range(x+1)]
	for j in range(t):
		position = [0,0]
		# performs random walk for x (current n iteration) distance (chooses random direction (which coordinate position to modify) and random value to move by (-1 or 1))
		for i in range(x):
			position[random.randrange(0,2)]+=random.randrange(-1,2,2)
		distance = abs(position[0])+abs(position[1])
		# adds final distance to frequency data
		walklengths[distance] += 1
	bus = 0
	# sums number of busrides (final distances over 4)
	for i in range(x-4):
		bus += walklengths[i+5]
	print(str(x)+" walk distance: " + str(100-(bus*100)/t)+"% walks and "+str((bus*100)/t)+"% bus rides")