# Functions
def read_int(msg):
    """
    -> Get an input by the user, if input is a valid positive number,
       return it as int type, else, ask for another input.
    :param msg: The message that will be displayed to the user.
    :return: The number typed by the user in int type.
    """
    while True:
        user_number_str = input(msg)

        if user_number_str.isnumeric():
            return int(user_number_str)
        else:
            print('Valor inválido. Deve ser um número inteiro positivo.') 


# Main program
number = read_int('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {number}.')
