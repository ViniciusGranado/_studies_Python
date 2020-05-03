from random import randint
from time import sleep


# Functions

def validate_number(str_number):
    is_valid = True

    if not (str_number.isnumeric() and (0 <= int(str_number) <= 5)):
        is_valid = False

    return is_valid


def get_user_number():
    is_number_valid = False

    while not is_number_valid:
        user_number_str = input('Em que número eu pensei? ')
        is_number_valid = validate_number(user_number_str)

        if is_number_valid:
            return int(user_number_str)
        else:
            print('Número inválido.')


# Header
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

# Body
game_number = randint(0, 5)
user_number = get_user_number()
is_guess_right = game_number == user_number

print('PROCESSANDO...')
sleep(2)

if is_guess_right:
    print('PARABENS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {game_number} e não no {user_number}!')

