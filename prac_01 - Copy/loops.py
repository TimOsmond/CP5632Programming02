"""
CP1404/CP5632 - Practical 1
Program to show the use of range and print stars in different orientations.
"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()
for i in range(0, 101, 10):
    print(i, end=' ')
print()
for i in range(20, 0, -1):
    print(i, end=' ')
print()
stars = int(input("Number of stars: "))
for i in range(stars):
    print("*", end='')
print()
for i in range(1, stars + 1):
    print(i * "*")
