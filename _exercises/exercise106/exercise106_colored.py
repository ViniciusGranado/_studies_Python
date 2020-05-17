# Functions
def show_documentation(command):
    """
    -> Show the documentation of a given Python command.
    :param command: The command to show documentation.
    :return: The documentation of command.
    """
    print('\n', end='\033[30;44m')
    formatted_print(f'Accessing documentation of comand \'{command}\'')
    print('\033[m')
    print('\033[7;30m')
    return help(command)


def formatted_print(message):
    """
    -> Print a formatted str, with lines above and bellow text,
       with dynamic size.
    :param message: The message to be formatted.
    :return: The formatted message.
    """
    message = '  ' + message + '  '
    print('-'*len(message))
    print(message)
    print('-'*len(message))


# Main program
print('[! This colored version doesn\'t work with windows shell.'
      '\nIf you\'re using windows, please use the regular version. !]')

while True:
    print('\033[m')
    print('\033[42;30m', end='')
    formatted_print('HELP SYSTEM PyHELP')
    print('This program will help you get the documentation of a Python command '
          'of your choose. \nType the command you want help with bellow, or '
          'type \'end\' to exit.')
    print('\033[0m')

    user_input = input('Function or Library: ').strip().lower()

    if user_input == 'end':
        break

    show_documentation(user_input)

print()
print('\033[30;41m', end='')
formatted_print('Finalizando...')
print('\033[m')
