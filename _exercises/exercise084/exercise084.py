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
        user_number = input('Peso: ').replace(',', '.')

        if validate_float_number(user_number):
            if float(user_number).is_integer():
                return int(user_number)
            else:
                return float(user_number)
        else:
            print('Valor inválido.')


def get_option():
    while True:
        user_option = input('Deseja cadastrar outro usuário? [S/N] ').strip().upper()

        if user_option == 'S' or user_option == 'N':
            return user_option
        else:
            print('Opção inválida.')


users_list = []
max_weight = min_weight = 0
while True:
    user = [input('Nome: ').strip().capitalize(), (get_number())]

    if not users_list:
        max_weight = min_weight = user[1]
    else:
        if user[1] > max_weight:
            max_weight = user[1]
        if user[1] < min_weight:
            min_weight = user[1]

    users_list.append(user[:])

    option = get_option()
    if option == 'N':
        break

print(f'Foram cadastradas {len(users_list)} pessoas.')

max_weight_names = []
min_weight_names = []
for i in users_list:
    if i[1] == min_weight:
        min_weight_names.append(i[0])
    if i[1] == max_weight:
        max_weight_names.append(i[0])

print(f'O maior peso cadastrado foi {max_weight}Kg. Peso de: {max_weight_names}')
print(f'O menor peso registrado foi {min_weight}Kg. Peso de: {min_weight_names}')
