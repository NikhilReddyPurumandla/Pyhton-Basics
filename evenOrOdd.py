#even or odd

num = int(input("Enter a number: "))

def func(a):
    if(a%2 == 0):
        res = str(a)+" is a even number"
        return res
    else:
        res = str(a)+" is odd number"
        return res

print(func(num))