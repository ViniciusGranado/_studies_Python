sentence = input('Digite uma frase: ').replace(' ', '').upper()
inverse_sentence = sentence[::-1]

print(f'O inverso de {sentence} é {inverse_sentence}.')
if sentence == inverse_sentence:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')
