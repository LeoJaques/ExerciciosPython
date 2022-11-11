while True:
    stop = int(input('Quer ver a tabuada de qual valor? '))
    if stop < 0:
        break
    print('-'*20)
    for i in range(1, 11):
        print(f'{stop} x {i:2} = {stop * i}')
    print('-'*20)
print('BRROOOOOOoooo...')