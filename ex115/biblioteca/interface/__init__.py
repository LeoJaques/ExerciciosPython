def line(size=42):
    return '-' * size

def header(txt):
    print(line())
    print(txt.center(42))
    print(line())

def menu(list):
    header('SISTEMA ARQUIVO')
    for v, i in enumerate(list, 1):
        print(f'\033[33m{v}\033[m - \033[34m{i}\033[m')
    resp = menu_escolha()
    return resp
def menu_escolha():
    from ex113.leiaNum.leiaInt import leiaInt
    from ex115.biblioteca.arquivo import ler_arquivo
    escolha_usuario = {
        1: 'USUÁRIOS CADASTRADOS',
        2: 'CADASTRAR USUÁRIO',
        3: 'Saindo do sistema...'
    }
    opc = leiaInt('\033[32mSua Opção:\033[m ')
    if opc not in escolha_usuario.keys():
        print('\033[31mERRO. Opção inválida\033[m')
    else:
        header(escolha_usuario[opc])
        return opc


