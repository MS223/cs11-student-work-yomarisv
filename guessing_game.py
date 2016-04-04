name = raw_input("What is your name?")
size = raw_input("What is the biggest number you want to guess?")
import random
number = random.randint(0,10)
a = input("Guess a number")
while a != number:
	a = input("Sorry guess again")
print number
#how do I get the range work
