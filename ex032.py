from datetime import date
print('Que ano você quer analisar? Digite 0 para analisar o ano atual')
ano = int(input('Digite o ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bisexto'.format(ano))
else:
    print('O ano {} não é bisexto'.format(ano))
