#Write a Python program to test whether a passed letter is a vowel or not

letter = input("Enter a alphabet: ")

def vowelCheck(alphabet):
    if letter in ['a','e','i','o',''u'']:
        result = letter + " is vowel"
        return  result
    elif letter in ['A','E','I','O','U']:
        result = letter + " is vowel"
        return result
    else:
        result = letter + " is not vowel"
        return result

print(vowelCheck(letter))