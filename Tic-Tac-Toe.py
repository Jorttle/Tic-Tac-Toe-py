board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
turn = 'X'
num_turns = 0
def print_board():
    print(board[0], '|', board[1], '|', board[2], '            1   2   3 ')
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5], '            4   5   6 ')
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8], '            7   8   9 ')


# Check if all items in a row/column/diagonal are the same. Essentially checks if someone won.
def check_list(r1):
    if len(set(r1)) == 1:
        print(f"It looks like {turn} won!")
        print(turn * 100)
        exit()
    
# Defining rows, columns, and diagonals.
def define_board():
    global r1, r2, r3, c1, c2, c3, d1, d2
    r1 = [board[0], board[1], board[2]]
    r2 = [board[3], board[4], board[5]]
    r3 = [board[6], board[7], board[8]]

    c1 = [board[0], board[3], board[6]]
    c2 = [board[1], board[4], board[7]]
    c3 = [board[2], board[5], board[8]]

    d1 = [board[0], board[4], board[8]]
    d2 = [board[2], board[4], board[6]]



print('\n\n\n\n\n\n\n\n\n\n\n\n\n')
print_board()

while num_turns < 9:
    num_turns += 1
    selection = int(input(f'What spot would {turn} like to go in?\n'))
    # subtract 1 from selection so that user input goes from 1-9 instead of 0-8
    selection -= 1
    print('\n\n\n\n\n\n')
    # Check if space is occupied
    if board[selection] != 'X' and board[selection] != 'O':
        board[selection] = turn

        print_board()
        # Start checking winners
        if num_turns >= 5:
            define_board()
            # Check for winners
            if selection == 0:
                check_list(r1)
                check_list(c1)
                check_list(d1)
            elif selection == 1:
                check_list(r1)
                check_list(c2)
            elif selection == 2:
                check_list(r1)
                check_list(c3)
                check_list(d2)
            elif selection == 3:
                check_list(r2)
                check_list(c1)
            elif selection == 4:
                check_list(r2)
                check_list(c2)
                check_list(d1)
                check_list(d2)
            elif selection == 5:
                check_list(r2)
                check_list(c3)
            elif selection == 6:
                check_list(r3)
                check_list(c1)
                check_list(d2)
            elif selection == 7:
                check_list(r3)
                check_list(c2)
            elif selection == 8:
                check_list(r3)
                check_list(c3)
                check_list(d1)
            
            
        # Next player's turn
        if turn == 'X':
            turn = 'O'
        elif turn == 'O':
            turn = 'X'
            #
    # If space is occupied:
    elif board[selection] == 'X' or board[selection] == 'O':
        print('It looks like that space is occupied. Please try again')
        num_turns -= 1
        print_board()
# If nobody won at the end
print('Looks like it was a tie!')


