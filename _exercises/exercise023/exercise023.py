def validate_int_number(int_number_str):
    is_number_valid = True

    for i in int_number_str:
        if not i.isnumeric():
            is_number_valid = False
            return is_number_valid

    if (int(int_number_str) < 0) or (int(int_number_str) > 9999):
        is_number_valid = False

    return is_number_valid


def get_number():
    is_valid = False

    while not is_valid:
        number_str = input('Digite um valor inteiro entre 0 e 9999: ')
        is_valid = validate_int_number(number_str)

        if is_valid:
            return number_str
        else:
            print('Número inválido, tente novamente.')


number = get_number()
final_number = number.zfill(4)

print('Analisando o número {}'.format(number))
print('Unidade: {}'.format(final_number[3]))
print('Dezena: {}'.format(final_number[2]))
print('Centena: {}'.format(final_number[1]))
print('Milhar: {}'.format(final_number[0]))
