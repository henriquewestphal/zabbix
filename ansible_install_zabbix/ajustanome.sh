#!/bin/bash
nome=`echo $HOSTNAME | sed 's/.sol/ /' | awk '{print $1}'`
echo "Hostname=Cliente-${nome^^}" >> /opt/seven/zabbix/conf/zabbix_agentd.conf
