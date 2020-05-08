def get_number(index):
    while True:
        user_number = input(f'Digite o peso da {index}ª pessoa: ').replace(',', '.')

        if validate_float_number(user_number):
            return float(user_number)
        else:
            print('Valor inválido.')


def validate_float_number(number_str):
    is_valid = True

    if number_str == '' or number_str[-1] == '.':
        is_valid = False
    else:
        for i in number_str:
            if not (i.isnumeric() or i == '.'):
                is_valid = False

    return is_valid


for i in range(1, 6):
    weight = get_number(i)
    if i == 1:
        smaller_value = weight
        biggest_value = weight

    if weight < smaller_value:
        smaller_value = weight
    if weight > biggest_value:
        biggest_value = weight

formatted_smaller_value = str('{:.1f}'.format(smaller_value)).replace('.', ',')
formatted_biggest_value = str('{:.1f}'.format(biggest_value)).replace('.', ',')

print('\nO menor peso lido foi {}Kg.'.format(formatted_smaller_value))
print('O maior peso lido foi {}Kg.'.format(formatted_biggest_value))
