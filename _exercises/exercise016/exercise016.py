from math import trunc


# Functions
def validate_number(number_str):
    is_valid = True

    if number_str == '' or number_str[-1] == '.':
        is_valid = False

    for i in number_str:
        if not (i.isnumeric() or i == '.'):
            is_valid = False

    return is_valid


def get_number():
    is_number_valid = False

    while not is_number_valid:
        number_str = input('Digite um número: ').replace(',', '.')
        is_number_valid = validate_number(number_str)

        if is_number_valid:
            converted_number = float(number_str)
            return converted_number
        else:
            print('Valor inválido, tente novamente.')


def get_integer_part(float_number):
    return trunc(float_number)


# Algorithm
number = get_number()
formatted_number = (str(number)).replace('.', ',')
integer_part = get_integer_part(number)

print('O valor digitado foi {} e a sua porção inteira é {}.'.format(formatted_number, integer_part))
