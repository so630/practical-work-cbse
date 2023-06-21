a = int(input("enter a number: "))
b = 1

for i in range(11):
    if i == 0:
        continue

    print("%i x %i = %i" %(a, b, a*b))
    b += 1

