def numbers_count(start, end, step):
    print('-=' * 20)
    print(f'Contagem de {start} até {end} em passo {abs(step)}.')

    if start == end:
        print('Os valores de início e fim são iguais, não é possível realizar a contagem.')
    else:
        if step == 0:
            step = 1
            print('Não é possível realizar a contagem com passo 0. Considerando passo 1.')

        if start < end:
            step = abs(step)
            end += 1
        elif start > end:
            step = -abs(step)
            end -= 1

        for i in range(start, end, step):
            print(i, end=' ')
        print('FIM!')


def validate_integer_str(str_number):
    if str_number.isnumeric():
        return True
    elif str_number[0] == '-' and str_number[1:].isnumeric():
        return True

    return False


def get_number(msg_index):
    message = ('Início: ', 'Fim: ', 'Passo: ')
    while True:
        user_number_str = input(message[msg_index]).strip()
        if validate_integer_str(user_number_str):
            return int(user_number_str)
        else:
            print('Número inválido, tente novamente.')


# Count 1 to 10 in step 1
numbers_count(1, 11, 1)

# Count 10 to 0 in step 2
numbers_count(10, -1, -2)

# Personalized count
user_start = get_number(0)
user_end = get_number(1)
user_step = get_number(2)

numbers_count(user_start, user_end, user_step)
