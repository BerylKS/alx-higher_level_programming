#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    ld = number % 10
else:
    absnumber = abs(number)
    ldabs = absnumber % 10
    ld = ldabs * -1
if ld > 5:
    print(f"Last digit of {number} is {ld} and is greater than 5")
elif ld == 0:
    print(f"Last digit of {number} is {ld} and is 0")
else:
    print(f"Last digit of {number} is {ld} and is less than 6 and not 0")
