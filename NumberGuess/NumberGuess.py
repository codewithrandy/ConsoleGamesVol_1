import os
import random
import sys


def menu():
    letsplay = input('Shall we play a game? (Y/N) ')
    letsplay = letsplay.lower()
    if letsplay == 'y' or letsplay == 'yes':
        clear_screen()
        start_game()
    elif letsplay == 'n' or letsplay == 'no':
        game_over()
    else:
        clear_screen()
        print('Please answer Y or N')
        menu()


def start_game():
    x = random.randint(1, 50)
    tries = 0
    guess = input('Guess a number between 1 and 50: ')
    if guess.isnumeric():
        guess = int(guess)
        tries += 1
    else:
        print(guess, 'is not a number')
        start_game()

    while True:
        if guess == x:
            clear_screen()
            print('YOU DID IT !!!')
            print('and it only took you', tries, 'guesses')
            menu()
        elif guess < x:
            clear_screen()
            print('Too Low')
            guess = check_input(guess)
            tries += 1
        elif guess > x:
            clear_screen()
            print('Too High')
            guess = check_input(guess)
            tries += 1


def check_input(x):
    # MAKE SURE THE USER INPUT A NUMBER
    while True:
        x = input('Guess Again: ')
        if x.isnumeric():
            x = int(x)
            return x
        else:
            clear_screen()
            print('That was not a number')


def clear_screen():
    # CLEARS THE CONSOLE SCREEN
    a = sys.platform
    if a == 'win32':
        os.system('cls')
    else:
        os.system('clear')


def game_over():
    clear_screen()
    print('Goodbye')
    sys.exit()


menu()

# EXPANSION IDEAS
# ADD LEVELS - PLAY ANOTHER GAME = INCREASES NUMBER RANGE
# ADD MORE DIFFICULTY - LIMITS THE NUMBER OF GUESSES BEFORE GAMEOVER
# ARCADE STYLE HIGH SCORE SYSTEM - STORES TO A FILE