from pyzabbix import ZabbixAPI
import csv
import sys

url = sys.argv[1]
username = sys.argv[2]
senha = sys.argv[3]

zapi = ZabbixAPI(url=url, user=username, password=senha)

f = csv.reader(open('/tmp/addhosts'), delimiter=';')

for [hostname,ip] in f:
    hostcriado = zapi.host.create(
        host= hostname,
        status= 0,
        macros=[{
                "macro": "{$SNMP_COMMUNITY}",
                "value": "public"},
                {
                "macro": "{$SCRIPT.DIR}",
                "value": "/opt/seven/scripts",
        }],
        interfaces=[{
            "type": 1,
            "main": "1",
            "useip": 1,
            "ip": ip,
            "dns": "",
           "port": 10050},
           {
            "type": 2,
            "main": "1",
            "useip": 1,
            "ip": ip,
            "dns": "",
           "port": 161
        }],
        groups=[{
            "groupid": 193},
            {"groupid": 9},
            {"groupid": 10},
            {"groupid": 36
        }],
        templates=[{
            "templateid": 10104},
			{"templateid" : 17287
		}],
        proxy_hostid=14555,
    
    )
    print ("ADD Host " + hostname + " com o IP:" + ip)

print ("Processo finalizado!")