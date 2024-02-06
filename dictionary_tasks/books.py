books = {}

n = int(input('enter the number of books you wish to enter: '))

for i in range(n):
    name = input('enter the name of the book: ')
    price = float(input('enter the price of the book in AED: '))

    books[name] = price

print(f'the set of books with price is: {books}')