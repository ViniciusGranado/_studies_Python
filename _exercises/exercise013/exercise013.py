def validate_number(str_number):
    is_valid = True

    if str_number == '':
        is_valid = False
    else:
        for i in str_number:
            if i == str_number[0]:
                if not (i.isnumeric() or i == '.' or (i == '-')) or (str_number[-1] == '.'):
                    is_valid = False
            else:
                if not (i.isnumeric() or i == '.') or (str_number[-1]=='.'):
                    is_valid = False

    return is_valid

def get_values(index):
    is_valid = False
    message = ['Qual é o salário do funcionário? R$', 'Qual será a porcentagem do reajuste: %']

    while not (is_valid):
        number_str = input(message[index]).replace(',', '.')
        if number_str == '0':
            print("O valor não pode ser 0.")
        elif (index == 0 and number_str[0] == '-'):
            print('O salário não pode ser negativo.')
        else:
            is_valid = validate_number(number_str)

            if is_valid:
                converted_number = float(number_str)
                return converted_number
            else:
                print('Valor inválido, tente novamente.')


salary = get_values(0)
adjustment = get_values(1)
adjustment_amount = salary*adjustment/100
new_salary = salary + adjustment_amount


formatted_salary = str('%.2f' % salary)
formatted_adjustment_amount = str('%.2f' % abs(adjustment_amount))
formatted_new_salary = str('%.2f' % new_salary)

if adjustment_amount>0:
    mensagem = 'um aumento'
else:
    mensagem = 'uma redução'

print('\nSalário anterior: R${}'.format(formatted_salary))
print('Com {} de R${}, o novo salário será R${}'.format(mensagem, formatted_adjustment_amount, formatted_new_salary))


