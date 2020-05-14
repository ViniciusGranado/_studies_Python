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

sum_third_column = even_sum = 0
biggest_value_second_line = matrix[1][0]

print('\n' + '-'*25)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end=' ')

        if matrix[l][c] % 2 == 0:  # Check even numbers
            even_sum += matrix[l][c]

        if c == 2:  # Get sum of third column
            sum_third_column += matrix[l][2]

        if l == 1:  # Get biggest value on second line
            if matrix[1][c] > biggest_value_second_line:
                biggest_value_second_line = matrix[1][c]
    print()

print('-'*25)

print(f'\nA soma de todos os valores pares digitados é {even_sum}')
print(f'A soma dos valores da terceira coluna é {sum_third_column}')
print(f'O maior valor da segunda linha é {biggest_value_second_line}')
