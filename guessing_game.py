name = raw_input("What is your name?")
size = raw_input("What is the biggest number you want to guess?")
import random
number = random.randint(0,10)
a = input("Guess a number")
while a != number:
	a = input("Sorry guess again")
print number
#how do I get the range work
name = raw_input("What is your name?")
size = raw_input("What is the biggest number you want to guess?")
import random
number = random.randint(0, 10)
a = input("Guess a number")
counter = 1
while a != number:
	if a > number:
		print "Sorry, " + str(name) + " your guess is too high"
		counter = counter + 1
	else:
		print "Sorry, " + str(name) + " your guess is too low"
		counter = counter + 1
	a = input("Guess again?")
	if a == number:
		print "Correct"
		print "you won"
print (counter) 
