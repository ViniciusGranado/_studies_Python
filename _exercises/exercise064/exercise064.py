def get_number():
    while True:
        user_number_str = input('Digite um número [999 para parar]: ').strip()

        if user_number_str.isnumeric():
            return int(user_number_str)
        else:
            print('Valor inválido')


# Header
print('*'*20)
print('{:^20}'.format('SOMANDO NÚMEROS'))
print('*'*20)
print('Este programa irá mostrar a soma dos números que você digitar.')

#Body

sum_numbers = total_numbers = 0
while True:
    number = get_number()

    if number == 999:
        break
    
    total_numbers += 1
    sum_numbers += number

print(f'Você digitou {total_numbers} números e a soma entre eles foi {sum_numbers}.')
    