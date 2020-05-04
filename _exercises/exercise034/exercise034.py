def validate_number(number_str):
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
        user_number = input('Qual é o salário do funcionário? R$').replace(',', '.')

        if validate_number(user_number):
            return float(user_number)
        else:
            print('Valor inválido.')


salary = get_number()

if salary > 1250:
    adjustment = 10
else:
    adjustment = 15

new_salary = salary + (salary*adjustment/100)

formatted_salary = str("{:.2f}".format(salary)).replace('.', ',')
formatted_new_salary = str("{:.2f}".format(new_salary)).replace('.', ',')

print(f"Salário anterior: R${formatted_salary}")
print(f"O novo salário será: R${formatted_new_salary}")