def validate_int_number(number_str):
    is_valid = True

    if not (number_str.isnumeric()):
        return False

    return is_valid


def get_number(i):

    mensagem = ['primeiro', 'segundo', 'terceiro']
    while True:
        user_number = input(f'Digite o {mensagem[i]} valor: ')

        if validate_int_number(user_number):
            return int(user_number)
        else:
            print('Valor inválido.')


print('Digite três valores. O programa irá analisá-los e mostrar qual o maior e o menor número.')

numbers = [get_number(0), get_number(1), get_number(2)]

minor_number = numbers[0]
major_number = numbers[0]

for i in range(1, 3):
    if numbers[i] < minor_number:
        minor_number = numbers[i]
    if numbers[i] > major_number:
        major_number = numbers[i]

print(f'O menor valor digitado foi {minor_number}')
print(f'O maior valor digitado foi {major_number}')
