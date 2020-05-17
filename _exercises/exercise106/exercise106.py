# Functions
def show_documentation(command):
    """
    -> Show the documentation of a given Python command.
    :param command: The command to show documentation.
    :return: The documentation of command.
    """
    print()
    formatted_print(f'Accessing documentation of comand \'{command}\'')
    print()
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

while True:
    formatted_print('HELP SYSTEM PyHELP')
    print('This program will help you get the documentation of a Python command '
          'of your choose. \nType the command you want help with bellow, or '
          'type \'end\' to exit.')

    user_input = input('\nFunction or Library: ').strip().lower()

    if user_input == 'end':
        break

    show_documentation(user_input)

print()
formatted_print('Finalizando...')
