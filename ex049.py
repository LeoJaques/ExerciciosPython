print('  TABUADA  ')
num = int(input('Qual número você quer a tabuada? '))
for i in range(0, 10 + 1):
    print('{} X {:2} = {}'.format(num, i, num * i))
print('FIM!!')