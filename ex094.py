pessoa = {}
listao = []
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERROR!, Por favor insira M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    listao.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERROR! Responda apenas S ou N')
    if resp == 'N':
        break
media = soma / len(listao)

print(f'A) O todo temos {len(listao)} pessoas cadastrada')
print(f'B) A média das idades é de {media:5.2f} anos')
print(f'C) As mulheres cadastradas foram ', end='')
for i in listao:
    if i['sexo'] == 'F':
        print(f'{i["nome"]}', end=' ')
print()
print(f'D) Pessoas com idade acima da média:')
for i in listao:
    if i['idade'] > media:
        print('   ')
        for k, v in i.items():
            print(f'{k} = {v};', end='')
        print()

