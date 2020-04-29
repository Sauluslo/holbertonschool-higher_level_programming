#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_of = "Last digit of"
if number >= 0:
    count = number % 10
else:
    count = number % -10
if count == 0:
    print("{}{} is {} and is 0".format(last_of, number, count))
elif count < 6 and count != 0:
    print("{}{} is {} and is less than 6 and not 0"
        .format(last_of, number, count))
else:
    print("{}{} is {} and is greater than 5".format(last_of, number, count))
