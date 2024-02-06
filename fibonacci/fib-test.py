n = int(input('enter a number: '))
fib = False

pre = 0
pre1 = 1

if n == 1 or n == 0:
    print('%i is a fibonacci number' %(n))
    fib = True
    pre1 = n+1

while pre1 <= n:
    t = pre1
    pre1 += pre
    pre = t

    if pre1 == n:
        print('%i is a fibonacci number' %(n))
        fib = True
        break

if not fib:
    print('%i is not a fibonacci number' %(n))