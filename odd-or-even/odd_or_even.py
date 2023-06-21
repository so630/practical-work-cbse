def is_even(a):
    return a%2 == 0

a = int(input("enter a number: "))

if is_even(a):
    print('the number is even')
else:
    print('the number is odd')