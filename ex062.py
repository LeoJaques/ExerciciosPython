print('='*20)
print(' 10 TERMOS DE UMA PA')
print('='*20)
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro_termo
i = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while i < total:
        print(' {} '.format(termo), end='➡')
        termo += razao
        i += 1
    print(' PAUSA ')
    mais = int(input('Quantos termos você quer mostrar a mais: '))
print('O total de termos foi {}..'.format(total))