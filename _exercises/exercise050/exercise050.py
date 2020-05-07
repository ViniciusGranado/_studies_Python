def get_number(index):
    message = ('primeiro', 'segundo', 'terceiro', 'quarto', 'quinto', 'sexto')
    while True:
        user_number = input(f'Digite o {message[index]} número: ')

        if user_number.isnumeric():
            return int(user_number)
        else:
            print('Valor inválido.')


print('*'*26)
print('* SOMA DOS NÚMEROS PARES *')
print('*'*26)
print()
input('''Este programa irá mostrar a soma dos números pares
que você digitar. Aperte ENTER para começar.''')
print()

sum_even_numbers = 0
for i in range(0, 6):
    number = get_number(i)

    if number % 2 == 0:
        sum_even_numbers += number

print(f'\nA soma dos números pares digitados é {sum_even_numbers}.')
