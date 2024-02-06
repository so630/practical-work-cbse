n = int(input("enter a number"))
pre = 0
pre1 = 1
fib = False

if n == 0 or n == 1:
    print("%i is in fibonacci series" %(n))
    fib = True
    pre1 = n+1

while pre1 <= n:
    t = pre1
    pre1 = pre+pre1
    pre = t

    if pre1 == n:
        print("%i is in fibonacci series" %(n))
        fib = True

if not fib:
    print("%i is not in fibonacci series" %(n))



