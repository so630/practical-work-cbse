def largest(a, b, c):
    l = [a, b, c]
    low = a
    for i in l:
        if i < low:
            low = i

a = int(input("enter a number: "))
b = int(input("enter another number: "))
c = int(input("enter another number: "))

print(largest(a, b, c))