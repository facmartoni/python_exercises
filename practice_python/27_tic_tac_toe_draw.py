import os
import time

# This exercise is Part 3 of 4 of the Tic Tac Toe exercise series.

# In a previous exercise we explored the idea of using a list of lists as a “data structure” to store information about a tic tac toe game.
# In a tic tac toe game, the “game server” needs to know where the Xs and Os are in the board, to know whether player 1 or player 2 (or whoever is X and O won).

# There has also been an exercise about drawing the actual tic tac toe gameboard using text characters.

# The next logical step is to deal with handling user input.
# When a player (say player 1, who is X) wants to place an X on the screen, they can’t just click on a terminal.
# So we are going to approximate this clicking simply by asking the user for a coordinate of where they want to place their piece.

# As a reminder, our tic tac toe game is really a list of lists. The game starts out with an empty game board like this:

# game = [[0, 0, 0],
# 	     [0, 0, 0],
# 	     [0, 0, 0]]

# The computer asks Player 1 (X) what their move is (in the format row,col), and say they type 1,3.
# Then the game would print out

# game = [[0, 0, X],
# 	     [0, 0, 0],
# 	     [0, 0, 0]]

# And ask Player 2 for their move, printing an O in that place.

# Things to note:

# For this exercise, assume that player 1 (the first player to move) will always be X and player 2 (the second player) will always be O.
# Notice how in the example I gave coordinates for where I want to move starting from (1, 1) instead of (0, 0).
# To people who don’t program, starting to count at 0 is a strange concept, so it is better for the user experience if the row counts and column counts start at 1. This is not required, but whichever way you choose to implement this, it should be explained to the player.
# Ask the user to enter coordinates in the form “row,col” - a number, then a comma, then a number.
# Then you can use your Python skills to figure out which row and column they want their piece to be in.
# Don’t worry about checking whether someone won the game, but if a player tries to put a piece in a game position where there already is another piece, do not allow the piece to go there.

# Bonus:

# For the “standard” exercise, don’t worry about “ending” the game - no need to keep track of how many squares are full.
# In a bonus version, keep track of how many squares are full and automatically stop asking for moves when there are no more valid moves.


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

        play_x = int(play[0])
        play_y = int(play[1])

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


def run():

    playing = True
    game = [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]

    while playing:
        os.system('cls')

        draw_game_board(3, 3)
        print_game(game)

        get_play('a', game)
        get_play('b', game)

        if ' ' not in game:
            playing = False


if __name__ == '__main__':
    run()
