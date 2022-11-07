import random
aluno1 = str(input('Qual o no nome do 1° aluno:'))
aluno2 = str(input('Qual o no nome do 2° aluno:'))
aluno3 = str(input('Qual o no nome do 3° aluno:'))
aluno4 = str(input('Qual o no nome do 4° aluno:'))
sorteio = [aluno1, aluno2, aluno3, aluno4]
print('O aluno que ira apagar o quadro é {}'.format(random.choice(sorteio)))
print(type(sorteio))