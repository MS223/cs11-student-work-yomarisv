# what does this function return ?
def print_only(x):
   y = x * 2
   print y
#It is printing the number 14 because the number 7 is being multipied by 2 before the print.
# how is this one different ?
def return_only(x):
   y = x * 2
   return y
#this one is different because it is returning a value.
# let's try to use our 2 functions
print "running print_only ..."
print_only(7)

print "running return_only ..."
return_only(7)

print "printing print_only ..."
print print_only(7)

print "printing return_only ..."
return_only(7)

print "using print_only ..."
print_only(7) + 6

print "using return_only ..."
return_only(7) + 6
#Return returned a none but print was simply printing the number.
