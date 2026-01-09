import os

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Mac and Linux (os.name is 'posix')
    else:
        _ = os.system('clear')

def display(matrix, message=''):
    if message:
        print(message)
    print('-------------')
    for i in range(len(matrix)*2):
        if i%2==0:
            i_temp = i//2
            print('| ', end='')
            for j in range(len(matrix[i_temp])):
                print(matrix[i_temp][j], end=' | ')
        else:
            print('\n-------------')
    print('\n')
        
def pos_input():
    pos = ''
    acceptable_value = range(1,10)
    while pos.isdigit() == False or int(pos) not in acceptable_value:
        pos = input(f'Type box number (number from {acceptable_value[0]} to {acceptable_value[-1]}): ')
        if pos.isdigit() == False:
            clear_screen()
            print('Sorry, please enter a positive number.\n')
        elif int(pos) not in acceptable_value:
            clear_screen()
            print(f'Sorry, please choose a number from {acceptable_value[0]} to {acceptable_value[-1]}\n')
    return int(pos)

def save_to_board(matrix, x_pos, y_pos, sym):
    while matrix[y_pos][x_pos] != ' ':
        clear_screen()
        display(matrix, 'This box is already taken. Please choose another box.\n')
        display(board_num, 'Here is the board number:')
        pos = pos_input()
        x_pos = (pos - 1) % 3
        y_pos = (pos - 1) // 3
    matrix[y_pos][x_pos] = sym
    return matrix

def player_sym():
    sym = ''
    acceptable_value = ['X', 'O']
    while sym not in acceptable_value:
        sym = input('Type your symbol (X or O): ').upper()
        if sym not in acceptable_value:
            clear_screen()
            print('Sorry, please choose X or O\n')
    return sym

def gameon_choice():
    choice = ''
    acceptable_value = ['Y', 'N']
    while choice not in acceptable_value:
        choice = input('Do you want to play again? (Y/N): ').upper()
        if choice not in acceptable_value:
            clear_screen()
            print('Sorry, please choose Y or N\n')
        elif choice == 'N':
            clear_screen()
            print('Thanks for playing!')
            return False
        else:
            return True

def set_up():
    global board
    global player_1
    global turn
    board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    print('Player 1:')
    player_1 = player_sym()
    turn = 0

def check_winner(matrix, sym, turn, x_pos, y_pos):
    winner = False
    win_line = sym * 3
    check = ''
    # check row
    i = 0
    while not winner and turn >= 4 and i < 3:
        check += matrix[y_pos][i]
        i += 1
    if check == win_line:
        winner = True
        print('row', y_pos)
    # check column
    i = 0
    check = ''
    while not winner and turn >= 4 and i < 3:
        check += matrix[i][x_pos]
        i += 1
    if check == win_line:
        winner = True
        print('column', x_pos)

    # check diagonal
    if not winner and turn >= 4:
        if x_pos == y_pos:      # check top left to down right diagonal
            i = 0
            check = ''
            while not winner and i < 3:
                check += matrix[i][i]
                i += 1
        if check == win_line:
            winner = True
            print('diagonal 1')
        if x_pos + y_pos == 2:  # check top right to down left diagonal
            i = 0
            check = ''
            while not winner and i < 3:
                check += matrix[i][2-i]
                i += 1
        if check == win_line:
            winner = True
            print('diagonal 2')
    return winner

board_num = [['1','2','3'],['4','5','6'],['7','8','9']]
game_on = True
clear_screen()
print('Welcome to Tic Tac Toe!\n')
set_up()

while game_on:
    #clear_screen()
    display(board, 'Here is the current board:')
    display(board_num, 'Here is the board number:')

    if turn % 2 == 0:
        sym = player_1
    else:
        if player_1 == 'X':
            sym = 'O'
        else:
            sym = 'X'

    pos = pos_input()
    x_pos = (pos - 1) % 3
    y_pos = (pos - 1) // 3
    board = save_to_board(board, x_pos, y_pos, sym)

    find_winner = check_winner(board, sym, turn, x_pos, y_pos)

    if find_winner:
        clear_screen()
        display(board, f'Player {turn % 2 + 1} ({sym}) wins! Congratulations!')
        game_on = gameon_choice()
        if game_on:
            clear_screen()
            set_up()
        else:
            break
    elif turn == 8:
        clear_screen()
        display(board, 'The game is a draw!')
        game_on = gameon_choice()
        if game_on:
            clear_screen()
            set_up()
        else:
            break
    else: 
        turn += 1

