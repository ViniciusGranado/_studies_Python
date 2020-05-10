gender = input('Informe o seu sexo: [M/F] ').upper()

while not (gender == 'M' or gender == 'F'):
    gender = input('Dados inválidos. Por favor, informe o seu sexo: [M/F] ').upper()


print(f'Sexo {gender} validado com sucesso.')
