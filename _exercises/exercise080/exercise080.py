def validate_float_number(number_str):
    is_valid = True

    if number_str == '' or number_str[-1] == '.':
        is_valid = False
    else:
        for i in number_str:
            if not (i.isnumeric() or i == '.'):
                is_valid = False

    return is_valid


def get_number(msg_index):
    message = ('primeiro', 'segundo', 'terceiro', 'quarto', 'quinto')
    while True:
        user_number = input(f'Digite o {message[msg_index]} valor: ').replace(',', '.')

        if validate_float_number(user_number):
            if float(user_number).is_integer():
                return int(user_number)
            else:
                return float(user_number)
        else:
            print('Valor inválido.')


numbers_list = []

for i in range(0, 5):
    number = get_number(i)

    if i == 0 or number > numbers_list[-1]:
        numbers_list.append(number)
        print('Adicionado ao final da lista.')
    else:
        if number < numbers_list[0]:
            numbers_list.insert(0, number)
            print('Adicionado a posição 0.')
        else:
            for i in range(0, len(numbers_list)-1):
                if numbers_list[i] < number < numbers_list[i + 1]:
                    numbers_list.insert(i+1, number)
                    print(f'Adicionado a posição {i+1}')
                    break

print(f'\nOs valores digitados foram: {numbers_list}')
