from random import randint
import sys

#Treating parameters
x = int(sys.argv[1])
y = 0
name = sys.argv[2]

#executing looping while in range
while (y < x):
    #using zfill() function to fill the 8 digits
    number = str(randint(0, 90000000)).zfill(8)
    print("register('" + str(name) + str(y)+ "', '" + str(number) + "').")
    y += 1
