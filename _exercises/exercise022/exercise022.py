name = input('Digite o seu nome completo: ').strip()
number_letters = (len(name)) - (name.count(' '))
name_list = name.split()

print('Analisando o seu nome...')
print('Seu nome em maiúsculas é {}'.format(name.upper()))
print('Seu nome em minúsculas é {}'.format(name.lower()))
print('Seu nome tem ao todo {} letras'.format(number_letters))
print('Seu primeiro nome é {} e ele tem {} letras'.format(name_list[0], len(name_list[0])))
