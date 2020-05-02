city = input('Em que cidade você nasceu?').strip().lower()

first_word = city[:city.find(' ')]
starts_with_santo = first_word == 'santo'

if starts_with_santo:
    print('A cidade de {} se inicia com "Santo".'.format(city.title()))
else:
    print('A cidade de {} não se inicia com "Santo".'.format(city.title()))



