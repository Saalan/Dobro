#!/usr/bin/env python3
import psycopg2
from psycopg2 import Error
from time import sleep

#role = "primary"
role = "slave"
srv_ip = "65.21.243.37"
static_rule = "#!/bin/bash\n# script add iptables rule for PARSEC.app\necho 1 > /proc/sys/net/ipv4/ip_forward\n"
#iptables -F -t nat
conn = psycopg2.connect(user="dobro_dbuser",password="~6331dobro",host="192.168.1.90",port="5432",database="dobro")
query ="""SELECT parsec_cfg.request_name, parsec_dns.ipv4, parsec_cfg.protocol, parsec_dns.redirect_port, parsec_cfg.work_port
FROM parsec_dns LEFT JOIN parsec_cfg ON parsec_dns.id_request_name=parsec_cfg.id
WHERE parsec_dns.id_count_start=(SELECT MAX(id_count_start) FROM parsec_dns)
ORDER BY parsec_dns.id_request_name, parsec_dns.redirect_port
"""

try:
   iptab_rule1 = "\n"
   iptab_rule2 = "\n"
   #srv_ip = srv_ip.ljust(15)
   with open("parsec_iptab_rule.sh","w") as f:
      f.write (static_rule)
      cursor = conn.cursor()
      cursor.execute(query)
      for data in cursor.fetchall():
         print (data)
         name   = data[0]
         dst_ip = data[1][:-3].ljust(15)
         proto  = data[2]
         r_port = str(data[3]).ljust(5)
         w_port = str(data[4]).ljust(5)
         if role=="prmary":
            iptab_rule1 += "iptables -t nat -A OUTPUT -d "+dst_ip+" -p "+proto+" --dport "+w_port+" -j DNAT --to-destination "+srv_ip+":"+r_port+"\t# "+name+"\n"
         if role=="slave":
            iptab_rule1 += "iptables -t nat -A PREROUTING -d "+srv_ip+" -p "+proto+" --dport "+r_port+" -j DNAT --to-destination "+dst_ip+":"+w_port+"\t# "+name+"\n"
            iptab_rule2 += "iptables -t nat -A POSTROUTING -d "+dst_ip+" -p "+proto+" --dport "+w_port+" -j SNAT --to-source "+srv_ip+":"+w_port+"\t# "+name+"\n"
      print (iptab_rule1)
      print (iptab_rule2)
      f.writelines (iptab_rule1)
      f.writelines (iptab_rule2)
except psycopg2.Error as e:
   print(e.pgcode, e.pgerror)
finally:
   if conn:
      cursor.close()
      conn.close()
      print("Соединение с PostgreSQL закрыто")