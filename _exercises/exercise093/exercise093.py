def get_number():
    while True:
        user_number = input(f'Quantas partidas {player["name"].split()[0]} jogou? ').strip()

        if user_number.isnumeric():
            return int(user_number)
        else:
            print('Valor inválido.')


def print_table(dic):
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


player = dict()
player['name'] = input('Nome do jogador: ').strip().title()
number_matches = get_number()

points = list()
for i in range(0, number_matches):
    while True:
        number = input(' '*5 + f'Quantos gols {player["name"].split()[0]} fez na partida {i+1}? ').strip()

        if number.isnumeric():
            points.append(int(number))
            break
        else:
            print('Valor inválido.')

player['points'] = points[:]
player['total_points'] = sum(points)

print('-'*50)
print(player)

print('-'*50)
for k, v in player.items():
    print(f'O campo {k} tem o valor {v}')

print('-'*50)
print_table(player)
