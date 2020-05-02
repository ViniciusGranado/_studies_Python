from math import sqrt


def validate_number(number_str):
    is_valid = True

    if number_str == '' or number_str[-1] == '.':
        is_valid = False

    for i in number_str:
        if not (i.isnumeric() or i == '.'):
            is_valid = False

    return is_valid


def get_value(index):
    is_number_valid = False
    mensagem = ['Comprimento do cateto oposto: ', 'Comprimento do cateto adjacente: ']

    while not is_number_valid:
        number_str = input(mensagem[index]).replace(',', '.')
        is_number_valid = validate_number(number_str)

        if is_number_valid:
            converted_number = float(number_str)
            return converted_number
        else:
            print('Valor inválido, tente novamente.')


def get_hypotenuse(opp, adj):
    hypo = sqrt((opp**2)+(adj**2))
    return hypo


opposite = get_value(0)
adjacent = get_value(1)
hypotenuse = get_hypotenuse(opposite, adjacent)
print('A hipotenusa irá medir {:.2f}.'.format(hypotenuse))
