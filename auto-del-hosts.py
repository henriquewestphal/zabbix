from pyzabbix import ZabbixAPI
import csv
import sys

username = sys.argv[1]
senha = sys.argv[2]

zapi = ZabbixAPI(url='http://m7.by7.com.br/', user=username, password=senha)
f = csv.reader(open('/tmp/delidhosts'), delimiter=';')

for hostdel,hostname in f:
	print hostdel
	result = zapi.host.delete(hostid = hostdel)
	print result
	print ("Host " + hostname + " Deletado  ID: " + hostdel )
	
print ("Processo finalizado!")