tot_mulhers_20 = tot_homens = tot18 = 0
while True:
    idade = int(input('Idade: '))
    sexo = resp = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        tot_homens += 1
    if sexo == 'F' and idade < 20:
        tot_mulhers_20 += 1
    while resp not in 'SN':
        resp = str(input('Quer continuar? ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Total de homens cadastrado: {tot_homens} ')
print(f'Total de mulhers com menos de 20 anos: {tot_mulhers_20}')