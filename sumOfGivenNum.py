"""
 Write a Python program to calculate the sum of three given numbers,
 if the values are equal tan return thrice of their sum.
"""

num1 = int(input(" Enter first number"))
num2 = int(input(" Enter second number"))
num3 = int(input(" Enter third number"))

if num1 == num2 == num3 :
    print("all 3 numbers are equal,sum is %i"%(num1*3))
else:
    print("sum is %i"%(num1+num2+num3))