a = input('enter a number or string: ')
r = ''

for i in a:
    r = i + r
if r == a:
    print(f'{a} is a palindrome')
else: 
    print(f'{a} is not a palindrome')