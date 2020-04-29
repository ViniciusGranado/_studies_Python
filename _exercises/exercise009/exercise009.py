def get_and_validate_number():
    user_number_str = ''
    while not user_number_str.isnumeric():
        user_number_str = input('Digite um número para ver sua tabuada: ')

        if user_number_str.isnumeric():
            converted_user_number = int(user_number_str)
            show_table(converted_user_number)
        else:
            print('Número inválido, tente novamente.')
            get_and_validate_number()


def show_table(number):
    print('-'*12)

    for i in range (0, 11, 1):
        print('{} X {:2} = {}'.format(number, i, number*i))

    print('-'*12)


get_and_validate_number()