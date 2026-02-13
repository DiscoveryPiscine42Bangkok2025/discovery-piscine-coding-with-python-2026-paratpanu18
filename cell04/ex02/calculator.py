#!/usr/bin/python3

num1 = int(input("Give me the first number: "))
num2 = int(input("Give me the second number: "))

print("Thank you!")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
if num2 == 0:
    print("Division by 0 is not allowed.")
else:
    print(f"{num1} / {num2} = {num1 // num2}")
print(f"{num1} * {num2} = {num1 * num2}")