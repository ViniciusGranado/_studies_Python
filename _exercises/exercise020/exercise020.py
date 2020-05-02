from random import shuffle

names = [input('Digite o primeiro nome: '),
         input('Digite o segundo nome: '),
         input('Digite o terceiro nome: '),
         input('Digite o quarto nome: ')
         ]

shuffle(names)

print('\nOs nomes em ordem aleatória são: {}, {}, {} e {}.'.format(names[0], names[1],
                                                                   names[2], names[3]))
