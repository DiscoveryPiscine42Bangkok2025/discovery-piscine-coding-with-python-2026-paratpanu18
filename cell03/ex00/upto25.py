#!/usr/bin/python3

num = int(input("Enter a number less than 25\n"))

if num > 25:
    print("Error")
    exit()

while num <= 25:
    print(f'Inside the loop, my variable is {num}')
    num += 1