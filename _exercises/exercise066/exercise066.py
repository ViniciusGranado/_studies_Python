def get_number():
    while True:
        user_number_str = input('\nDigite um valor (999 para parar): ').strip()

        if user_number_str.isnumeric():
            return int(user_number_str)
        else:
            print('Valor inválido.')

        
# Header
print('-'*30)
print('{:^30}'.format('SOMANDO VALORES'))
print('-'*30)
print('Este programa irá somar os valores digitados. Quando desejar parar, apenas digite o número 999.')

total_numbers = sum_numbers = 0

while True:
    number = get_number()

    if number == 999:
        break

    total_numbers += 1
    sum_numbers += number


if total_numbers == 0:
    print('\nNenhum valor foi digitado.')
elif total_numbers == 1:
    print(f'\nApenas o valor {sum_numbers} foi digitado.')
else:
    print(f'\nA soma dos {total_numbers} valores digitados é {sum_numbers}')
