d = {}

while True:
    print('''
          Menu
          1. add an element to dictionary
          2. remove an element from dictionary
          3. display length of dictionary
          4. clear the elements of the dictionary
          5. get a value from key
          6. get list of keys
          7. get list of values
          8. change the value of a key
          9. print largest value
          10. print the lowest value
          11. print the dictionary
          12. quit
    ''')
    c = input('enter your choice: ')

    if c == '1':
        key = input('enter the key: ')
        value = input('enter the value: ')
        d[key] = value
        print(d)
    elif c == '2':
        key = input('enter the key to be removed')
        print(d[key])
        del d[key]
    elif c == '3':
        print(f'length of dictionary is: {len(d)}')
    elif c == '4':
        d.clear()
    elif c == '5':
        key = input('enter the key: ')
        print(f'value of [{key}] is [{d[key]}]')
    elif c == '6':
        print(f'list of keys is: {d.keys()}')
    elif c == '7':
        print(f'list of values: {d.values()}')
    elif c == '8':
        key = input('enter the key to update: ')
        value = input('enter the value to update to: ')
        d[key] = value
    elif c == '9':
        print(f'largest value is: {max(d, key=d.get)}')
    elif c == '10':
        print(f'minimum value is: {min(d, key=d.get)}')
    elif c == '11':
        print(d)
    else:
        break
