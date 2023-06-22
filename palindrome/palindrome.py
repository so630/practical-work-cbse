a = input('enter a number or a string: ')
r = ''

for i in a:
    r = i + r

if a == r:
    print(a + ' is a palindrome')
else:
    print(a + ' is not a palindrome')