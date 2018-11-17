# ZABBIX


## ADD HOST auto-add-hosts.py

Script criado conforme necessidade de adicionar varios host de uma so vez via API. 

Nela voce pode setar o Proxy, Templates, Groupos e macros, conforme necessidade. 

Para usar basta passar como parametro a URL de conexão com a API, usuário e senha. 

Necessario criar um arquivo no /tmp/addhosts

com a estrutura hostname;IP

Exemplo:
```
Server1;10.10.0.1
Server2;10.10.0.2
Server3;10.10.0.3
```


## DEL HOST auto-del-hosts.py

Script criado para deletar o host de forma automatica. 

Para usar basta passar como parametro a URL de conexão com a API, usuário e senha.
Basta Criar um arquivo /tmp/delidhosts

com a estrutura hostid;hostname

Exemplo:
```
14132;Server1
14133;Server2
14134;Server3
```
