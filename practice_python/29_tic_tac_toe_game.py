import os
import time

# This exercise is Part 4 of 4 of the Tic Tac Toe exercise series.

# In 3 previous exercises, we built up a few components needed to build a Tic Tac Toe game in Python:

# Draw the Tic Tac Toe game board
# Checking whether a game board has a winner
# Handle a player move from user input
# The next step is to put all these three components together to make a two-player Tic Tac Toe game!
# Your challenge in this exercise is to use the functions from those previous exercises all together in the same program to make a two-player game that you can play with a friend.
# There are a lot of choices you will have to make when completing this exercise, so you can go as far or as little as you want with it.

# Here are a few things to keep in mind:

# You should keep track of who won - if there is a winner, show a congratulatory message on the screen.
# If there are no more moves left, don’t ask for the next player’s move!
# As a bonus, you can ask the players if they want to play again and keep a running tally of who won more - Player 1 or Player 2.


def gotoxy(x, y):
    print("%c[%d;%df" % (0x1B, x, y), end='')


def draw_game_board(rows, cols):
    gotoxy(0, 0)

    dashes = ' ---' * (cols)
    pipes = '|   ' * (cols) + '|'

    for i in range(rows + 1):
        if i < rows:
            print(dashes)
            print(pipes)
        else:
            print(dashes)


def print_game(gameboard):

    gotoxy(2, 3)
    print(gameboard[0][0])

    gotoxy(2, 7)
    print(gameboard[0][1])

    gotoxy(2, 11)
    print(gameboard[0][2])

    gotoxy(4, 3)
    print(gameboard[1][0])

    gotoxy(4, 7)
    print(gameboard[1][1])

    gotoxy(4, 11)
    print(gameboard[1][2])

    gotoxy(6, 3)
    print(gameboard[2][0])

    gotoxy(6, 7)
    print(gameboard[2][1])

    gotoxy(6, 11)
    print(gameboard[2][2])

    gotoxy(10, 0)


def get_play(player, gameboard):

    player = player.upper()

    if player == 'A':
        token = 'x'
    else:
        token = 'o'

    while True:
        play = input(f'\nPlayer {player} - Give me the coordinates [x y]: ')
        play = play.split()

        if len(play) != 2:
            print('\nInvalid input!')
            continue

        try:
            play_x = int(play[0])
            play_y = int(play[1])
        except ValueError:
            print('\nInvalid input!')
            continue

        if play_x not in range(1, 4) or play_y not in range(1, 4):
            print('\nInvalid Coordinates!')
            continue

        if gameboard[play_x - 1][play_y - 1] != ' ':
            print('\nThat place is already taken!')
            continue

        gameboard[play_x - 1][play_y - 1] = token
        break

    os.system('cls')
    draw_game_board(3, 3)
    print_game(gameboard)


def display_menu():
    os.system('cls')
    choice = input('''
    Welcome to the Tic Tac Toe game (⌐■_■)

    [p]lay 🎮
    [i]nstructions 👽
    [q]uit 💔

    Enter an option: ''')
    return choice


def display_instructions():
    os.system('cls')
    print('''
    How to Play 🤔

    This game is a two player game. Each one must give the coordinates
    where he wants to put his token, in the format [row column], from
    1 to 3 rows and 1 to 3 columns, for example:

    1 1 <-- ✅ Valid coordinate
    2 3 <-- ✅ Valid coordinate
    4 1 <-- ❌ Invalid coordinate

    Are you ready? 😎''')
    input('\nPress enter to return to menu')


def check_game(game_board):
    # Rows check
    for row in game_board:
        if len(set(row)) == 1 and ' ' not in set(row):
            if row[0] == 'x':
                return 1
            if row[0] == 'o':
                return 2

    # Columns check
    for i in range(0, 3):
        col = []
        for row in game_board:
            col.append(row[i])
        if len(set(col)) == 1 and ' ' not in set(col):
            if col[0] == 'x':
                return 1
            if col[0] == 'o':
                return 2

    # Diagonals check
    diagonal1 = [game_board[0][0], game_board[1][1], game_board[2][2]]
    if len(set(diagonal1)) == 1 and ' ' not in set(diagonal1):
        if diagonal1[0] == 'x':
            return 1
        if diagonal1[0] == 'o':
            return 2

    diagonal2 = [game_board[0][2], game_board[1][1], game_board[2][0]]
    if len(set(diagonal2)) == 1 and ' ' not in set(diagonal2):
        if diagonal2[0] == 'x':
            return 1
        if diagonal2[0] == 'o':
            return 2

    # If none won
    return 0


def play():
    playing = True
    game = [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]
    player_1_wins = 0
    player_2_wins = 0

    while playing:
        os.system('cls')

        draw_game_board(3, 3)
        print_game(game)

        while True:
            get_play('a', game)
            check = check_game(game)
            if check != 0:
                break

            if ' ' not in game[0] and ' ' not in game[1] and ' ' not in game[2]:
                check = 0
                break

            get_play('b', game)
            check = check_game(game)
            if check != 0:
                break

            if ' ' not in game[0] and ' ' not in game[1] and ' ' not in game[2]:
                check = 0
                break

        if check == 0:
            print('\nDraw ¯\_(ツ)_/¯')
        elif check == 1:
            print('\nPlayer 1 wins ☜(ﾟヮﾟ☜)')
            player_1_wins += 1
        elif check == 2:
            print('\nPlayer 2 wins ☜(ﾟヮﾟ☜)')
            player_2_wins += 1

        retry = input('\nDo you want to play again? [y]es, [n]o: ')
        while retry != 'y' and retry != 'n':
            print('\nEnter a valid option!')
            retry = input('\nDo you want to play again? [y]es, [n]o: ')

        if retry == 'y':
            game = [[' ', ' ', ' '],
                    [' ', ' ', ' '],
                    [' ', ' ', ' ']]
            continue
        elif retry == 'n':
            print(f'\nPlayer 1 wins = {player_1_wins}')
            print(f'Player 2 wins = {player_2_wins}')
            print('\nThank you for playing!')
            input('\nPress enter to return to the menu')
            break


def run():
    choice = display_menu()
    while choice != 'q':
        if choice == 'p':
            play()
        elif choice == 'i':
            display_instructions()
        else:
            print('\nInvalid option!')
            time.sleep(1)
        choice = display_menu()


if __name__ == '__main__':
    run()
