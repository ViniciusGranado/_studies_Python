words = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Grátis', 'Estudar', 'Praticar', 'Trabalhar', 'Mercado', 'Programador', 'Futuro')

for item in words:
    print(f'\nNa palavra {item.upper()} temos as vogais: ', end='')
    for letter in item.upper():
        if letter in ('AEIOUÁÀÃÂÉÊÍÓÔÕ'):
            print(letter, end=' ')
