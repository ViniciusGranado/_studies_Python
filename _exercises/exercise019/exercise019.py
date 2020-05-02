from random import choice


names = [input("Nome do primeiro aluno: "),
         input("Nome do segundo aluno: "),
         input("Nome do terceiro aluno: "),
         input("Nome do quarto aluno: ")
         ]

print('O aluno escolhido foi {}.'.format(choice(names)))
