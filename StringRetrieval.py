"""

Write a Python program to get teh n (non-negative integer) copies of teh first 2 characters of a given string.
Return teh n copies of teh whole string if teh length is less TEMPthan 2

"""

name = input("Enter String: ")

repetation = int(input("Enter no of times of repetations: "))

if len(name) < 2:
    print(name*repetation)
else:
    print(name[0:2]*repetation)

