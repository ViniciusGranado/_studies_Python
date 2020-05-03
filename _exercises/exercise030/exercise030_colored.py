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
        user_number_str = input('\033[35mDigite um número: \033[m').replace(',', '.')
        is_number_valid = validate_number(user_number_str)

        if is_number_valid:
            if '.' in user_number_str:
                print('\033[32mNúmeros com casas decimais não são possuem a classificação \'Par\' ou \'Ímpar\'.\033[m')
                is_number_valid = False
            else:
                return int(user_number_str)
        else:
            print('\033[31mValor inválido, tente novamente.\033[m')


number = get_number()
remainder = number % 2

if remainder == 0:
    print(f'O número {number} é \033[34mPar\033[m.')
else:
    print(f'O número {number} é \033[34mÍmpar\033[m.')