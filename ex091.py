from random import randint
from time import sleep

plays = list()
scoreboard = dict()
for i in range(0, 4):
    scoreboard['name'] = str(input('Nome do jogador: '))
    print('Jogando os dados...', end='')
    for c in range(3, 0, -1):
        #sleep(1)
        print(c, end='...')
    scoreboard['score'] = randint(1, 6)
    plays.append(scoreboard.copy())
    print('Valor armazenado com sucesso!')


ordened_score = []
maior = menor =  0

for i in plays:
    ordened_score.append(i['score'])
    if len(ordened_score) == 4:
        ordened_score.sort(reverse=True)
        


    # if len(ordened_score) == 0:
    #     ordened_score.append(i)
    #     maior = menor = i['score']
    # else:
    #     if i['score'] > maior:
    #         ordened_score.insert(i.copy())
    #         maior = i['score']
    #     if i['score'] < menor:
    #         ordened_score.append(i.copy())
    #         menor = i['score']


print(ordened_score)

