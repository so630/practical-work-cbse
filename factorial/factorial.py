n = int(input("enter a number: "))

f = 1
for i in range(n+1):
    if i != 0:
        f *= i

print("%i is %i!" %(f, n))