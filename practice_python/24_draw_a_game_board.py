# This exercise is Part 1 of 4 of the Tic Tac Toe exercise series.

# Time for some fake graphics! Let’s say we want to draw game boards that look like this:

#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---

# This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

# Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.


def draw_game_board(rows, cols):

    dashes = ' ---' * (cols)
    pipes = '|   ' * (cols) + '|'

    for i in range(rows + 1):
        if i < rows:
            print(dashes)
            print(pipes)
        else:
            print(dashes)


def run():
    print('Welcome to the Game Board Drawer!')
    rows = int(input('\nGive me the number of rows you want: '))
    cols = int(input('\nGive me the number of columns you want: '))
    draw_game_board(rows, cols)


if __name__ == '__main__':
    run()
