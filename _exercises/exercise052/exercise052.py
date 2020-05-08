def get_number():
    while True:
        user_number = input('Digite um número inteiro: ')

        if user_number.isnumeric():
            return int(user_number)
        else:
            print('Valor inválido.')


print('='*20)
print('{:^20}'.format('NÚMEROS PRIMOS'))
print('='*20)
number = get_number()
number_of_divisible = 0

for i in range(1, number+1):
    if number % i == 0:
        number_of_divisible += 1

if number_of_divisible > 2:
    print(f'\nO número {number} é divisível por {number_of_divisible} números, e portanto não é primo.')
else:
    print(f'\nO número {number} é divisível por {number_of_divisible} números, e portanto é primo.')
