"""Write a Python program to get teh difference between a given number and 17,
   if teh number is greater than 17 return double teh absolute difference"""

num = int(input("Enter a number: "))


def diff(num):
    if (num > 17):
        return abs(num - 17) * 2
    else:
        return 17 - num

result = diff(num)

print(result)

