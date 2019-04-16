def display_board(board):
    print(' ', board[1], ' | ', board[2], ' | ', board[3], ' ')
    print('-----------------')
    print(' ', board[4], ' | ', board[5], ' | ', board[6], ' ')
    print('-----------------')
    print(' ', board[7], ' | ', board[8], ' | ', board[9], ' ')


def choose_symbol():
    player1 = ''
    player2 = ''
    while player1 != 'X' or player1 != 'O':

        player1 = input("What symbol do you prefer? 'X' or 'O'? ").upper()

        if player1 == 'X':
            player2 = 'O'
            return (player1, player2)
            break

        elif player1 == 'O':
            player2 = 'X'
            return (player1, player2)
            break

    print('(Player 1, Player 2) : ', (player1, player2))


def turn():
    from random import randint
    i = randint(1, 2)
    if i == 1:
        return player1
    else:
        return player2


def check_if_win():
    return (board[1] == board[2] == board[3] == player1 or board[1] == board[2] == board[3] == player2) or (
                board[4] == board[5] == board[6] == player1 or board[4] == board[5] == board[6] == player2) or (
                       board[7] == board[8] == board[9] == player1 or board[7] == board[8] == board[9] == player2) or (
                       board[1] == board[4] == board[7] == player1 or board[1] == board[4] == board[7] == player2) or (
                       board[5] == board[2] == board[8] == player1 or board[5] == board[2] == board[8] == player2) or (
                       board[6] == board[9] == board[3] == player1 or board[6] == board[9] == board[3] == player2) or (
                       board[1] == board[5] == board[9] == player1 or board[1] == board[5] == board[9] == player2) or (
                       board[5] == board[7] == board[3] == player1 or board[5] == board[7] == board[3] == player2)


def check_tie():
    return (board[1] == 'X' or board[1] == 'O') and (board[2] == 'X' or board[2] == 'O') and (
                board[3] == 'X' or board[3] == 'O') and (board[4] == 'X' or board[4] == 'O') and (
                       board[5] == 'X' or board[5] == 'O') and (board[6] == 'X' or board[6] == 'O') and (
                       board[7] == 'X' or board[7] == 'O') and (board[8] == 'X' or board[8] == 'O') and (
                       board[9] == 'X' or board[9] == 'O')


def assignment(player):
    number = ''
    while number != '1' or number != '2' or number != '3' or number != '4' or number != '5' or number != '6' or number != '7' or number != '8' or number != '9':
        number = int(input('Chose a position in a range of 1-9 that was not chosed before: '))
        if board[number] == '1' or board[number] == '2' or board[number] == '3' or board[number] == '4' or board[
            number] == '5' or board[number] == '6' or board[number] == '7' or board[number] == '8' or board[
            number] == '9':
            board[number] = player
            break
        elif board[number] == player1 or board[number] == player2:
            print('Should you chose a position that was not chosed before!')
            continue


def gameon():
    game_on = input('Are you ready to start the game? Yes or No?')
    if game_on[0].upper() == 'Y':
        return True
    else:
        print('Ok, return when you get ready!')


def replay():
    return input('Do you want to play again? ').upper().startswith('Y')


while True:
    print('Welcome to Tic Tac Toe! \n')
    board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    print('This is the board and the positions!')
    print('\n')
    display_board(board)
    print('\n')
    (player1, player2) = choose_symbol()
    time = turn()
    gameon()
    while gameon():
        if time == player1:
            print('\n' * 100)
            print("It is Player 1's time!")
            print('\n')
            display_board(board)
            assignment(player1)
            if check_if_win():
                print('Congradulation, Player 1 Won the game!\n')
                display_board(board)
                break
            elif check_tie():
                print('This game is Draw!\n')
                display_board(board)
                break
            else:
                print('\n' * 100)
                print("It is Player 2's time!")
                print('\n')
                display_board(board)
                assignment(player2)
                if check_if_win():
                    print('Congradulation, Player 2 Won the game!\n')
                    display_board(board)
                    break
                elif check_tie():
                    print('This game is Draw!\n')
                    display_board(board)
                    break

        elif time == player2:
            print('\n' * 100)
            print("It is Player 2's time!")
            print('\n')
            display_board(board)
            assignment(player2)
            if check_if_win():
                print('Congradulation, Player 2 Won the game!\n')
                display_board(board)
                break
            elif check_tie():
                print('This game is Draw!\n')
                display_board(board)
                break
            else:
                print('\n' * 100)
                print("It is Player 1's time!")
                print('\n')
                display_board(board)
                assignment(player1)
                if check_if_win():
                    print('Congradulation, Player 1 Won the game!\n')
                    display_board(board)
                    break
                elif check_tie():
                    print('This game is Draw!\n')
                    display_board(board)
                    break

    if not replay():
        print('Thank you for playing!')
        break
