days = {'january': 31, 'february': 28, 'march': 31, 'april': 30, 'may': 31, 'june': 30, 'july': 31, 'august': 31, 'september': 30, 'october': 31, 'november': 30, 'december': 31}

y = int(input('enter the year in AD or CE: '))
ly = ((y % 4 == 0))

if (y % 100 == 0):
    if y % 400 == 0:
        ly = True
    else:
        ly = False
    

if ly:
    days['february'] = 29

print(days)
