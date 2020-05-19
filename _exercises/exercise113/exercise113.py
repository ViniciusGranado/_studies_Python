def read_int(msg):
    while True:
        try:
            number = int(input(msg))
        except (ValueError, TypeError):
            print('[ERRO] Digite um número inteiro válido.')
            print()
        except KeyboardInterrupt:
            print('[ERRO] Entrada de dados interrompida.')
            print('Considerando valor 0')
            return 0
        else:
            return number


def read_float(msg):
    while True:
        try:
            number = float(input(msg).replace(',', '.'))
        except (ValueError, TypeError):
            print('[ERRO] Digite um número real válido.')
            print()
        except KeyboardInterrupt:
            print('[ERRO] Entrada de dados interrompida.')
            print('Considerando valor 0')
            return 0
        else:
            if number.is_integer():
                return int(number)

            return number


int_number = read_int('Digite um valor inteiro: ')
float_number = read_float('Digite um valor real: ')
print(f'Você digitou {int_number} e {float_number}')
