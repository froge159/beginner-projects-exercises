import random

computerTurn = False
choices = ['rock', 'paper', 'scissors']


def play():
    # player
    player_choice = input("ROCK, PAPER, or SCISSORS. 'Q' to quit: ").lower()
    print(f'You: {player_choice}')
    if player_choice == 'q':
        exit()
    else:
        computer_turn = True

    # computer
    computer_choice = random.choice(choices).lower()
    print(f'Computer: {computer_choice}')

    # win checker
    if player_choice == computer_choice:
        print("It's a TIE!")
    elif player_choice == 'rock' and computer_choice == 'paper' or player_choice == 'paper' and computer_choice == 'scissors' or player_choice == 'scissors' and computer_choice == 'rock':
        print('You lost!')
    elif computer_choice == 'rock' and player_choice == 'paper' or computer_choice == 'paper' and player_choice == 'scissors' or computer_choice == 'scissors' and player_choice == 'rock':
        print('You Won!')


def play_again():
    play_again = input('Play again? Y/N: ').lower()
    print('')
    while play_again == 'y':
        play()
        print('')
        play_again = input('Play again? Y/N: ').lower()
    if play_again == 'n':
        exit()


while True:
    play()
    play_again()
