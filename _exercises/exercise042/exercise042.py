def validate_float_number(number_str):
    is_valid = True

    if number_str == '' or number_str[-1] == '.':
        is_valid = False
    else:
        for i in number_str:
            if not (i.isnumeric() or i == '.'):
                is_valid = False

    return is_valid


def get_number(i):

    mensagem = ['Primeiro', 'Segundo', 'Terceiro']
    while True:
        user_number = input(f'{mensagem[i]} segmento: ').replace(',', '.')

        if validate_float_number(user_number):
            return float(user_number)
        else:
            print('Valor inválido.')


def check_triangle(side1, side2, side3):
    return (side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2)


def get_category(side1, side2, side3):
    if side1 == side2 == side3:
        return 'EQUILÁTERO'
    elif side1 != side2 != side3 != side1:
        return 'ESCALENO'
    else:
        return 'ISÓSCELES'


print('-='*18)
print('Analisador de Triângulos')
print('-='*18)

print('Digite abaixo o comprimento de cada segmento do triângulo.')

sides = [get_number(0), get_number(1), get_number(2)]

if check_triangle(sides[0], sides[1], sides[2]):
    category = get_category(sides[0], sides[1], sides[2])
    print(f"Os segmentos acima PODEM formar um triângulo {category}!")
else:
    print("Os segmentos acima NÃO PODEM formar um triângulo!")


