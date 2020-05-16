from random import randint


def highest_number(*numbers):
    print('-'*30)
    print('Analisando os valores informados...')
    highest = 0
    for index, item in enumerate(numbers):
        print(item, end=' ')
        if item > highest:
            highest = item

    if len(numbers) == 0:
        print('\nNão foi informado nenhum valor.')
        return
    elif len(numbers) == 1:
        print(f'\nFoi informado apenas 1 valor ao todo.')
    else:
        print(f'\nForam informados {len(numbers)} valores ao todo.')
    print(f'O maior valor informado foi {highest}')


highest_number(randint(0, 50), randint(0, 50), randint(0, 50), randint(0, 50), randint(0, 50), randint(0, 50))

highest_number(randint(0, 50), randint(0, 50), randint(0, 50))

highest_number(randint(0, 50), randint(0, 50))

highest_number(randint(0, 50))

highest_number()
