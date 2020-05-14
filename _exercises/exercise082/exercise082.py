def get_number():
    while True:
        user_number = input('Digite um valor: ').replace(',', '.').strip()

        if user_number.isnumeric():
                return int(user_number)
        else:
            print('Valor inválido.')


def get_option():
    while True:
        user_option = input('Deseja inserir outro número? [S/N] ').strip().upper()

        if user_option == 'S' or user_option == 'N':
            return user_option
        else:
            print('Opção inválida.')


numbers_list = []
while True:
    numbers_list.append(get_number())

    if get_option() == 'N':
        break

even_list = []
odd_list = []

for i in numbers_list:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print(f'\nA lista completa de números é {numbers_list}')
print(f'A lista de números pares é {even_list}')
print(f'A listra de números ímpares é {odd_list}')
