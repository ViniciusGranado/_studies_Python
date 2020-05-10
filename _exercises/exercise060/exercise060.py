def get_factorial(number):
    if number == 0:
        return 1
    else:
        return number * get_factorial(number-1)


def get_number():
    while True:
        user_number_str = input('Digite um número inteiro para calcular o seu fatorial: ').strip()

        if user_number_str.isnumeric():
            return int(user_number_str)
        else:
            print('Valor inválido.')
            print()


# Header
print('-'*30)
print('{:^30}'.format('FATORIAL'))
print('-'*30)
print()

# Body

user_number = get_number()
number_factorial = get_factorial(user_number)

print(f'\nO fatorial de {user_number} é {number_factorial}.')
