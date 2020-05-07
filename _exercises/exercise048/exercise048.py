print('-'*44)
print('{:^44}'.format(' MÚLTIPLOS DE 3 '))
print('-'*44)
input('''Este programa irá mostrar a soma de todos os
números ímpares múltiplos de 3 entre 1 e 500. 
Aperte enter para começar.''')

sum_numbers = 0
total_numbers = 0

for i in range(3, 501, 6):
    sum_numbers += i
    total_numbers += 1

print(f'\nA soma de todos os {total_numbers} valores citados é {sum_numbers}.')
