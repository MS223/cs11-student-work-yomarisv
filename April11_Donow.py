import random

def mystery_function(x, y):
    random_number = random.randint(0,2) # What's the range of randoms?
    #0 through 2
    if random_number > 0: # What's the probability that random_number is greater than 0?
   #50 percent chance
        z = x + y
    else:
        z = x * y
    return z
mystery_function(1, 2)
