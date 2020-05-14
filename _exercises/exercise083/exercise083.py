def check_expression(expression_str):
    is_valid = True

    for i in expression_str:
        if i == '(':
            break
        if i == ')':
            is_valid = False
            break

    if expression_str[expression_str.index('('):].count('(') != expression_str[expression_str.index('('):].count(')'):
        is_valid = False

    return is_valid


expression = input('Digite a expressão matemática à ser analisada: ').strip()

is_expression_valid = check_expression(expression)

if is_expression_valid:
    print('Sua expressão é valida')
else:
    print('Sua expressão não é valida.')
