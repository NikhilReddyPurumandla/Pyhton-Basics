# Write a Python program to create a histogram from a given list of integers

a = input("Enter comma seperated numbers: ")
data = list(a.split(","))
print(data)
display =''
for number in data:
    rep = int(number)
    while(rep>0):
        display = display + '*'
        rep = rep - 1
    print(display)