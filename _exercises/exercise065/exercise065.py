def get_number():
    while True:
        user_number_str = input('Digite um número: ').strip()

        if user_number_str.isnumeric():
            return int(user_number_str)
        else:
            print('Valor inválido.')


def get_answer():
    while True:
        user_answer = input('Deseja continuar? [S/N] ').strip().upper()

        if user_answer in ('SN'):
            return user_answer
        else:
            print('Respota inválida.')
        
        
# Header
print('-'*30)
print('{:^30}'.format('MÉDIA DOS NÚMEROS'))
print('-'*30)
print('Este programa irá mostrar a média dos números digitados abaixo.')

# Body
sum_numbers = total_numbers = 0

while True:
    number = get_number()

    if total_numbers == 0: # Declare variables in the first iteration
        smaller_numbers = biggest_number = number
    else:
        if number < smaller_numbers:
            smaller_numbers = number
        if number > biggest_number:
            biggest_number = number

    sum_numbers += number
    total_numbers += 1

    answer = get_answer()

    if answer != 'S':
        break

mean_numbers = sum_numbers / total_numbers
formatted_mean_numbers = str('{:.1f}'.format(mean_numbers)).replace('.', ',')

print(f'\nVocê digitou {total_numbers} números e a média foi {formatted_mean_numbers}.')
print(f'O maior valor foi {biggest_number} e o menor foi {smaller_numbers}.')
