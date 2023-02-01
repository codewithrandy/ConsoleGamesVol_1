import os
import random
import sys


def menu():
    is_playing = input('Wanna Play? (Y/N) ')
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
    weapons = ['r', 'p', 's']
    cpu = random.choice(weapons)
    print('Choose your weapon ...')
    print('r .. Rock')
    print('p .. Paper')
    print('s .. Scissors')
    player = input().lower()
    if player == cpu:
        is_tie()
    is_winner = did_win(cpu, player)
    clear_screen()
    if is_winner:
        print(f'Congrats !!! {get_weapon(player)} beats {get_weapon(cpu)}')
    else:
        print(f'Sorry !!! {get_weapon(cpu)} beats {get_weapon(player)}')
    menu()


def is_tie():
    clear_screen()
    print('Game was a tie !!')
    menu()


def get_weapon(weapon) -> str:
    match weapon:
        case 'r':
            return 'Rock'
        case 'p':
            return 'Paper'
        case 's':
            return 'Scissors'


def did_win(cpu, player):
    if player == 'r' and cpu == 's' \
            or player == 'p' and cpu == 'r' \
            or player == 's' and cpu == 'p':
        return True
    return False


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
