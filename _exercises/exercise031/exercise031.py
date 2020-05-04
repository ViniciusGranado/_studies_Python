def validate_int_number(number_str):
    is_valid = True

    if not (number_str.isnumeric()):
        return False

    return is_valid


def get_number():
    while True:
        user_number = input("Qual é a distância da sua viagem? ")

        if validate_int_number(user_number):
            return int(user_number)
        else:
            print('Distância inválida.')


number = get_number()
ticket_price = (number*0.50) if number <= 200 else (number*0.45)
formatted_ticket = str("{:.2f}".format(ticket_price)).replace('.', ',')

print(f"Você está preste a começar uma viagem de {number}Km")
print(f"E o preço da sua passagem será de R${formatted_ticket}")



