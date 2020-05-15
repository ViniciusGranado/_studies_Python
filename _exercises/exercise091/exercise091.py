from random import randint

players = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}

print('Valores sorteados:')
for k, v in players.items():
    print(f'{k} tirou {v} no dado.')
print('-'*40)
print()

sorted_players = sorted(players.items(), key=lambda x: x[1], reverse=True)
print(f"{'== RANKING DOS JOGADORES == '}")

for index, item in enumerate(sorted_players):
    print(f'{index+1}º Lugar: {item[0]} com {item[1]}')
