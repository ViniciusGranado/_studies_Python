def get_number(index):
    while True:

        if index == 0:
            number = input('Digite um número inteiro: ')

            if number.isnumeric():
                return int(number)
            else:
                print('Valor inválido.')

        else:
            number = input('Sua opção: ')

            if number.isnumeric() and 0 < int(number) < 4:
                return int(number)
            else:
                print('Opção inválida.')


def convert_number(number, convert_option):
    if convert_option == 1:
        return bin(number)
    elif convert_option == 2:
        return oct(number)
    else:
        return hex(number)


user_number = get_number(0)
print('Escolha uma das bases para conversão: ')
print('[ 1 ] Converter para BINÁRIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL')
user_option = get_number(1)

converted_number = convert_number(user_number, user_option)[2:]
message = ['BINÁRIO', 'OCTAL', 'HEXADECIMAL']

print(f'{user_number} convertido para {message[user_option-1]} é igual a {converted_number}.')
