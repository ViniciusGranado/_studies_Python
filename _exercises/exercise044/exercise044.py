def validate_float_number(number_str):
    is_valid = True

    if number_str == '' or number_str[-1] == '.':
        is_valid = False
    else:
        for i in number_str:
            if not (i.isnumeric() or i == '.'):
                is_valid = False

    return is_valid


def get_number(index):
    message = ['Preço das compras: R$', 'Selecione uma opção: ', 'Número de parcelas: ']
    while True:
        user_number = input(message[index]).replace(',', '.')

        if index == 0:
            if validate_float_number(user_number):
                return float(user_number)
            else:
                print('Valor inválido.')
        elif index == 1:
            if user_number.isnumeric() and 0 < int(user_number) < 5:
                return int(user_number)
            else:
                print('Opção inválida')
        else:
            if user_number.isnumeric():
                return int(user_number)
            else:
                print('Número de parcelas inválido.')


print('{:=^40}'.format(' LOJAS GUANABARA '))
product_price = get_number(0)

print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista no dinheiro')
print('[ 2 ] à vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')

pay_method = get_number(1)
formatted_price = str('{:.2f}'.format(product_price)).replace('.', ',')

if pay_method == 1:
    formatted_price_discount = str('{:.2f}'.format(product_price - (product_price*10/100))).replace('.', ',')

    print(f'Sua compra de R${formatted_price} irá custar R${formatted_price_discount} com 10% de desconto.')
elif pay_method == 2:
    formatted_price_discount = str('{:.2f}'.format(product_price - (product_price*5/100))).replace('.', ',')

    print(f'Sua compra de R${formatted_price} irá custar R${formatted_price_discount} com 5% de desconto.')
elif pay_method == 3:
    formatted_installments = str('{:.2f}'.format(product_price/2)).replace('.', ',')

    print(f'Sua compra de R${formatted_price} será parcelada em 2 vezes de R${formatted_installments} sem juros')
else:
    installments_number = get_number(2)
    formatted_installments = str('{:.2f}'.format((product_price + (product_price*20/100)) / installments_number)).replace('.', ',')
    formatted_price_final = str('{:.2f}'.format(product_price + (product_price*20/100))).replace('.', ',')

    print(f'Sua compra será parcelada em {installments_number} vezes de R${formatted_installments} COM JUROS')
    print(f'Sua compra de R${formatted_price} irá custar RS{formatted_price_final} no final.')
