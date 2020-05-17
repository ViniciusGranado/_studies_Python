# Functions
def get_number():

    """
    Get a string by an user input, if the str is a
    valid number, return it in num type.

    :return: num. An int number in num type.
    """

    while True:
        user_number_str = input('Digite um número para saber o seu fatorial: ').strip()

        if user_number_str.isnumeric():
            return int(user_number_str)
        else:
            print('Valor inválido.')


def factorial(num, show=False):
    """
    -> Calculate the factorial of a given number, and can show the calculus process.
    :param num: The number to calculate the factorial
    :param show: Determine whether or not the calculus
                 process will be shown. Default = False
    :return: The factorial of 'num', and the calculus process (if show is True)
    """

    fact = 1
    calculus = ''

    for i in range(num, 0, -1):
        fact *= i

        if show:
            if i == 1:
                calculus += f'{i} = '
            else:
                calculus += f'{i} x '

    calculus += f'{fact}'
    return calculus


# Main program
user_number = get_number()
print('-'*20)
print(factorial(user_number))
