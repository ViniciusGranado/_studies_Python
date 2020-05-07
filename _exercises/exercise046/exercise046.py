from time import sleep


print('-'*40)
print('{:^40}'.format('CONTAGEM REGRESSIVA PARA O ANO NOVO'))
print('-'*40)
input('Aperte enter para iniciar: ')
print()

for i in range(10, 0, -1):
    print(i)
    sleep(1)

print('-'*40)
print('{:^40}'.format('FELIZ ANO NOVO!!!!!'))
print('-'*40)