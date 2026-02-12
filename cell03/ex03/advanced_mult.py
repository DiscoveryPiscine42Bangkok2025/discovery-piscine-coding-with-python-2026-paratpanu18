#!/usr/bin/python3

for i in range(0, 11):
    print(f"Table de {i}: ", end="")
    for j in range(0, 11):
        print(f'{i * j}', end=" ")
    print()