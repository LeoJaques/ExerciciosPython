par_impar = [[], []]
num = 0
for i in range(1, 8):
    num = int(input(f'Digite o {i}° valor:'))
    if num % 2 == 0:
        par_impar[0].append(num)
    else:
        par_impar[1].append(num)

print(f'Par: {sorted(par_impar[0])}')
print(f'Ímpar: {sorted(par_impar[1])}')