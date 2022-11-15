brasileirao = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians',
               'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza',
               'São Paulo', 'América-MG', 'Botafogo', 'Santo', 'Goiás',
               'Bregantino', 'Coritiba', 'Cuiabá', 'Ceará SC', 'Atlético-GO',
               'Avaí', 'Juventude')

print('Os 5 primeiros colocas são:')
for i in range(0, 5):
    print(brasileirao[i])

print('-'*30)

print('Os 4 últimos são:')
for i in range(len(brasileirao) - 1, len(brasileirao) - 5, -1):
    print(brasileirao[i])

print('-'*30)

print('Essa é a ordem alfabetica dos times: ')
ordem = sorted(brasileirao)
for i in ordem:
    print(i)

print('-'*30)


flamengo = brasileirao.index('Flamengo') + 1
print(f'O Flamengo entá na {flamengo}° posição')