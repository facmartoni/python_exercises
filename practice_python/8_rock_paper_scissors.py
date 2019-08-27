# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock


def run():

    print(' R O C K  P A P E R  S C I S S O R S')
    print('\n Welcome to the Rock Paper Scissors game. \n It has two players, and they have to type "rock", "paper" or "scissors" to play')
    print("\n Let's play! ")

    decision = ''
    while decision != 's':

        while True:
            play_a = input('\n Player A: ').lower()
            if play_a != "rock" and play_a != "paper" and play_a != "scissors":
                print('Type a valid play!')
                continue
            break
        while True:
            play_b = input('\n Player B: ').lower()
            if play_b != "rock" and play_b != "paper" and play_b != "scissors":
                print('Type a valid play!')
                continue
            break

        if play_a == 'rock':
            if play_b == 'rock':
                print('\n Draw')
            if play_b == 'paper':
                print('\n Player B wins!')
            if play_b == 'scissors':
                print('\n Player A wins!')

        if play_a == 'paper':
            if play_b == 'rock':
                print('\n Player A wins!')
            if play_b == 'paper':
                print('\n Draw')
            if play_b == 'scissors':
                print('\n Player B wins!')

        if play_a == 'scissors':
            if play_b == 'rock':
                print('\n Player B wins!')
            if play_b == 'paper':
                print('\n Player A wins!')
            if play_b == 'scissors':
                print('\n Draw')

        decision = input(
            '\n Do you want to play again? Press enter. Otherwise type "s": ')


if __name__ == '__main__':
    run()
