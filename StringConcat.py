"""
 Write a Python program to get a new string from a given string where "Is" has been added to the front.
  If the given string already begins with "Is" then return the string unchanged.
"""

word = input("Enter String: ")

def  func(str):
    if str.startswith("Is"):
        print("Is already exist")
        return str
    else:
        str = "Is"+str
        return str

print(func(word))