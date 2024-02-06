students = dict()

while True:
    rn = int(input('enter roll no. of student: '))
    name = input('enter name of student: ')
    students[rn] = name

    q = input('do you wish to quit? enter q if so: ')
    if q[0].lower() == 'q':
        print('terminating input process...')
        break

print(f'list of students names and their roll numbers are: {students}')