import telnetlib
from time import sleep

#Script criado para remoção de ONU em OLT's HUAWEI
#Criador: Carlos Bruno
#19/04/2023


def remover():
    comandos_remover = [f'undo service-port port {fsp} ont {ont_id} \n\n', 'y \n', f'interface gpon 0/{placa} \n', f'ont delete {porta} {ont_id}\n' ]

    for comando in comandos_remover:
        telnet.write(comando.encode('utf-8'))
        sleep(2)

def olt(num):
    if num == 1:
        dados_olt = {
            'host': b'Ip-acesso',
            'port': 23,
            'usuario': b'Usuario\n',
            'senha': b'Senha\n',
        }
        
    elif num == 2:
        dados_olt = {
            'host': b'Ip-acesso',
            'port': 23,
            'usuario': b'Usuario\n',
            'senha': b'Senha\n',
        }

    elif num == 3:
        dados_olt = {
            'host': b'Ip-acesso',
            'port': 23,
            'usuario': b'Usuario\n',
            'senha': b'Senha\n',
        }

    elif num == 4:
        dados_olt = {
            'host': b'Ip-acesso',
            'port': 23,
            'usuario': b'Usuario\n',
            'senha': b'Senha\n',
        }
        
    elif num == 5:
        dados_olt = {
            'host': b'Ip-acesso',
            'port': 23,
            'usuario': b'Usuario\n',
            'senha': b'Senha\n',
        }
    
    return dados_olt    

def titulo():
    print('-' * 50)
    print(f"{'Menu de opções':^50}")
    print('-' * 50)
    
    print('[1] - Olt-1')
    print('[2] - Olt-2')
    print('[3] - Olt-3')
    print('[4] - Olt-4')
    print('[5] - Olt-5')
    print('\n')

def pesquisa():
    comandos_pesquisa = [f'enable \n', f'config \n', f'display ont info by-sn {serial} \n\n' ]

    for comando in comandos_pesquisa:
        telnet.write(comando.encode('utf-8'))
        sleep(2)
        
titulo()

try:
    
    opcao = int(input('Escolha sua opção: '))
    if not 0 < opcao < 6:
        raise ValueError
    
    dados = olt(opcao)
    
    telnet = telnetlib.Telnet(dados['host'], dados['port'], timeout=5)
    
    telnet.read_until(b'name:')
    telnet.write(dados['usuario'])

    telnet.read_until(b'password:')
    telnet.write(dados['senha'])

    serial = input('Informe o serial: ')

    pesquisa()

    sleep(3)

    data = telnet.read_until(b'Control', timeout=5).decode('utf-8')

    teste = data.split()

    if 'error' in teste:
        print('Serial incorreto !!')
        telnet.close()

    elif 'exist' in teste:
        print('Serial não encontrado nesta OLT')
        telnet.close()
        
    else:
        
        telnet.write(b'q \n')
        
        linhas = data.splitlines()
        del linhas[:-3]
        linhas.pop()

        placaPorta = linhas[0].split(':')
        fsp = placaPorta[1]
        filtroPlaca = placaPorta[1].split('/')
        placa = filtroPlaca[1]
        porta = filtroPlaca[2]
        ont = linhas[1].split(':')
        ont_id = ont[1]
        remover()
        
        print('ONU removida com Sucesso!!')
        telnet.close() 
    
except ValueError:
    print('Dados incorretos, tente novamente...')
    
except Exception:
    print('Erro ao realizar conexão, fale com o responsável !!!')


