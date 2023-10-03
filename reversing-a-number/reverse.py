n = int(input('enter a number: '))

ns = str(n)
nsr = ''
for i in range(len(ns)-1, -1, -1):
    nsr += ns[i]

print(nsr)
