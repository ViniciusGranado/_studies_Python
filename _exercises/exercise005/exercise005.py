def show_number_succesor_predecessor():
    user_number = (input('Digite um número: '))

    if user_number.isnumeric():
        converted_user_number = int(user_number)
        print('O antecessor de {} é {}.'.format(converted_user_number, (converted_user_number-1)))
        print('O sucessor de {} é {}.'.format(converted_user_number, (converted_user_number+1)))
    else:
        print('Número inválido. Tente novamente')
        show_number_succesor_predecessor()
        

show_number_succesor_predecessor()


