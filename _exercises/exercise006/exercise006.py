def show_number_info():
    number = input('Digíte um número: ')
    if number.isnumeric():
        number_converted = int(number)
        print('O dobro de {} é {}.'.format(number_converted, number_converted*2))
        print('O triplo de {} é {}.'.format(number_converted, number_converted*3))
        print('A raiz quadrada de {} é {}'.format(number_converted, number_converted**(1/2)))
    else:
        print('Número inválido, tente novamente.')
        show_number_info()


show_number_info()
