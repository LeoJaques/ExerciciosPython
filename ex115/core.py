from biblioteca.interface import *
from biblioteca.arquivo import *
from time import sleep
from ex113.leiaNum.leiaInt import leiaInt


file = './biblioteca/arquivo/cursoemvideo.txt'

if not arquivo_existe(file):
    criar_arquivo(file)
else:
    print('Arquivo já existe')

while True:
    resp = menu(['USUÁRIOS CADASTRADOS', 'CADASTRAR USUÁRIO', 'SAIR DO SISTEMA'])
    if resp == 1:
        ler_arquivo(file)
    elif resp == 2:
        cadastrar_usuario(file)
    elif resp == 3:
        break
    sleep(2)