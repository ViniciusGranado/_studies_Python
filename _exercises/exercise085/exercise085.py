def get_number(msg_index):
    message = ('primeiro', 'segundo', 'terceiro', 'quarto', 'quinto', 'sexto', 'sétimo')
    while True:
        user_number = input(f'Digite o {message[msg_index]} número: ').strip()

        if user_number.isnumeric():
            return int(user_number)
        else:
            print('Valor inválido.')


numbers_list = [[], []]
for i in range(0, 7):
    number = get_number(i)

    if number % 2 == 0:
        numbers_list[0].append(number)
    else:
        numbers_list[1].append(number)

numbers_list[0].sort()
numbers_list[1].sort()
print(f'Os valores pares digitados foram: {numbers_list[0]}')
print(f'Os valores ímpares digitados foram: {numbers_list[1]}')
