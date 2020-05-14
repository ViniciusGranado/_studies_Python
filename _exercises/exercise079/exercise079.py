def validate_float_number(number_str):
    is_valid = True

    if number_str == '' or number_str[-1] == '.':
        is_valid = False
    else:
        for i in number_str:
            if not (i.isnumeric() or i == '.'):
                is_valid = False

    return is_valid


def get_number():
    while True:
        user_number = input('Digite o valor desejado: ').replace(',', '.')

        if validate_float_number(user_number):
            if float(user_number).is_integer():
                return int(user_number)
            else:
                return float(user_number)
        else:
            print('Valor inválido.')


def get_answer():
    while True:
        user_answer = input('Deseja adicionar outro valor? [S/N] ').strip().upper()

        if user_answer == 'S' or user_answer == 'N':
            return user_answer
        else:
            print('Opção inválida, tente novamente.')


numbers = []
while True:
    number = get_number()

    if number not in numbers:
        numbers.append(number)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor já consta na lista.')

    option = get_answer()

    if option == 'N':
        break

print(f'\nOs valores digitados foram {sorted(numbers)}')
