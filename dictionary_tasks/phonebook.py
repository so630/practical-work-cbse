contacts = {}

while True:
    name = input('enter the name of the contact: ')
    ph_no = int(input('enter the number of the contact: '))
    contacts[name] = ph_no

    c = input('enter if you wish to quit (q): ')
    if c == 'q':
        break

name = input('enter the name of the person whose phone number you want: ')
print(contacts[name])
