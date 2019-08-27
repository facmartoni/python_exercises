import os

# This exercise is Part 2 of 4 of the Tic Tac Toe exercise series.

# As you may have guessed, we are trying to build up to a full tic-tac-toe board. However, this is significantly more than half an hour of coding, so we’re doing it in pieces.

# Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.

# If a game of Tic Tac Toe is represented as a list of lists, like so:

# game = [[1, 2, 0],
#         [2, 1, 0],
# 	      [2, 1, 1]]

# where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2 put their token in that space.

# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.


def check_game(game_board):
    # Rows check
    for row in game_board:
        if len(set(row)) == 1:
            if row[0] == 1:
                return 1
            if row[0] == 2:
                return 2

    # Columns check
    for i in range(0, 3):
        col = []
        for row in game_board:
            col.append(row[i])
        if len(set(col)) == 1:
            if col[0] == 1:
                return 1
            if col[0] == 2:
                return 2

    # Diagonals check
    diagonal1 = [game_board[0][0], game_board[1][1], game_board[2][2]]
    if len(set(diagonal1)) == 1:
        if diagonal1[0] == 1:
            return 1
        if diagonal1[0] == 2:
            return 2

    diagonal2 = [game_board[0][2], game_board[1][1], game_board[2][0]]
    if len(set(diagonal2)) == 1:
        if diagonal2[0] == 1:
            return 1
        if diagonal2[0] == 2:
            return 2

    # If none won
    return 0


def run():
    os.system('cls')
    print('Welcome to the Tic Tac Toe checker!')

    game = [[1, 2, 0],
            [2, 1, 0],
            [2, 1, 0]]

    result = check_game(game)
    if result == 0:
        print('\nDraw ¯\_(ツ)_/¯')
    elif result == 1:
        print('\nPlayer 1 wins ☜(ﾟヮﾟ☜)')
    elif result == 2:
        print('\nPlayer 2 wins ☜(ﾟヮﾟ☜)')


if __name__ == '__main__':
    run()
