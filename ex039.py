import datetime
atual = datetime.date.today().year
print('{}ALISTAMENTO NO EXÉRCITO{}'.format('\033[7;32;40m', '\033[m'))
print('{}Verifique sua situação {}'.format('\033[7;40m', '\033[m'))
ano = int(input('Em qual ano você nasceu? '))
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))
if idade == 18:
    print('Você tem qie se alistar IMEDIATAMENTE!.')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    print('Seu alitamento foi em {}.'.format(ano))