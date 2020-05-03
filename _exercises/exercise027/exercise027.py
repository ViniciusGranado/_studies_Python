name_list = input('Digite o seu nome completo: ').strip().lower().split()

print('Muito prazer em conhecer!')
print('O seu primeiro nome é {}'.format(name_list[0].capitalize()))
print('O seu último nome é {}.'.format(name_list[-1].capitalize()))
