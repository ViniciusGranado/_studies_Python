import currency
import numbers

user_number = numbers.get_number()
print(f'A metade de R${user_number} é R${currency.half(user_number)}.')
print(f'O dobro de R${user_number} é R${currency.double(user_number)}.')
print(f'Acrescentando 10%, temos R${currency.increase_n_percent(user_number, 10)}.')
print(f'Subtraindo 15%, temos R${currency.decrease_n_percent(user_number, 15)}.')
