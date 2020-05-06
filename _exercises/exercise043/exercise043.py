def validate_float_number(number_str):
    is_valid = True

    if number_str == '' or number_str[-1] == '.':
        is_valid = False
    else:
        for i in number_str:
            if not (i.isnumeric() or i == '.'):
                is_valid = False

    return is_valid


def get_number(index):
    message = ['Qual é o seu peso? (Kg) ', 'Qual é a sua altura? (m) ']
    while True:
        user_number = input(message[index]).replace(',', '.')

        if validate_float_number(user_number):
            return float(user_number)
        else:
            print('Valor inválido.')


def get_imc(weight, height):
    return weight / (height**2)


def get_message(imc):
    if imc < 18.5:
        message = 'Você está ABAIXO DO PESO ideal'
    elif imc <= 25:
        message = 'Parabéns, você está na faixa de PESO IDEAL'
    elif imc <= 30:
        message = 'Você está na faixa de SOBREPESO'
    elif imc <= 40:
        message = 'Você está na faixa de OBESIDADE'
    else:
        message = 'Você está na faixa de OBESIDADE MÓRBIDA, cuidado!'

    return message


user_weight = get_number(0)
user_height = get_number(1)
user_imc = get_imc(user_weight, user_height)

formatted_imc = str('{:.1f}'.format(user_imc)).replace('.', ',')
print_message = get_message(user_imc)

print(f'O IMC dessa pessoa é de {formatted_imc}')
print(print_message)
