# Write a Python program to concatenate all elements in a list into a string and return it.

data = input("Enter comma separated strings: ")
listData = list(data.split(","))
print(listData)
res = ''
for entry in listData:
    res = res+entry
print("concatenated string: ",res)
