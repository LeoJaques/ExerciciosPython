matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = maior = soma_coluna = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor [{l}, {c}]: '))

for i in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[i][c]:^5}]', end='')
        if matriz[i][c] % 2 == 0:
            soma_par += matriz[i][c]
    print()
print('*'*40)
print(f'A soma dos valores pares é {soma_par}.')
for i in range(0, 3):
    soma_coluna += matriz[i][2]
print(f'A soma da coluna 3 é {soma_coluna}.')
for i in range(0, 3):
    if i == 0 or matriz[1][i] > maior:
        maior = matriz[1][i]

print(f'O maior valor da 2° linha é {maior}.')