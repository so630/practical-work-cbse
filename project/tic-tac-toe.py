from random import randint

table = [['0', '1', '2'],
         ['3', '4', '5'],
         ['6', '7', '8']]

def print_table():
    loc = 0
    for i in table:
        counter = 0
        for j in i:
            print(' ', end='')
                
            print(j, end=(' |' if counter != 2 else '\n'))
            counter += 1
        print('-'*11 if loc != 2 else '')
        loc += 1

def check_win():
    def check_diagonal():
        if table[0][0] == table[1][1] == table[2][2]:
            return True
        elif table[0][-1] == table[1][-2] == table[2][0]:
            return True
        
        return False
    
    def check_horizontal():
        for i in table:
            equal = ''
            counter = 0
            for j in i:
                if counter == 2 and equal == j:
                    return True

                if j == equal:
                    equal = j
                elif counter == 0:
                    equal = j
                else:
                    break

                counter += 1

        return False
    
    def check_vertical():
        for i in range(3):
            equal = ''
            for j in range(3):
                if j == 2 and equal == table[j][i]:
                    return True
                    

                if j == 0:
                    equal = table[j][i]
                elif equal == table[j][i]:
                    equal = table[j][i]
                else:
                    break

        return False
    
    return check_diagonal() or check_horizontal() or check_vertical()

def check_draw():
    for i in table:
        for j in i:
            if (j != 'O' and j != 'X'):
                return False
    
    return True

# print_table()
# print(check_win())

def take_input(loc, turn):
    if loc <= 2 and loc >= 0:
        if table[0][loc] == 'X' or table[0][loc] == 'O':
            print('You cannot fill in this space since it is already occupied!')
            return False
        table[0][loc] = turn
    elif loc <= 5 and loc >= 3:
        if table[1][loc-3] == 'X' or table[1][loc-3] == 'O':
            print('You cannot fill in this space since it is already occupied!')
            return False
        table[1][loc-3] = turn
    elif loc <= 8 and loc >= 6:
        if table[2][loc-6] == 'X' or table[2][loc-6] == 'O':
            print('You cannot fill in this space since it is already occupied!')
            return False
        table[2][loc-6] = turn
        
    return True

def reset_table():
    global table
    table = [['0', '1', '2'],
             ['3', '4', '5'],
             ['6', '7', '8']]
    
    print('\n'*100)
    


game_loop = True
player = ''
first = True

while game_loop:
    player = ('X' if randint(1,2) == 1 else 'O') if first else player
    first = False if first else first

    print(f'{player} is playing now')
    print_table()
    loc = int(input('enter the location at which you wish to place your marker (to quit press \'-1\'): '))
    if loc == -1:
        print('quitting...')
        game_loop = False
    if not take_input(loc, player):
        print('enter again...')
        continue

    
    if check_win():
        print(f'player {player} wins!')
        print_table()
        q = input('do you wish to play again? (y/n): ')
        if q[0].lower() == 'y':
            reset_table()
            first = True
        elif q[0].lower() == 'n':
            game_loop = False
    elif check_draw():
        print(f'it is a draw!')
        print_table()
        q = input('do you wish to play again? (y/n): ')
        if q[0].lower() == 'y':
            reset_table()
            first = True
        elif q[0].lower() == 'n':
            game_loop = False


    player = 'O' if player == 'X' else 'X'



            






