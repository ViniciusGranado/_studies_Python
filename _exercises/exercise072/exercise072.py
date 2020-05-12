def get_number():
    while True:
        user_number_str = input('Digite um número entre 0 e 20: ').strip()

        if user_number_str.isnumeric() and 0 < int(user_number_str) < 21:
            return int(user_number_str)
        else:
            print('Número inválido.', end=' ')


def get_option():
    while True:
        user_answer = input('\nDeseja digitar outro número? [S/N] ').strip().upper()

        if user_answer == 'S' or user_answer == 'N':
            return user_answer
        else:
            print('Opção inválida.', end=' ')


control = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',
           'dezesseis','dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    number = get_number()
    print(f'\nVocê digitou o número {control[number]}.')
    wish_to_continue = get_option()

    if wish_to_continue == 'N':
        break

print('Encerrando...')
