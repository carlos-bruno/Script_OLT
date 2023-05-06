# Script_OLT
Scripts usados na OLT HUAWEI para facilitar gerenciamento

- Script de remoção:
Após conexão utilizam o serial da ONU a ser removida para captura de algumas informações (ONT_ID, PLACA, PORTA...), script conta com algumas trativas de erro e localização de ONU caso serial não pertença a OLT ou o mesmo foi escrito de forma incorreta.
- Script de busca:
Após conexão faz busca pelo serial inserido e captura alguns dados necessários (CHASSI, PLACA, PORTA, ONT_ID) para busca do service-port, com o mesmo encontrado captura os dados informados de Download e Upload, no caso destas OLT’s os dados informados são relacionados ao traffic table cadastrados na OLT.

Obs: OLT's são definidas no código com dados necessários para o acesso e funcionamento depende do modo de operação da OLT, Script utiliza o acesso via telnet, além de ser testado em alguns modelos da OLT HUAWEI (MA5800V100R019C12, MA5600V800R017C00, MA5800V100R018C10, MA5800V100R018C00). Recomendo a criação de um arquivo executável para facilitar no uso do script.
