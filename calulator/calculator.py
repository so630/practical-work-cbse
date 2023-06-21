def addition(a, b):
    return a+b

def subtraction(a, b):
    return a-b

def multiplication(a, b):
    return a*b

def division(a, b):
    return a/b

a = int(input("enter a number: "))
b = int(input("enter another number: "))
type = input("enter operation to be done: ")

if type[0].lower() == 'a':
    print(addition(a, b))
elif type[0].lower() == 's':
    print(subtraction(a, b))
elif type[0].lower() == 'm':
    print(multiplication(a, b))
elif type[0].lower == 'd':
    print(division(a, b))
else:
    print("incorrect type written")