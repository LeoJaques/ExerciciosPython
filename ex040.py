n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print('A média do aluno foi {:.1f}'.format(m))
if m < 5:
    print('Aluno REPROVADO!')
elif 7 > m >= 5:
    print('Aluno em RECUPERAÇÃO!')
elif m >= 7:
    print('Aluno APROVADO!')