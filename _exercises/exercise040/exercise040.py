def validate_float_number(number_str):
    is_valid = True

    if number_str == '' or number_str[-1] == '.':
        is_valid = False
    else:
        for i in number_str:
            if not (i.isnumeric() or i == '.'):
                is_valid = False
    if float(number_str) < 0 or float(number_str) > 10:
        is_valid = False

    return is_valid


def get_number(index):
    message = ['Primeira', 'Segunda']

    while True:
        user_number = input(f'{message[index]} nota: ').replace(',', '.')

        if validate_float_number(user_number):
            return float(user_number)
        else:
            print('Valor inválido.')


grade1 = get_number(0)
grade2 = get_number(1)
mean = (grade1 + grade2) / 2

formatted_grade1 = str('{:.1f}'.format(grade1)).replace('.', ',')
formatted_grade2 = str('{:.1f}'.format(grade2)).replace('.', ',')
formatted_mean = str('{:.1f}'.format(mean)).replace('.', ',')

print(f'\nCom as notas {formatted_grade1} e {formatted_grade2}, a média do aluno é {formatted_mean}')

if mean >= 7:
    print('O aluno está APROVADO')
elif mean >= 5:
    print('O aluno está de RECUPERAÇÃO')
else:
    print('O aluno está REPROVADO')
