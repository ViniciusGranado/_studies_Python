def validate_float_number(number_str):
    is_valid = True

    if number_str == '' or number_str[-1] == '.':
        is_valid = False
    else:
        for i in number_str:
            if not (i.isnumeric() or i == '.'):
                is_valid = False

    return is_valid


def get_number(msg_index):
    message = ('Nota 1: ', 'Nota 2: ')
    while True:
        user_number = input(message[msg_index]).replace(',', '.')

        if validate_float_number(user_number) and 0 <= float(user_number) <= 10:
            if float(user_number).is_integer():
                return int(user_number)
            else:
                return float(user_number)
        else:
            print('Valor inválido.')


def get_student_number():
    while True:
        student_number_str = input('\nDigite o número de um aluno para ver as suas notas '
                                   'individuais: (digite 999 para sair) ').strip()

        if student_number_str.isnumeric() and not int(student_number_str) < 0 and \
        (not int(student_number_str) > len(students)-1 or student_number_str == '999'):
            return int(student_number_str)
        else:
            print('Número inválido, tente novamente.')


def get_option():
    while True:
        user_option = input('Deseja cadastrar outro aluno? [S/N] ').strip().upper()

        if user_option == 'S' or user_option == 'N':
            return user_option
        else:
            print('Opção inválida.')


# Students register
students = []
while True:
    student_name = (input('\nNome: ').strip().title())  # Get student name

    student_grade1 = get_number(0)  # Get grade 1
    student_grade2 = get_number(1)  # Get grade 2

    student_mean = (student_grade1 + student_grade2) / 2  # Get student mean

    # Register student on the students list
    students.append([student_name, [student_grade1, student_grade2], student_mean])

    option = get_option()  # Check if the user wants to register another student
    if option == 'N':
        break


# Grades table
print('\n' + '-'*50)
print(f'{"Noº":<4} {"NOME":<30} {"MÉDIA"}')
print('-'*50)

for index, item in enumerate(students):
    print(f'{index:<4}', end=' ')
    print(f'{item[0]:30}', end=' ')
    print(item[2])

print('-'*50)

# Show student's individual grades
while True:
    student_number = get_student_number()

    if student_number == 999:
        break

    print(f'Notas de {students[student_number][0]}: {students[student_number][1]}')

print('\nEncerrando...')
