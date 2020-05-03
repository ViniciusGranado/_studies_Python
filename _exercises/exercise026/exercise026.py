def get_letter():
    is_letter_valid = False

    while not is_letter_valid:
        user_letter = input('Digite uma letra: ').strip().lower()
        is_letter_valid = validate_letter(user_letter)

        if is_letter_valid:
            return user_letter
        else:
            print('Letra inválida. Tente novamente.')


def validate_letter(letter_to_validate):
    is_valid = True

    if not (letter_to_validate.isalpha() and len(letter_to_validate) == 1):
        is_valid = False

    return is_valid


sentence = input("Digite uma frase: ").strip().lower()
letter = get_letter()
letter_count = sentence.count(letter)
first_occurrence = (sentence.find(letter)) + 1
last_occurrence = (sentence.rfind(letter)) + 1

if letter_count < 1:
    message = 'não aparece'
elif letter_count == 1:
    message = 'aparece 1 vez'
else:
    message = 'aparece {} vezes'.format(letter_count)

print('Ansalisando a frase: \'{}\''.format(sentence.capitalize()))
print('A letra \'{}\' {} na frase'.format(letter.upper(), message))
print('A primeira letra \'{}\' aparece na posição {}.'.format(letter.upper(), first_occurrence))
print('A última letra \'{}\' aparece na posição {}.'.format(letter.upper(), last_occurrence))

