# Functions
def vote(birth_year):

    """
    :param birth_year: int. The users birth year.
    :return: A string containing the age and wheter
             the vote is NOT ALLOWED, OPTIONAL or
             MANDATORY.
    """
    from datetime import date

    age = date.today().year - birth_year

    return_str = f'Com {age} anos: '
    if age < 16:
        return_str += 'VOTO NÃO PERMITIDO'
    elif age < 18 or age >= 70:
        return_str += 'VOTO OPCIONAL'
    else:
        return_str += 'VOTO OBRIGATÓRIO'

    return return_str


def get_birth_year():

    """
    Get a number string by an user input, if the str is a
    valid int number, return it in number format.

    :return: num. A number in number format.
    """

    while True:
        user_number_str = input('Ano de nascimento: ').strip()

        if user_number_str.isnumeric():
            return int(user_number_str)
        else:
            print('Valor inválido.')


# Main program
users_birth_year = get_birth_year()
print(vote(users_birth_year))
