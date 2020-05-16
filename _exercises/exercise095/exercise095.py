def get_number():
    while True:
        user_number = input(f'Quantas partidas {new_player["name"].split()[0]} jogou? ').strip()

        if user_number.isnumeric():
            return int(user_number)
        else:
            print('Valor inválido.')


def get_option():
    while True:
        user_option = input('Deseja cadastrar outro jogador? [S/N] ').strip().upper()

        if user_option == 'S' or user_option == 'N':
            return user_option
        else:
            print('Opção inválida. Utilize apenas S ou N.')


def print_table(dic):
    print()
    print('-' * 60)
    print(f'O jogador {dic["name"].split()[0]} jogou {len(dic["points"])} partidas.')

    for index, value in enumerate(dic["points"]):
        if value == 0:
            print(' '*5, f'=> Na partida {index+1}, não marcou gols.')
        elif value == 1:
            print(' '*5, f'=> Na partida {index+1}, marcou 1 gol.')
        else:
            print(' '*5, f'=> Na partida {index+1}, marcou {value} gols.')

    if dic['total_points'] == 0:
        print('Não marcou gols em nenhuma partida.')
    elif dic['total_points'] == 1:
        print('Marcou 1 gol no total.')
    else:
        print(f'Marcou {dic["total_points"]} gols no total.')
    print('-' * 60)


# Register players on list
list_players = list()
while True:
    new_player = dict()
    new_player['name'] = input('Nome do jogador: ').strip().title()
    number_matches = get_number()

    points = list()
    for i in range(0, number_matches):
        while True:
            number = input(' '*5 + f'Quantos gols {new_player["name"].split()[0]} fez na partida {i+1}? ').strip()

            if number.isnumeric():
                points.append(int(number))
                break
            else:
                print('Valor inválido.')

    new_player['points'] = points[:]
    new_player['total_points'] = sum(points)

    list_players.append(new_player.copy())

    if get_option() == 'N':
        break

    print()

# Print players table
print(f'{"Noº":4}{"Nome":20}{"Gols":20}{"Total":5}')
print('-'*60)

for index, item in enumerate(list_players):
    print(f'{index:<4}{item["name"]:20}{str(item["points"]):20}{item["total_points"]}')

# Show individual player table
while True:
    print('\nDigite o número de um jogador para ver o seu aproveitamento detalhado. (999 para sair) ', end='')
    player_number = input().strip()

    if player_number.isnumeric():
        if int(player_number) == 999:
            break
        elif int(player_number) >= len(list_players):
            print('Número não encontrado, tente novamente.')
        else:
            print_table(list_players[int(player_number)])
    else:
        print('Valor inválido.')

print('Encerrando...')
