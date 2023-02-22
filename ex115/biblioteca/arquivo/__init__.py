def arquivo_existe(file):
    try:
        a = open(file, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(file):
    try:
        a = open(file, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {file} criado com sucesso!')

def ler_arquivo(file):
    try:
        a = open(file, 'rt')
    except:
        print('ERRO ao ler o arquivo')
    else:
        for l in a:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} \t{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar_usuario(file):
    from ex113.leiaNum.leiaInt import leiaInt
    nome = str(input('Nome: ')).strip()
    if not nome:
        nome = 'desconhecido'
    idade = leiaInt('Idade: ')
    try:
        a = open(file, 'at')
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na gravação de dados no arquivo')
        else:
            print('Usuário cadastrado com sucesso!')
            a.close()