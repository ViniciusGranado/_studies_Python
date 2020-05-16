def area(w, l):
    area_terrain = w * l
    print(f'A área de um terreno {w}x{l} é de {area_terrain}m².')


def validate_float_number(number_str):
    if number_str == '' or number_str[-1] == '.':
        return False
    else:
        for i in number_str:
            if not (i.isnumeric() or i == '.'):
                return False

    return True


def get_number(msg_index):
    message = ('Largura: ', 'Comprimento: ')
    while True:
        user_number_str = input(message[msg_index]).strip().replace(',', '.')
        if validate_float_number(user_number_str):
            if float(user_number_str).is_integer():
                return int(user_number_str)
            else:
                return float(user_number_str)
        else:
            print('Valor inválido, tente novamente.')


print('Controle de terrenos')
print('-'*20)

width = get_number(0)
length = get_number(1)

area(width, length)
