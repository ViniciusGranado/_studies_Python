def validate_float_number(number_str):
    """
    -> Check if a given string is a valid positive number(float or int).
    :param number_str: Str. String to be validated.
    :return: Bool. True if str is a valid number, else, False
    """
    # Check if str is empty or last char is '.'
    if number_str == '' or number_str[-1] == '.':
        return False
    else:
        # Check if all char are numeric or '.'
        for i in number_str:
            if not (i.isnumeric() or i == '.'):
                return False

    return True


def get_number():
    """
    -> Ask a number input for the user, if the input is valid, return
       as 'num' type. PS: Input and print values need to be adapted
       according to the needs of the program.
    :return: Num. Input converted as 'num' type
    """
    while True:
        user_number_str = input('Digite um valor: R$').strip().replace(',', '.')

        if validate_float_number(user_number_str):
            if float(user_number_str).is_integer():
                return int(user_number_str)
            else:
                return float(user_number_str)
        else:
            print('Valor inválido.')
