def get_number():
    while True:
        user_number_str = input('\nQuantos termos deseja mostrar? ').strip()

        if user_number_str.isnumeric():
            return int(user_number_str)
        else:
            print('Valor inválido.')


# Header
print('-'*26)
print('{:^20}'.format('| SEQUENCIA DE FIBONACCI |'))
print('-'*26)
print('Este programa irá mostrar o número de termos desejados da Sequencia de Fibonacci.')

number_of_terms = get_number()

number1 = 0
number2 = 1
print(f'{number1} \u279E {number2}', end=' \u279E ')

for i in range(2, number_of_terms):
    current_number = number1 + number2     

    if i != number_of_terms-1:
        print(current_number, end=' \u279E ')
    else:
        print(current_number)
        
    number1 = number2
    number2 = current_number
 