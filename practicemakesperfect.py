x = input("Input a number to see if its even")
def is_even(input):
    if x % 2 == 0:
        return True
    else:
        return False
print is_even(x)

def is_int(x):
    if x == int(x):
        return True
    else:
        return False
print is_int(x)


x = 1234
print x
y = str(x)
print y
print y[2]

def digit_sum(n):
    y = str(n)
    answer= 0
    for i in y:
        answer = answer + int(i)
    return answer
print digit_sum(1234)
