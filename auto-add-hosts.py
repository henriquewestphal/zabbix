from pyzabbix import ZabbixAPI
import csv
import sys
username = sys.argv[1]
senha = sys.argv[2]

print username
zapi = ZabbixAPI("http://m7.by7.com.br/")
zapi.login(user=username, password=senha)

arq = csv.reader(open('/tmp/hosts.csv'))

linhas = sum(1 for linha in arq)

f = csv.reader(open('/tmp/hosts.csv'), delimiter=';')
i = 0

for [hostname,ip] in f:
    hostcriado = zapi.host.create(
        host= hostname,
        status= 0,
        interfaces=[{
            "type": 1,
            "main": "1",
            "useip": 1,
            "ip": ip,
            "dns": "",
           "port": 10050
        }],
        groups=[{
            "groupid": 193},
            {"groupid": 9},
            {"groupid": 10},
            {"groupid": 36
        }],
        templates=[{
            "templateid": 10104
        }],
        proxy_hostid=14555
    
    )
    print ("ADD Host" + hostname + "com o IP:" + ip)

    i += 1
print " "
