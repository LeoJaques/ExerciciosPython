from random import randint
num_sorteados = (randint(1, 10), randint(1, 10), randint(1, 10),
                 randint(1, 10), randint(1, 10), )
print(f'Os valores sorteados foram {num_sorteados}')

print(f'O maior valor sorteado foi {max(num_sorteados)}')
print(f'O menor valor sorteado foi {min(num_sorteados)}')

