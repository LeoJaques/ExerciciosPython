nome = str(input('Qual o nome do colaborador? '))
s = float(input('Qual o sálario do {} R$'.format(nome)))
a = s + (s * 0.15)
print('O novo salário do colaborador {} é de R$ {}'.format(nome, a))

