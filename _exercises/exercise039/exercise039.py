from datetime import date


def get_number():
    while True:
        user_number = input('Ano de nascimento: ')

        if user_number.isnumeric():
            return int(user_number)
        else:
            print('Valor inválido.')


birth_year = get_number()
actual_year = date.today().year
user_age = actual_year - birth_year

print(f'Quem nasceu em {birth_year} tem {user_age} anos em {actual_year}')

if user_age < 18:
    print(f'Anda faltam {18-user_age} anos para o alistamento')
    print(f'Seu alistamento sera em {actual_year + (18-user_age)}')
elif user_age > 18:
    print(f'Você já deveria ter se alistado há {user_age-18} anos')
    print(f'Seu alistamento foi em {actual_year - (user_age - 18)}')
else:
    print('Você deve se alistar IMEDIATAMENTE!')




