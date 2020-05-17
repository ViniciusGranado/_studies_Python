def get_number():

    """
    Get a string by an user input, if the str is a
    valid number, return it in num type.

    :return: num. A number in num type.
    """
    
    while True:
        user_number_str = input('Número de Gols: ').strip()

        if user_number_str.isnumeric():
            return int(user_number_str)
        else:
            print('Valor inválido. Tente novamente.')


def record(player_name, goals=0):
    if player_name == '':
        player_name = '<desconhecido>'

    if goals == 0:
        return f'O jogador {player_name} não fez gols no campeonato.'
    elif goals == 1:
        return f'O jogador {player_name} fez 1 gol no campeonato.'
    else:
        return f'O jogador {player_name} fez {goals} gols no campeonato.'


player_name_input = input('Nome do jogador: ').strip().title()
goals_input = get_number()

print(record(player_name_input, goals_input))
