def validate_float_number(number_str):
    is_valid = True

    if number_str == '' or number_str[-1] == '.':
        is_valid = False
    else:
        for i in number_str:
            if not (i.isnumeric() or i == '.'):
                is_valid = False

    return is_valid


def get_number():
    while True:
        user_number_str = input('Preço: R$').strip().replace(',', '.')

        if validate_float_number(user_number_str):
            return float(user_number_str)
        else:
            print('Valor inválido.')

    
def get_option():
    while True:
        user_option = input('Deseja continuar? [S/N] ').strip().upper()

        if user_option == 'S' or user_option == 'N':
            return user_option
        else:
            print('Opção inválida.')


# Header
print('-'*40)
print('{:^40}'.format('LOJA SUPER BARATÃO'))
print('-'*40)

# Body
sum_prices = products_over_1000 = 0

while True:
    product = input('Nome do produto: ').strip().capitalize()
    product_price = get_number()
    wants_to_continue = get_option()

    if sum_prices == 0 or product_price < cheapest_product_price:
        cheapest_product = product
        cheapest_product_price = product_price

    sum_prices += product_price

    if product_price > 1000:
        products_over_1000 += 1

    if wants_to_continue == 'N':  
        break

    print('-'*25)

formatted_sum_prices = str(f'{sum_prices:.2f}').replace('.', ',')
formatted_cheapest_price = str(f'{cheapest_product_price:.2f}').replace('.', ',')

print('{:-^40}'.format('FIM DA COMPRA'))
print(f'O total da compra foi de R${formatted_sum_prices}')

if products_over_1000 == 0:
    print('Não foram comprados produtos com valor superior à R$1000,00')
elif products_over_1000 == 1:
    print('Foi comprado 1 produto com valor superior à R$1000,00')
else:
    print(f'Foram comprados {products_over_1000} produtos com valor superior à R$1000,00')

print(f'O produto mais barato foi {cheapest_product} que custou R${formatted_cheapest_price}')
