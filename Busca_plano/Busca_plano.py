import telnetlib
from time import sleep
from os import system

#Script criado para verificação de plano
#Criador: Carlos Bruno
#06/05/2023



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
        
def filtro_serial():
    linhas = dados_serial.splitlines()
    del linhas[:-3]
    linhas.pop()

    placaPorta = linhas[0].split(':')
    fsp = placaPorta[1]

    ont = linhas[1].split(':')
    ont_id = ont[1]

    return fsp, ont_id

def captura_index():
    busca_index = telnet.read_until(b'common', timeout=5).decode('utf-8')
    linhas_index = busca_index.splitlines()
    del linhas_index[:-3]
    index_filtro = linhas_index[2].split()
    index = index_filtro[0]

    return index
    
def filtro_velocidade():
    busca_velocidade = telnet.read_until(b'Admin', timeout=5).decode('utf-8').splitlines()

    del busca_velocidade[:-4]

    filtro_upload = busca_velocidade[0].split(':')
    upload = filtro_upload[1]
    filtro_download = busca_velocidade[2].split(':')
    download = filtro_download[1] 
    
    return download, upload

clear = lambda: system('clear')

while True:
    titulo()

    try: 
        opcao = int(input('Escolha sua opção: '))
            
        if not 0 < opcao < 7:
            raise ValueError
            
        dados = olt(opcao)
                    
        telnet = telnetlib.Telnet(dados['host'], dados['port'], timeout=5)
                    
        telnet.read_until(b'name:')
        telnet.write(dados['usuario'])

        telnet.read_until(b'password:')
        telnet.write(dados['senha'])

        serial = input('Informe o serial: ')
                
        pesquisa()
                
        dados_serial = telnet.read_until(b'Control', timeout=5).decode('utf-8')
                
        erro = dados_serial.split()

        if 'error' in erro:
            print('Serial incorreto !!')
            telnet.close()

        elif 'exist' in erro:
            print('Serial não encontrado nesta OLT')
            telnet.close()
                    
        else:
            
            telnet.write(b'q\n\n')
                
            fsp, ont_id = filtro_serial()

            telnet.write(f'display service-port port {fsp} ont {ont_id}\n\n'.encode('utf-8'))
            sleep(2)
            telnet.write(b'q\n\n')
                    
            index = captura_index()

            telnet.write(f'display service-port {index}\n\n'.encode('utf-8'))
                    
            download, upload = filtro_velocidade()

            print(f'Seu Download é:{download}')
            print(f'Seu Upload é:{upload}')
                        
            telnet.close()

    except ValueError:
        print('Dados incorretos, tente novamente...')
        
    except Exception:
        print('Erro ao realizar conexão, fale com o responsável !!!')
    
    saida = input('Digite qualquer tecla para refazer ou 0 para sair: ')
    clear()
    
    if saida == '0':
        print('Programa finalizado!!!')
        break

