from datetime import date


def validate_int_number(number_str):
    is_valid = True

    if not (number_str.isnumeric()):
        return False

    return is_valid


def get_number():
    while True:
        user_number = input('Que ano quer analisar? Digite 0 para analisar o ano atual: ')

        if validate_int_number(user_number):
            return int(user_number)
        else:
            print('Ano inválido.')


def check_is_bissextile(year):
    if (year % 4 == 0) and (not year % 100 == 0 or year % 400 == 0):
        return True
    else:
        return False


user_year = get_number()

if user_year == 0:
    user_year = date.today().year

is_bissextile = check_is_bissextile(user_year)

if is_bissextile:
    print(f'O ano {user_year} é BISSEXTO')
else:
    print(f'O ano {user_year} NÃO é BISSEXTO')
