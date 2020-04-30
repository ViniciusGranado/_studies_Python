def validate_value(number_str):
    number_is_valid = True

    if number_str=='':
        number_is_valid = False
    else:
        for i in number_str:
            if not (i.isnumeric() or i=='.') or (number_str[-1]=='.'):
                number_is_valid = False

    return number_is_valid


def get_values(i):
    is_valid = False
    message = ['Qual é o valor do produto? R$', 'Qual a porcentagem de desconto? %']
    while not is_valid:
        number_str = input(message[i]).replace(',', '.')
        is_valid = validate_value(number_str)

        if is_valid:
            converted_number = float(number_str)
            return converted_number
        else:
            print('Número inválido, tente novamente.')


product_value = get_values(0)
discount = get_values(1)
final_value = (product_value) - (product_value*discount/100)

formatted_product_value = str("%.2f" % product_value).replace('.', ',')
formatted_final_value = str("%.2f" % final_value).replace('.', ',')

print('\nO produto que custava R${}, na promoção com desconto de {}% irá custar RS{}'.format(formatted_product_value, discount, formatted_final_value))