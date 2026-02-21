x = input("Enter a sentence")
y=x
print("There are",len(x.split())," words in the sentence")
digits, upper, lower = 0,0,0
for i in x:
    if i.isdigit():
        digits += 1
    elif i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
print("There are {0} digits, {1} upper case characters and {2} lower case characters in the sentence".format(digits, upper,lower))