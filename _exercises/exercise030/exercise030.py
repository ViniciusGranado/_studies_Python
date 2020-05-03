def validate_number(str_number):
    is_valid = True

    if str_number == '' or str_number[-1] == '.':
        is_valid = False

    for i in str_number:
        if not (i.isnumeric() or i == '.'):
            is_valid = False

    return is_valid


def get_number():
    is_number_valid = False

    while not is_number_valid:
        user_number_str = input('Digite um número: ').replace(',', '.')
        is_number_valid = validate_number(user_number_str)

        if is_number_valid:
            if '.' in user_number_str:
                print('Números com casas decimais não são possuem a classificação \'Par\' ou \'Ímpar\'.')
                is_number_valid = False
            else:
                return int(user_number_str)
        else:
            print('Valor inválido, tente novamente.')


number = get_number()
remainder = number % 2

if remainder == 0:
    print(f'O número {number} é Par.')
else:
    print(f'O número {number} é Ímpar.')