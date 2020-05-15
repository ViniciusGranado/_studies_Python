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
        user_number = input(f'Média de {student["name"]}: ').replace(',', '.')

        if validate_float_number(user_number) and 0 <= float(user_number) <= 10:
            if float(user_number).is_integer():
                return int(user_number)
            else:
                return float(user_number)
        else:
            print('Valor inválido.')


student = {
    'name': input('Nome: ').strip().title(),
    'mean': get_number()
}

if student['mean'] >= 7:
    student['situation'] = 'Aprovado'
elif student['mean'] >= 5:
    student['situation'] = 'Recuperação'
else:
    student['situation'] = 'Reprovado'

print('-='*20)

print(f'- Nome do aluno: {student["name"]}')
print(f'- Média do aluno: {student["mean"]}')
print(f'- Situação do aluno: {student["situation"]}')
