def validate_float_number(number_str):
    is_valid = True

    if number_str == '' or number_str[-1] == '.':
        is_valid = False
    else:
        for i in number_str:
            if not (i.isnumeric() or i == '.'):
                is_valid = False

    return is_valid


def get_number(index):
    message = ['primeiro', 'segundo']
    while True:
        user_number = input(f'Digite o {message[index]} número: ').replace(',', '.')

        if validate_float_number(user_number):
            return float(user_number)
        else:
            print('Valor inválido.')


first_number = get_number(0)
second_number = get_number(1)

if first_number > second_number:
    print('O PRIMEIRO número é maior')
elif second_number > first_number:
    print('O SEGUNDO número é maior')
else:
    print('Os dois valores são IGUAIS')
