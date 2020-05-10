def get_number(index):
    message = ['Primeiro termo: ', 'Razão: ']
    while True:
        user_number = input(message[index])

        if user_number.isnumeric():
            return int(user_number)
        else:
            print('Valor inválido.')


print('-'*30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('-'*30)

first_term = get_number(0)
common_difference = get_number(1)

terms = first_term
i = 0

while i < 10:
    print(terms, end='')
    if i != 9:
        print('\u279E', end=' ')
    terms += common_difference
    i += 1
