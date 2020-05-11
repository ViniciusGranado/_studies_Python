from random import randint

def get_number():
    while True:
        user_number_str = input('\nDigite um valor: ').strip()

        if user_number_str.isnumeric() and 0 <= int(user_number_str) <= 10:
            return int(user_number_str)
        else:
            print('Número inválido. Tente novamente')


def get_game_option():
    while True:
        user_option = input('\nPar ou Ímpar? [P/I] ').strip().upper()

        if user_option == 'P' or user_option == 'I':
            return user_option
        else:
            print('Opção inválida. Digite apenas \'P\' ou \'I\'. ')


# Header
print('-'*60)
print('{:^60}'.format('PAR OU ÍMPAR'))
print('-'*60)
print('Vamos jogar Par ou Ímpar. Digite um número entre 0 e 10 e \nescolha se quer jogar com \'Par\' ou \'Ímpar\'. BOA SORTE!')

# Body
total_wins = 0

while True:
    computer_number = randint(0, 10)
    game_option = get_game_option()
    user_number = get_number()

    is_game_even = (computer_number + user_number) % 2 == 0

    if is_game_even:
        result = "PAR"
    else:
        result = 'ÍMPAR'

    print('\n' + '-'*60)
    print(f'Você jogou {user_number} e o computador {computer_number}. Total de {user_number + computer_number}.')
    print(f'DEU {result}')
    print('-'*60)

    if (game_option == 'P' and is_game_even) or (game_option == 'I' and not is_game_even):
        print('Você GANHOU!')
        print('Vamos jogar novamente...')
        total_wins += 1
        print('-'*60)
    else:
        print('Você PERDEU!')
        print('-'*60)
        break

# Final result

if total_wins == 0:
    print('GAME OVER! Você não venceu nenhuma vez.')
elif total_wins == 1:
    print(f'GAME OVER! Você venceu apenas uma vez.') 
else:
    print(f'GAME OVER! Você venceu {total_wins} vezes.')
