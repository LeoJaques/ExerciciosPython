soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
mulher_20 = 0
for i in range(1, 5):
    print('-----{} PESSOA-----'.format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade
    if i == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulher_20 += 1
media_idade = soma_idade / 4
print('A média de idade do grupo é de {} anos'.format(media_idade))
print('A idade do homem mais velho é {} e seu nome é {}.'.format(maior_idade_homem, nome_velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher_20))