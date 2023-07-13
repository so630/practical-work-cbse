def print_menu():
    print('''
    Menu:
    1. Append an element
    2. Insert an element
    3. Append a list to the given list
    4. Modify an existing element
    5. Delete an existing element
    6. Delete an exisiting element with a given value
    7. Sort the list in ascending order
    8. Sort the list in descending order
    9. Display the list
    0. quit
    
    ''')

l = []
while True:
    print_menu()
    choice = int(input('enter your choice: '))

    if choice == 1:
        element = input('enter the element to be appended: ')
        l.append(element)
    elif choice == 2:
        element = input('enter the element to be inserted: ')
        index = int(input('enter the position at which the element is to be inserted: '))-1
        l.insert(index, element)
    elif choice == 3:
        li = input('enter the elements to be appended, separated by commas [example: 1,2,3,4]: ')
        li = li.split(',')
        l.extend(li)
    elif choice == 4:
        element = input('enter the element to modify to: ')
        element2 = input('enter the element to be modified: ')
        index = l.index(element2)
        l[index] = element
    elif choice == 5:
        index = int(input('enter the index of element to be deleted: '))
        l.pop(index)
    elif choice == 6:
        element = input('enter the element to be deleted: ')
        l.remove(element)
    elif choice == 7:
        l.sort()
    elif choice == 8:
        l.sort(reverse=True)
    elif choice == 9:
        print(f'list is: {l}')
    else:
        print('quitting')
        break