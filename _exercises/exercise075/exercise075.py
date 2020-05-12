def get_number(msg_index):
    message = ('primeiro', 'segundo', 'terceiro', 'quarto')
    while True:
        user_number_str = input(f'Digite o {message[msg_index]} número: ').strip()

        if user_number_str.isnumeric():
            return int(user_number_str)
        else:
            print('Valor inválido, tente novamente.')


numbers = (get_number(0), get_number(1), get_number(2), get_number(3))

print('\nVocê digitou os valores: ', end='')
for index, item in enumerate(numbers):
    if index == len(numbers)-1:
        print(item)
    else:
        print(item, end=', ')

if numbers.count(9) == 0:
    print('O valor 9 não aparece nenhuma vez.')
elif numbers.count(9) == 1:
    print('O valor 9 aparece 1 vez.')
else:
    print(f'O valor 9 aparece {numbers.count(9)} vezes.')

if not 3 in numbers:
    print('O valor 3 não aparece nenhuma vez.')
else:
    print(f'O valor 3 aparece pela primeira vez na {numbers.index(3)+1}ª posição.')

even_numbers = []
for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)

if even_numbers == []:
    print('Não houve valores pares digitados.')
else:
    print('Os valores pares digitados foram: ', end='')
    for index, item in enumerate(even_numbers):
        if index == len(even_numbers)-1:
            print(item)
        else:
            print(item, end=', ')
