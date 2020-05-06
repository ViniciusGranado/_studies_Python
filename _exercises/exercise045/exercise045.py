from random import randint
from time import sleep


def get_number():
    while True:
        user_number = input('Qual é a sua jogada? ')

        if user_number.isnumeric() and 0 < int(user_number) < 4:
            return int(user_number)
        else:
            print('Jogada inválida.')


def get_play(play):
    plays = ('PEDRA', 'PAPEL', 'TESOURA')
    return plays[play-1]


print('{:=^40}'.format(' PEDRA, PAPEL E TESOURA '))
print('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')

user_play = get_number()
computer_play = randint(1, 3)

user_play_message = get_play(user_play)
computer_play_message = get_play(computer_play)

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')

print('-='*15)
print(f'Jogador jogou {user_play_message}')
print(f'Computador jogou {computer_play_message}')
print('-='*15)

message = ('JOGADOR VENCE!', 'COMPUTADOR VENCE!')

if user_play == computer_play:
    print('EMPATE!')
elif user_play == 1:
    if computer_play == 2:
        print(message[1])
    else:
        print(message[0])
elif user_play == 2:
    if computer_play == 1:
        print(message[0])
    else:
        print(message[1])
elif user_play == 3:
    if computer_play == 1:
        print(message[1])
    else:
        print(message[0])
