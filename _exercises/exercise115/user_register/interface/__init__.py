# This module has functions that create the program interface.


def header(msg):
    """
    -> Creates a simple formatted message, with lines above and bellow it.
    :param msg: Type: str. The message to be formatted.
    :return: None.
    """
    print('-'*45)
    print(f'{msg:^45}')
    print('-'*45)


def print_main_menu():
    """
    -> Prints the program main menu.
    :return: None
    """
    header('MENU PRINCIPAL')
    print('1 - Exibir usuários cadastrados')
    print('2 - Cadastrar novo usuário')
    print('3 - Sair do sistema')
    print('-'*45)


def show_users_table(file):
    """
    -> Print the users table, using the data from the 'users' file.
    :param file: Type: <class '_io.TextIOWrapper'>
    :return: None
    """
    file.readline()
    file_list = file.readlines()

    if len(file_list) == 0:
        print('\nNão há usuários cadastrados no momento.\n')
    else:
        print()
        header('USUÁRIOS CADASTRADOS')
        for line in file_list:
            comma = line.index(',')
            print(f"{line[0:comma]:35}", end=' ')
            age_data = str(line[comma+1:]).replace('\n', '')
            print(f"{age_data:>3} anos")

        print()

    file.close()
