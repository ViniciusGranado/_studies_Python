def validate_number(str_number):
    is_valid = True

    if not (str_number.isnumeric()) or int(str_number) < 0:
        is_valid = False

    return is_valid


def get_number():
    is_number_valid = False

    while not is_number_valid:
        velocity_str = input('Qual é a velocidade atual do carro em Km/h? ')
        is_number_valid = validate_number(velocity_str)

        if is_number_valid:
            return int(velocity_str)
        else:
            print('Velocidade inválida.')


velocity = get_number()

if velocity > 80:
    ticket = ('%.2f' % ((velocity-80) * 7))
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print(f'Você deve pagar uma multa de R${ticket.replace(".", ",")}!')

print('Tenha um bom dia! Dirija com segurança!')
