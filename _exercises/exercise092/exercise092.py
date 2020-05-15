from datetime import date

def get_number(msg_index):
    message = ('Ano de nascimento: ', 'Número da carteira de trabalho: (0 se não possui) ', 'Ano de contratação: ')
    while True:
        user_number = input(message[msg_index]).strip()

        if user_number.isnumeric():
            return int(user_number)
        else:
            print('Valor inválido.')


def validate_float_number(number_str):
    is_valid = True

    if number_str == '' or number_str[-1] == '.':
        is_valid = False
    else:
        for i in number_str:
            if not (i.isnumeric() or i == '.'):
                is_valid = False

    return is_valid


def get_salary():
    while True:
        user_number = input('Salário: ').strip().replace(',', '.')

        if validate_float_number(user_number):
            if float(user_number).is_integer():
                return int(user_number)
            else:
                return float(user_number)
        else:
            print('Valor inválido.')


def print_table(dic):
    print('-'*50)
    print(f'Nome: {dic["name"]}')
    print(f'Idade: {dic["age"]}')
    print('Carteira de trabalho: ', end='')
    if dic['work card'] != 0:
        print(dic["work card"])
        print(f'Ano de contratação: {dic["hire year"]}')
        print(f'Salário: R${dic["salary"]:.2f}')
        print(f'{dic["name"].split()[0]} irá se aposentar com {dic["retirement"]} anos.')
    else:
        print('Não possui.')
    print('-'*50)


employee = dict()
employee['name'] = input('Nome: ').strip().title()
employee['age'] = date.today().year - (get_number(0))
employee['work card'] = get_number(1)

if employee['work card'] != 0:
    employee['hire year'] = get_number(2)
    employee['salary'] = get_salary()
    employee['retirement'] = (35 - (date.today().year - employee['hire year'])) + employee['age']

print_table(employee)
