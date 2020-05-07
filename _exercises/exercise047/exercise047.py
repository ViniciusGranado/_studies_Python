print('-'*50)
print('{:^50}'.format('NÚMEROS PARES'))
print('-'*50)
input('''Este programa irá mostrar todos os números pares 
entre 1 e 50. Aperte enter para começar: ''')
print()

for i in range(2, 51, 2):
    print(i, end=' ')
