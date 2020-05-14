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
        user_number = input('Digite um valor: ').replace(',', '.').strip()

        if validate_float_number(user_number):
            if float(user_number).is_integer():
                return int(user_number)
            else:
                return float(user_number)
        else:
            print('Valor inválido.')


def get_option():
    while True:
        user_option = input('Deseja inserir outro número? [S/N] ').strip().upper()

        if user_option == 'S' or user_option == 'N':
            return user_option
        else:
            print('Opção inválida.')


numbers_list = []
while True:
    numbers_list.append(get_number())

    if get_option() == 'N':
        break

print(f'Você digitou {len(numbers_list)} elementos.')
print(f'Os valores em ordem decrescente são: {numbers_list}')
numbers_list.sort(reverse=True)

if 5 in numbers_list:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')
