#!/usr/bin/python3

num = input("Give me a number: ")
try:
    if float(num) == int(float(num)):
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("This number is not a valid number.")