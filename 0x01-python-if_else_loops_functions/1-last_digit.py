#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = repr(number) #get the string rep. of the number
# Acces the last string of the digit string
last_digit_str = num_str[-1]
# Covert the last digit string to an integer
last_digit = int(last_digit_str)
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
else:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
