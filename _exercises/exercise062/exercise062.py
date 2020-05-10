def get_number(index):
    message = ['Primeiro termo: ', 'Razão: ', '\nQuantos termos deseja mostrar a mais? Digite 0 para finalizar. ']
    while True:
        user_number = input(message[index]).strip()

        if user_number.isnumeric():
            return int(user_number)
        else:
            print('Valor inválido.')


print('-'*30)
print('{:^30}'.format('TERMOS DE UMA PA'))
print('-'*30)

first_term = get_number(0)
common_difference = get_number(1)

terms = first_term
i = 0

number_of_terms = 10
total_of_terms = 0

while not number_of_terms <= 0:

    for i in range (0, number_of_terms):
        print(terms, end='')
        if i != number_of_terms-1:
            print('\u279E', end=' ')
        terms += common_difference
        i += 1
        
    total_of_terms += number_of_terms
    number_of_terms = get_number(2)
    

print(f'\nProgressão finalizada com {total_of_terms} termos mostrados.')
    