from math import sin, cos, tan, radians


def validate_number(number_str):
    is_valid = True

    if number_str == '' or number_str[-1] == '.':
        is_valid = False

    for i in number_str:
        if not (i.isnumeric() or i == '.'):
            is_valid = False

    return is_valid


def get_value():
    is_number_valid = False

    while not is_number_valid:
        number_str = input('Digite um ângulo: ').replace(',', '.')
        is_number_valid = validate_number(number_str)

        if is_number_valid:
            converted_number = float(number_str)
            return converted_number
        else:
            print('Valor inválido, tente novamente.')


angle_value = get_value()
sin = sin(radians(angle_value))
cos = cos(radians(angle_value))
tan = tan(radians(angle_value))

print('O angulo de {}° tem o SENO de {:.2f}'.format(angle_value, sin))
print('O angulo de {}° tem o COSENO de {:.2f}'.format(angle_value, cos))
print('O angulo de {}° tem a TANGENTE de {:.2f}'.format(angle_value, tan))
