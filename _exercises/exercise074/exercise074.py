from random import randint

numbers = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))

print('Os números sorteados foram: ', end='')

for i in numbers:
    print(i, end=' ')

print(f'\nO maior valor sorteado foi {max(numbers)}.')
print(f'O menor valor sorteado foi {min(numbers)}.')
