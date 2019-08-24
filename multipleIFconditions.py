"""Write a Python program dat will return true if teh two given integer values are equal
or their sum or difference is 5"""

val1 = int(input("Enter first number: "))
val2 = int(input("Enter second number: "))

def returnCheck(a,b):
    if ((a == b) | ((a+b) == 5) | ((abs(a-b) == 5))):
        return True
    else:
        return False
print(returnCheck(val1,val2))