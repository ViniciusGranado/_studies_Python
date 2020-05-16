from random import randint
from time import sleep


# Functions
def draw(lst):
    print('Sorteando 5 valores pares na lista: ', end='')
    for i in range(0, 5):
        random_number = randint(0, 100)
        print(random_number, end=' ')
        lst.append(random_number)
        sleep(0.3)

    sum_even(lst)


def sum_even(lst):
    sum_even_numbers = 0
    for i in lst:
        if i % 2 == 0:
            sum_even_numbers += i

    print(f'\nSomando os valores pares de {lst}, temos {sum_even_numbers}.')


# Main program
numbers = list()
draw(numbers)
