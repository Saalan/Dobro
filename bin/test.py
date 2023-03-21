#!/usr/bin/env python3
import re
import psycopg2
import subprocess
from psycopg2 import Error

conn = psycopg2.connect(user="dobro_dbuser",
                        password="~6331dobro",
                        host="192.168.1.90",
                        port="5432",
                        database="dobro")

try:
    with conn, conn.cursor() as curs:
       curs.execute("SELECT MAX(id_count_start) FROM parsec_dns")		# максимальный номер счетчика запусков
       count_start = curs.fetchone()[0]
       print ("cursor.rowcount",cursor.rowcount)

       if count_start is None: count_start = 0
       count_start += 1								# счетчик запусков +1

       print (type(count_start),count_start)
       # таблица конфигурации 
       query="SELECT id, reqest_name, match_ip_count, first_redirect_port FROM parsec_cfg WHERE active_rule=true ORDER BY id"
       cursor.execute(query)
       print ("cursor.rowcount",cursor.rowcount)

       for cfg in cursor.fetchall():
          # print (type(cfg[1]),cfg[1])
          cmd = "dig A -4 +noall +answer "+cfg[1]					# DNS запрос 
          sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
          redirect_port=cfg[3]
          print("\n####",cmd,redirect_port)
          for out in iter(sp.stdout.readline,b''):
             data = out.decode('utf-8').split()
             if re.match(r'((?:\d{1,3}\.?){4})', data[4]):
                 print (data,"B================>",data[1])
                 with conn, conn.cursor() as curs:
                    query="INSERT INTO public.parsec_dns (id_count_start, id_request_name, responce_name, ttl, ipv4, redirect_port) VALUES (%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING"
                    curs.execute(query, (count_start, cfg[0], data[0], data[1], data[4], redirect_port))
                    print ("cursor.rowcount",cursor.rowcount)
                    conn.commit()
                    redirect_port += 1



except psycopg2.Error as e:
    if e.pgcode == '23505': print ("# 23505 ##########################################################################")
    print(e.pgcode, e.pgerror)
finally:
    if conn:
       cursor.close()
       conn.close()
       print("Соединение с PostgreSQL закрыто")


