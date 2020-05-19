# This module has functions that manipulate the program data.
from user_register.interface import header


def get_menu_option():
    """
    -> Get the user's option from the main menu. Validate input type and number range.
    :return: Type: int. The user's option.
    """
    while True:
        try:
            option = int(input('Sua opção: '))
        except ValueError:
            print('Valor inválido, tente novamente.')
        else:
            if not 1 <= option <= 3:
                print('Opção inválida. Utilize apenas 1, 2 ou 3.')
            else:
                return option


def open_users_file(mode):
    """
    -> Open CSV file, with the desired mode.
    :param mode: Type: str. Indicates the mode to open the file.
    :return: Type: <class '_io.TextIOWrapper'>. The file opened by the function.
    """
    users_file = open('users.csv', mode)
    return users_file


def get_new_user_data():
    """
    -> Ask the user the data to register on system. Uses function get_user_age() to
       validate age data.
    :return: Type: list of str. A list containing new user's name and age.
    """

    header('NOVO USUÁRIO')

    while True:
        new_user_name = input('Nome: ').strip().title()
        if new_user_name == '':
            print('Você deve digitar um nome válido.\n')
        else:
            break

    new_user_age = get_user_age()

    return [new_user_name, new_user_age]


def get_user_age():
    """
    -> Ask and validate new user's age.
    :return: Type: int. New user's age.
    """
    while True:
        try:
            age = int(input('Idade: '))
        except ValueError:
            print('Idade inválida, tente novamente.\n')
        else:
            if age >= 0:
                return age
            else:
                print(f'Valor negativo. Considerando idade {abs(age)}.')
                return abs(age)


def append_data_users_file(file, data):
    """
    -> Register new user's data on CSV file.
    :param file: Type: <class '_io.TextIOWrapper'>. The CSV file.
    :param data: Type: list of str. The data to be registered on file.
    :return:
    """
    try:
        file.write(f'{data[0]},{data[1]}\n')
    except:
        print('[Erro] Usuário não cadastrado, tente novamente.')
    else:
        print(f'\nCadastro de {data[0]} realizado com sucesso.')
        file.close()


def check_user_files():
    """
    Check if CSV file does exist. If not, create one.
    :return: None
    """
    try:
        test_file = open('users.csv', 'r')
    except FileNotFoundError:
        test_file = open('users.csv', 'w+')
        test_file.write('user_name,user_age\n')
    finally:
        test_file.close()
