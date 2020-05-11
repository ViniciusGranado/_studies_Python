from time import sleep

def get_number():
    while True:
        user_number_str = input('\nDigite um valor para ver a sua tabuada. Entre um número negativo para sair. ').strip()

        if user_number_str.isnumeric() or (user_number_str[1:].isnumeric and user_number_str[0] == '-'):
            return int(user_number_str)
        else:
            print('Valor inválido.')


# Header
print('-'*20)
print('{:^20}'.format('TABUADA'))
print('-'*20)
print('Este programa irá mostrar a tabuada dos numeros que você digitar. \nSe quiser sair, apenas entre com um número negativo.')

# Body
while True:
    number = get_number()
    
    if number < 0:
        break

    print('-'*40)
    for i in range(1, 11):
        print(f'{number:>3} X {i:>2} = {number*i}')
    print('-'*40)

print('ENCERRANDO...')
sleep(2)
