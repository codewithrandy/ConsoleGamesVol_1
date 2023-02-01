import os
import random
import sys

def menu():
    is_playing = input('Ready to Play? (Y/N) ')
    is_playing = is_playing.lower()
    if is_playing == 'y' or is_playing == 'yes':
        clear_screen()
        start_game()
    elif is_playing == 'n' or is_playing == 'no':
        game_over()
    else:
        clear_screen()
        print('Please answer Y or N')
        menu()


def start_game():
    weapons = ['rock', 'paper', 'scissors']
    cpu = random.choice(weapons)
    print('Choose your weapon ...')
    print('R - Rock')
    print('P - Paper')
    print('S - Scissors')
    player = input()
    get_winner(cpu, player)


def get_winner(cpu, player):
    pass


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