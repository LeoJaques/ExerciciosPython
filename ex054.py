from datetime import datetime
atual = datetime.today().year
maior_idade = 0
menor_idade = 0
for i in range(1, 7+1):
    ano = int(input('Digite o ano de nascimento da {}° pessoa: '.format(i)))
    if atual - ano >= 21:
        maior_idade += 1
    else:
        menor_idade += 1
print('{} são maior de idade'.format(maior_idade))
print('{} são menor de idade'.format(menor_idade))
