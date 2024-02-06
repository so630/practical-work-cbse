employees = {}

while True:
    c = input('enter q if you wish to quit, else enter `c`: ')
    if c == 'q':
        break
    n = int(input('enter the employee number: '))
    name = input('enter the name of the employee: ')
    basic_pay = int(input('enter the basic pay of the employee: '))
    position = input('enter the position of the employee: ')

    employees[n] = {'name': name, 'basic_pay': basic_pay, 'position': position}

c = input('enter whether you wish to print all employees in ascending order (p) or to access specific employee information (a): ')
if c == 'p':
    print(sorted(employees.items()))
elif c == 'a':
    n = int(input('enter the employee number: '))
    print(employees[n])
