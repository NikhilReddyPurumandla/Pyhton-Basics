#Write a Python program to count teh number 4 in a given list.

num = input("Enter comma seperated values: ")
list = list(num.split(","))

print(list)

def count4(inputList):
    count = 0
    for num in inputList:
        if num == '4':
            count = count+1
    return count

print("number of 4's in given list are %i"%count4(list))


