import currency
import numbers

user_number = numbers.get_number()
print(f'A metade de {currency.format_currency(user_number)} é {currency.half(user_number)}.')
print(f'O dobro de {currency.format_currency(user_number)} é {currency.double(user_number)}.')
print(f'Acrescentando 10%, temos {currency.increase10percent(user_number, 10)}.')
print(f'Subtraindo 15%, temos {currency.decrease10percent(user_number, 15)}.')
