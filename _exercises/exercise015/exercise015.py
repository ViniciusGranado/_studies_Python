def validate_number(number, index):
    is_valid = True

    if index == 0:  # If number is Int
        if not number.isnumeric():
            is_valid = False

    else:  # If number is Float
        if number == '' or number[-1] == '.':
            is_valid = False
        else:
            for i in number:
                if not (i.isnumeric() or i == '.'):
                    is_valid = False

    return is_valid


def convert_str_to_number(number, index):
    if index == 0:  # If number is Int
        converted_number = int(number)
    else:  # If number if float
        converted_number = float(number)

    return converted_number


def get_values(index):
    message = ['Total de dias de aluguel: ', 'Total de Km rodados: ']
    is_valid = False

    while not is_valid:
        value_str = input(message[index])
        is_valid = validate_number(value_str, index)

        if is_valid:
            converted_value = convert_str_to_number(value_str, index)
            return converted_value
        else:
            print('Valor inválido, tente novamente.')


days = get_values(0)
km = get_values(1)

rent_value = (days*60) + (km*0.15)
converted_rent_value = str('%.2f' % rent_value).replace('.', ',')

print('O total a pagar é R${}'.format(converted_rent_value))
