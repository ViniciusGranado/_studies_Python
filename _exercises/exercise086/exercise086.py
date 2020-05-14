def get_number():
    while True:
        user_number = input().replace(',', '.')

        if user_number.isnumeric():
            return int(user_number)
        else:
            print('Valor inválido.')


matrix = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'Digite o valor da posição [{l}, {c}]: ', end='')
        number = get_number()
        matrix[l].append(number)

print('\n' + '-'*25)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end=' ')
    print()
print('-'*25)
