products_prices = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-'*50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('-'*50)

for index, item in enumerate(products_prices):
    if index % 2 == 0:
        print('{:.<40}'.format(item), end='')
        print('R$', end=' ')
    else:
        print(str(f'{item:>6.2f}').replace('.', ','))

print('-'*50)
