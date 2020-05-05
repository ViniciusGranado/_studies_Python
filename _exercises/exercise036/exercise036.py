def validate_float_number(number_str):
    is_valid = True

    if number_str == '' or number_str[-1] == '.':
        is_valid = False
    else:
        for i in number_str:
            if not (i.isnumeric() or i == '.'):
                is_valid = False

    return is_valid


def validate_int_number(number_str):
    return number_str.isnumeric()


def get_number(i):

    mensagem = ['Valor da casa: R$', 'Salário do comprador: R$', 'Quantos anos de financiamento: ']
    while True:
        user_number = input(mensagem[i]).replace(',', '.')

        if i == 2:
            if validate_int_number(user_number):
                return int(user_number)
            else:
                print('Valor inválido.')
        else:
            if validate_float_number(user_number):
                return float(user_number)
            else:
                print('Valor inválido.')


house_value = get_number(0)
user_salary = get_number(1)
years = get_number(2)

installments = years * 12
installments_value = house_value/installments

formatted_house_value = str('{:.2f}'.format(house_value)).replace('.', ',')
formatted_installments_value = str('{:.2f}'.format(installments_value)).replace('.' , ',')

print(f'Para pagar uma casa de R${formatted_house_value} em {years} anos, a prestação será de R${formatted_installments_value}')

if (installments_value) >= (user_salary*30/100):
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')