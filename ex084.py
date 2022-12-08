pessoas = []
dados = []
maior_peso = menor_peso = 0
while True:
    dados.append(str(input('Nome :')).strip())
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior_peso = menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        if dados[1] < menor_peso:
            menor_peso = dados[1]

    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('-='*15)

print(f'Total de pessoas: {len(pessoas)}')
print(f'O maior peso foi de {maior_peso}Kg. Peso de ', end='')
for i in pessoas:
    if i[1] == maior_peso:
        print(f'[{i[0]}] ', end='')
print()
print(f'O menor peso foi de {menor_peso}Kg. Peso de ', end='')
for i in pessoas:
    if i[1] == menor_peso:
        print(f'[{i[0]}] ', end='')