list = []

for i in range(1, 6):
    list.append(int(input(f'Digite o {i}° valor: ')))

print('-='*40)
print(f'Assim ficou a lista {list}')
print(f'O maior valor digitado foi {max(list)} nas posições ', end='')
for c, i in enumerate(list):
    if i == max(list):
        print(f'{c}...', end='')
print()
print(f'O menor valor digitado foi {min(list)} nas posições ', end='')
for c, i in enumerate(list):
    if i == min(list):
        print(f'{c}...', end='')
print()
