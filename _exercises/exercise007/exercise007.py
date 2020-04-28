def get_numbers():
    number1_str = ''
    number2_str = ''

    while not number1_str.isnumeric():
        number1_str = input('Digite o primeiro número: ')

        if number1_str.isnumeric():
            number1_converted = int(number1_str)
            break
        else:
            print('Número inválido. Tente novamente.')

    while not number2_str.isnumeric():
        number2_str = input('Digite o segundo número: ')

        if number2_str.isnumeric():
            number2_converted = int(number2_str)
            break
        else:
            print('Número inválido, tente novamente.')

    show_arithmetic_mean(number1_converted, number2_converted)


def show_arithmetic_mean(number1, number2):
    print('A média aritmética de {} e {} é {}.'.format(number1, number2, (number1+number2)/2))


get_numbers()
