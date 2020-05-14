from random import randint

def get_number():
    while True:
        user_number = input('Quantos jogos serão gerados? ').strip()

        if user_number.isnumeric():
            return int(user_number)
        else:
            print('Valor inválido.')


print('-'*40)
print('{:^40}'.format('GERADOR DE JOGOS DA MEGA SENA'))
print('-'*40)
number_of_games = get_number()
games = []

for i in range(0, number_of_games):
    games.append([])

    for i2 in range(0, 6):
        while True:
            random_number = randint(1, 60)
            if random_number not in games[i]:
                games[i].append(random_number)
                break

    games[i].sort()

print('{:-^40}'.format(f'Sorteando {number_of_games} JOGOS'))

for index, item in enumerate(games):
    print(F'Jogo {index+1}: {item}')

print('{:-^40}'.format('< BOA SORTE! >'))
