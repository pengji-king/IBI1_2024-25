# What does this piece of code do?
# Answer:it makes a loop, while in this loop there will be two random int be stored in two variables first_n and second_n. Then compare thses two nubmber(between 1 and 6) to see whether there are equal or not. if not the loop will continue again, but if the they are equal it will break from the whle loop. and the variable progress is used to count how many loops it uses to get two equal random numbers. 

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
while progress>=0:
	progress+=1
	first_n = randint(1,6)
	second_n = randint(1,6)
	if first_n == second_n:
		print(progress)
		break

