def get_age():
    while True:
        user_number = input('Idade: ').strip()

        if user_number.isnumeric():
            return int(user_number)
        else:
            print('Valor inválido.')


def get_option():
    while True:
        user_option = input('Deseja cadastrar outro usuário? [S/N] ').strip().upper()

        if user_option == 'S' or user_option == 'N':
            return user_option
        else:
            print('Opção inválida.')


def get_gender():
    while True:
        user_option = input('Sexo: [M/F] ').strip().upper()

        if user_option == 'M' or user_option == 'F':
            return user_option
        else:
            print('Opção inválida. Utilize apenas M ou F.')


def check_if_women(list_of_dict):
    for i in list_of_dict:
        if i['sex'] == 'F':
            return True

    return False


# Get users data
users = list()

while True:
    new_user = dict()
    new_user['name'] = input('\nNome: ').strip().title()
    new_user['sex'] = get_gender()
    new_user['age'] = get_age()

    users.append(new_user.copy())

    if get_option() == 'N':
        break

# Show number of users registered
print('-'*50)

if len(users) == 1:
    print(f'- Ao todo temos 1 usuário cadastrado.')
else:
    print(f'- Ao todo temos {len(users)} usuários cadastrados.')

# Show age average
age_sum = 0
for i in users:
    age_sum += i['age']
age_average = age_sum / len(users)
print(f'- A média de idade dos usuário é de {age_average:.1f} anos.')


# Show registered women
# To-do: Fix comma when first user is not woman.
if check_if_women(users):
    print('- As mulheres cadastradas foram: ', end='')
    for index, item in enumerate(users):
        if index == 0 and item['sex'] == 'F':
            print(item['name'], end='')
        elif index == len(users)-1 and item['sex'] == 'F':
            print(f' e {item["name"]}', end='')
        elif item['sex'] == 'F':
            print(', ' + item['name'], end='')
else:
    print('- Não há mulheres cadastradas.')


# Show people with age above average
print('\n- Lista de pessoas com idade acima da média do grupo: ')
for i in users:
    if i['age'] > age_average:
        print(f'     Nome: {i["name"]}; Sexo: {i["sex"]}; Idade: {i["age"]}')
