def get_number(index):
    message = ('primeiro', 'segundo')

    while True:
        user_number = input(f'Digite o {message[index]} valor: ').strip()
        
        if user_number.isnumeric():
            return int(user_number)
        else:
            print('Valor inválido. Tente novamente.')


def get_option():
    while True:
        user_option = input('Digite a sua opção: ').strip()

        if user_option.isnumeric() and (0 < int(user_option) < 6):
            return user_option
        else:
            print('Opção inválida, tenve novamente.')
            print()


print('-'*30)
print('{:^30}'.format('CALCULADORA'))
print('-'*30)
print()
print('''Este programa irá ralizar operações utilizando dois números.
Digite abaixo dois números inteiros positivos.''')
print()

number1 = get_number(0)
number2 = get_number(1)

while True:
    print()
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior número')
    print('[ 4 ] Utilizar novos números')
    print('[ 5 ] Sair do programa')
    print()
    
    option = get_option()
    if option == '1':
        print(f'A soma entre {number1} e {number2} é {number1 + number2}')
        print('-'*30)
    elif option == '2':
        print(f'O produto entre {number1} e {number2} é {number1 * number2}.')
    elif option == '3':
        if number1 == number2:
            print('Os dois números são iguais.')
        else:
            print(f'O maior número entre {number1} e {number2} é {max(number1, number2)}')
    elif option == '4':
        print()
        print('Insira os números novamente: ')
        number1 = get_number(0)
        number2 = get_number(1)   
    else:
        break

print('Finalizando...')
