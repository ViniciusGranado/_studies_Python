name = input("Digite o seu nome completo: ").strip().lower()
name_list = name.split()
has_silva = "silva" in name_list

if has_silva:
    print('O seu nome, "{}", possui "Silva".'.format(name.title()))
else:
    print('O seu nome, "{}", não possui "Silva".'.format(name.title()))
