import os
import random
import sys
from time import sleep


def menu():
    clear_screen()
    letsplay = input('Do you seek guidance from the Magic 8 Ball? ')
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
    print('Then the Magic 8 Ball shall provide you with the answers you seek most ...')
    sleep(2)
    print(input('Tell me what you wish to know : '))
    shake_ball()
    replies = [
        'It is certain',
        'Reply hazy, try again',
        'Don’t count on it',
        'It is decidedly so',
        'Ask again later',
        'My reply is no',
        'Without a doubt',
        'Better not tell you now',
        'My sources say no',
        'Yes – definitely',
        'Cannot predict now',
        'Outlook not so good',
        'You may rely on it',
        'Concentrate and ask again',
        'Very doubtful',
        'As I see it, yes',
        'Most likely',
        'Outlook good',
        'Yes',
        'Signs point to yes'
    ]
    print(random.choice(replies))
    sleep(4)
    menu()


def shake_ball():
    # RETRO GAME TEXT EFFECT FOR THE SHAKE
    clear_screen()
    print('... hmmmm ... Let\'s find out.\n')
    type_fx('SHAKE . . SHAKE . . SHAKE . . . ')
    clear_screen()


def type_fx(text):
    for i in text:
        print(i, end='')
        sleep(.2)
    sleep(1.5)
    print("")


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