from datetime import date


def get_number():
    while True:
        user_number = input('Digite o seu ano de nascimento: ')

        if user_number.isnumeric():
            return int(user_number)
        else:
            print('Valor inválido.')


def get_category(year):
    age = date.today().year - year

    if age <= 9:
        category = 'MIRIM'
    elif age <= 14:
        category = 'INFANTIL'
    elif age <= 19:
        category = 'JÚNIOR'
    elif age <= 25:
        category = 'SÊNIOR'
    else:
        category = 'MASTER'

    return age, category


birth_year = get_number()
age_category = get_category(birth_year)

print(f'O atleta tem {age_category[0]} anos.')
print(f'Classificação: {age_category[1]}')
