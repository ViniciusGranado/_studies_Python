user_input = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(user_input)))
print('Só tem espaços? {}'.format(user_input.isspace()))
print('É um número? {}'.format(user_input.isnumeric()))
print('É alfabético? {}'.format(user_input.isalpha()))
print('É alfanumérico? {}'.format(user_input.isalnum()))
print('Está em maiúsculas? {}'.format(user_input.isupper()))
print('Está em minúsculas? {}'.format(user_input.islower()))
print('Está capitalizada? {}'.format(user_input.istitle()))




