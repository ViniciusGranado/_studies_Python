def get_number():
    while True:
        user_number_str = input('Valor que deseja sacar R$').strip()

        if user_number_str.isnumeric():
            return int(user_number_str)
        else:
            print('Valor inválido, tente novamente.')


# Header
print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)

# Body
withdraw = get_number()

for i in range(0, 4):
    if i == 0:
        bill_value = 50
    elif i == 1:
        bill_value = 20
    elif i == 2:
        bill_value = 10
    else:
        bill_value = 1

    bills_amount = withdraw // bill_value
    rest = withdraw % bill_value

    if bills_amount != 0:
        print(f'Total de {bills_amount:.0f} cédulas de R${bill_value:.0f}')

    withdraw = rest

# Footer
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
