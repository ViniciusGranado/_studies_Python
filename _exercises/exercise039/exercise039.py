from datetime import date


def get_number(index):
    message = ['Opção: ', 'Ano de nascimento: ']
    while True:
        user_number = input(message[index])

        if index == 0:
            if user_number.isnumeric() and (0 < int(user_number) < 3):
                return int(user_number)
            else:
                print('Valor inválido.')
        else:
            if user_number.isnumeric():
                return int(user_number)
            else:
                print('Valor inválido.')


print('Qual é o seu sexo: ')
print('-------------------')
print('[ 1 ] Masculino')
print('[ 2 ] Feminino')
gender = get_number(0)

if gender == 2:
    print('\nO serviço militar é obrigatório apenas para cidadãos do sexo masculino.')
    print('Caso deseje realizar o serviço militar voluntário, entre em contato com a Junta Militar mais próxima.')
else:
    birth_year = get_number(1)
    actual_year = date.today().year
    user_age = actual_year - birth_year

    print(f'\nQuem nasceu em {birth_year} tem {user_age} anos em {actual_year}')

    if user_age < 18:
        print(f'Anda faltam {18-user_age} anos para o alistamento')
        print(f'Seu alistamento sera em {actual_year + (18-user_age)}')
    elif user_age > 18:
        print(f'Você já deveria ter se alistado há {user_age-18} anos')
        print(f'Seu alistamento foi em {actual_year - (user_age - 18)}')
    else:
        print('Você deve se alistar IMEDIATAMENTE!')
