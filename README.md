# Script_OLT
Scripts usados na OLT HUAWEI para facilitar gerenciamento

- Script de remoção:
OLT's são definidas no codigo com dados necessários para o acesso, após conexão utilizam o serial da ONU a ser removida para captura de algumas informações (ONT_ID, PLACA, PORTA...), script conta com algumas trativas de erro e localização de ONU caso serial não pertença a OLT ou o mesmo foi escrito de forma incorreta.

Obs: Script utiliza o acesso via telnet, alem de ser testado em alguns modelos da OLT HUAWEI (MA5800V100R019C12, MA5600V800R017C00, MA5800V100R018C10, MA5800V100R018C00). Recomendo a criação de um arquivo executavel pra facilitar no uso do script.
