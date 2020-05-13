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
        user_number_str = input(f'Digite o {message[msg_index]} número: ').replace(',', '.').strip()

        if validate_float_number(user_number_str):
            if float(user_number_str).is_integer():
                return int(user_number_str)
            else:
                return float(user_number_str)
        else:
            print('Valor inválido.')


def get_formatted_indexes(number):
    max_number_positions = []
    for index, item in enumerate(numbers):
        if item == number:
            max_number_positions.append(index)

    max_number_positions_message = ''
    for index, item in enumerate(max_number_positions):
        if index == len(max_number_positions)-1:
            max_number_positions_message += f' e {item}'
        elif index == 0:
            max_number_positions_message += f'{item}'
        else:
            max_number_positions_message += f', {item}'

    return max_number_positions_message


numbers = []
for i in range(0, 5):
    numbers.append(get_number(i))

print('Você digitou os valores: ', end='')
for index, item in enumerate(numbers):
    if index == len(numbers)-1:
        print(item)
    else:
        print(item, end=', ')

if numbers.count(max(numbers)) == 1:
    print(f'O maior valor digitado foi {max(numbers)} na posição {numbers.index((max(numbers)))}.')
else:
    print(f'O maior valor digitado foi {max(numbers)} nas posições {get_formatted_indexes(max(numbers))}.')

if numbers.count(min(numbers)) == 1:
    print(f'O menor valor digitado foi {min(numbers)} na posição {numbers.index(min(numbers))}.')
else:
    print(f'O menor valor digitado foi {min(numbers)} nas posições {get_formatted_indexes(min(numbers))}.')
