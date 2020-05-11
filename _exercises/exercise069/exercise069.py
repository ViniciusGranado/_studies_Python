def get_age():
    while True:
        user_number_str = input('Idade: ').strip()

        if user_number_str.isnumeric():
            return int(user_number_str)
        else:
            print('Número inválido. Tente novamente')

def get_gender():
    while True:
        user_gender = input('Sexo: [M/F] ').strip().upper()

        if user_gender == 'M' or user_gender == 'F':
            return user_gender
        else:
            print('Opção inválida. Utilize apenas \'M\' ou \'F\'. ')


def get_option():
    while True:
        user_option = input('Deseja continuar? [S/N] ').strip().upper()

        if user_option == 'S' or user_option == 'N':
            return user_option
        else:
            print('Opção inválida.')

total_over_18 = total_men = women_over_20 = 0

while True:
    print('\n' + '-'*40)
    print('{:^40}'.format('CADASTRE UMA PESSOA'))
    print('-'*40)

    age = get_age()
    gender = get_gender()

    if age >= 18:
        total_over_18 += 1
    if gender == 'M':
        total_men += 1
    if age >= 20 and gender == 'F':
        women_over_20 += 1

    print('-'*40)
    option = get_option()

    if option == 'N':
        break

print()

if total_over_18 == 0:
    print('Não há pessoas maiores de idade cadastradas.')
elif total_over_18 == 1:
    print('Há 1 pessoa maior de idade cadastrada.')
else:
    print(f'Há {total_over_18} pessoas maiores de idade cadastradas.')

if total_men == 0:
    print('Não há pessoas cadastradas do sexo masculino.')
elif total_men == 1:
    print('Há 1 pessoa cadastrada do sexo masculino.')
else:
    print(f'Há {total_men} pessoas cadastradas do sexo masculino.')

if women_over_20 == 0:
    print('Não há mulheres com mais de 20 anos cadastradas.')
elif women_over_20 == 1:
    print('Há 1 mulher com mais de 20 anos cadastrada.')
else:
    print(f'Há {women_over_20} mulheres com mais de 20 anos cadastradas.')
