from pyzabbix import ZabbixAPI
import csv
import sys
url = sys.argv[1]
username = sys.argv[2]
senha = sys.argv[3]

zapi = ZabbixAPI(url=url, user=username, password=senha)
f = csv.reader(open('/tmp/delidhosts'), delimiter=';')

for hostdel,hostname in f:
	print hostdel
	result = zapi.host.delete(hostid = hostdel)
	print result
	print ("Host " + hostname + " Deletado  ID: " + hostdel )
	
print ("Processo finalizado!")