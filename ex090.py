aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] >= 7:
    print('-'*40)
    print(f'O aluno {aluno["nome"]} está APROVADO ')
    aluno['aprovado'] = True
else:
    print('-'*40)
    print(f'O aluno {aluno["nome"]} não obteve a média 7 ou superior e está REPROVADO')
    aluno['aprovado'] = False

print('-'*40)
print('Estrutura: ')
print(aluno)
