print('='*20)
print(' 10 TERMOS DE UMA PA')
print('='*20)
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro_termo
i = 0
while i < 10:
    print(' {} '.format(termo), end='➡')
    termo += razao
    i += 1


print(' ACABOU ')