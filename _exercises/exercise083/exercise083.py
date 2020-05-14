def check_expression(expression_str):
    control = 0

    for i in expression_str:
        if i == '(':
            control += 1
        if i == ')':
            if control > 0:
                control -= 1
            else:
                control += 1

    return control == 0


expression = input('Digite a expressão matemática à ser analisada: ').strip()

is_expression_valid = check_expression(expression)

if is_expression_valid:
    print('Sua expressão é valida')
else:
    print('Sua expressão não é valida. Verifique os parênteses.')
