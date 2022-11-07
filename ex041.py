import datetime
ano = int(input('Em qual ano o atleta nasceu? '))
atual = datetime.date.today().year
idade = atual - ano
print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JUNIOR')
elif idade <= 25:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')