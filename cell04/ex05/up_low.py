#!/usr/bin/python3

inp = list(input())
for i in range(len(inp)):
    if inp[i].isupper():
        print(inp[i].lower(), end="")
    elif inp[i].islower():
        print(inp[i].upper(), end="")