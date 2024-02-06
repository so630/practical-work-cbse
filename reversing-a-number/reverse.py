n = int(input('enter a number: '))

ns = str(n)
nsr = ''

for i in range(len(ns)):
    nsr = ns[i] + nsr

print(nsr)