from random import randint


# Functions
def validate_number(str_number):
    is_valid = True

    if not (str_number.isnumeric() and (0 <= int(str_number) <= 10)):
        is_valid = False

    return is_valid


def get_user_number():

    while True:
        user_number_str = input('Em que número eu pensei? ')
        is_number_valid = validate_number(user_number_str)

        if is_number_valid:
            return int(user_number_str)
        else:
            print('Número inválido.')
            print()


# Header
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)

# Body
game_number = randint(0, 10)
user_number = get_user_number()
is_guess_right = game_number == user_number
number_of_tries = 1

while not is_guess_right:
    if game_number > user_number:
        print('Mais... Tente mais uma vez.')
    else:
        print('Menos, tente mais uma vez.')
    print()
    user_number = get_user_number()
    is_guess_right = user_number == game_number
    number_of_tries += 1
    
print()
print(f'Acertou com {number_of_tries} tentativas. Parabéns')
