"""
Darts Simulation
CS550 Kevin Xie

10: 3.6
100: 3.16
1,000: 3.168
10,000: 3.1408
100,000: 3.13892
1,000,000: 3.142408
10,000,000: 3.1413504

The final value is moving closer to pi. According to a video I watched for more information,
this simulation is meant to estimate the value of pi with a higher accuracy as iterations
increase.

Sources:
generating a random float: https://stackoverflow.com/questions/6088077/how-to-get-a-random-number-between-a-float-range

On My Honor, I have neither given nor recceived unauthorized aid.
Kevin Xie
"""
import random, sys

# number of darts (n) thrown and count of darts that land in inscribed circle
n = int(sys.argv[1])
count = 0

# for number (n), chooses a random coordinate between -1 and 1 for x and y. 
for i in range(n):
	position = [random.uniform(-1.0,1.0) for j in range(2)] 
	# uses pythagoras distance formula to check if dart is at or within circle radius of 1
	if ((position[0]**2+position[1]**2)**0.5)<=1.0:
		count+=1

# count of darts*4/100
print((count*4)/n)