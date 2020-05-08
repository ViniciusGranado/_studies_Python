from datetime import date


def get_number(index):
    while True:
        user_number = input(f'Em que ano nasceu a {index}ª pessoa? ')

        if user_number.isnumeric():
            return int(user_number)
        else:
            print('Valor inválido.')


minors = 0
majors = 0
for i in range(1, 8):
    birth_year = get_number(i)

    if date.today().year-birth_year >= 18:
        majors += 1
    else:
        minors += 1

print(f'\nAo todo temos {minors} pessoas menores de idade e {majors} pessoas maiores de idade.')
