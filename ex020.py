import random
aluno1 = str(input('Qual o nome do 1° aluno? '))
aluno2 = str(input('Qual o nome do 2° aluno? '))
aluno3 = str(input('Qual o nome do 3° aluno? '))
aluno4 = str(input('Qual o nome do 4° aluno? '))
sorteio = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(sorteio)
print('A ordem de aprensentação será: ')
print(sorteio)
