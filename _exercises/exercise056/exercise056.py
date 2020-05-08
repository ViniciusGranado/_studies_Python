def get_number():
    while True:
        user_number = input('Idade: ')

        if user_number.isnumeric():
            return int(user_number)
        else:
            print('Valor inválido.')


def get_gender():
    while True:
        user_gender = input('Sexo [M/F]: ').upper()
        if user_gender == 'M' or user_gender == 'F':
            return user_gender
        else:
            print('Resposta inválida. Utiliza apenas as letras \'M\' ou \'F\'.')


age_sum = 0
oldest_man_name = ''
oldest_man_age = 0
women_under_20 = 0


for i in range(1, 5):
    print('{:-^22}'.format(f' {i}ª PESSOA '))
    name = input('Nome: ')
    age = get_number()
    gender = get_gender()
    print()

    age_sum += age

    if gender == 'M' and age > oldest_man_age:
        oldest_man_name = name
        oldest_man_age = age

    if gender == "F" and age < 20:
        women_under_20 += 1

age_mean = age_sum/4

print(f'A média de idade do grupo é de {age_mean} anos')
print(f'O homem mais velho tem {oldest_man_age} e se chama {oldest_man_name.capitalize()}')
print(f'Ao todo são {women_under_20} mulheres com menos de 20 anos.')
