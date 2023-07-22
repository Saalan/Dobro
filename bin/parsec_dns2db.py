#!/usr/bin/env python3
import re
import psycopg2
import subprocess
from psycopg2 import Error
from time import sleep


conn = psycopg2.connect(user="dobro_dbuser",password="~6331dobro",host="172.22.0.104",port="5432",database="dobro")

try:
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(id_count_start) FROM parsec_dns")		# максимальный номер счетчика запусков
    count_start = cursor.fetchone()[0]
    if count_start is None: count_start = 0
    count_start += 1								# счетчик запусков +1
    # таблица конфигурации 
    query="SELECT id, request_name, match_ip_count, first_redirect_port FROM parsec_cfg WHERE active_rule=true ORDER BY id"
    cursor.execute(query)
    for cfg in cursor.fetchall():
       #print (type(cfg[2]),cfg[2])
       new_ip_record = 0
       request_count = 0
       redirect_port=cfg[3]
       cmd = "dig A -4 +noall +answer "+cfg[1]				# DNS запрос 
       print ("shell command      :", cmd)
       while request_count <= cfg[2]:						# циклы DNS запросов пока cfg[2] раз полного совпадения ip
          sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
          for out in iter(sp.stdout.readline,b''):
             data = out.decode('utf-8').split()
             if re.match(r'((?:\d{1,3}\.?){4})', data[4]):
                print ("line 'dig' answer  :", data)
                with conn, conn.cursor() as curs:
                   query="INSERT INTO public.parsec_dns (id_count_start, id_request_name, responce_name, ttl, ipv4, redirect_port) VALUES (%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING"
                   curs.execute(query, (count_start, cfg[0], data[0], data[1], data[4], redirect_port))
                   conn.commit()
                   #print ("curs.rowcount",curs.rowcount)
                   if curs.rowcount != 0:
                      request_count = 0
                      new_ip_record = 1
                      redirect_port += 1

          if new_ip_record != 1: request_count += 1
          if cfg[2] == 0:        request_count  = 1

          print ("loop: cfg[2]       :", cfg[2])
          print ("loop: request_count:", request_count)
          print ("loop: new_ip_record:", new_ip_record)
          print ("loop: redirect_port:", redirect_port)
          if request_count < cfg[2]:
             print ("loop: wait         :", int(data[1])+5, "sec")
             sleep(int(data[1])+5)
          print ("loop: #####################################")
          new_ip_record = 0
       else:
          print ("else: cfg[2]       :", cfg[2])
          print ("else: request_count:",request_count)
          print ("else: new_ip_record:",new_ip_record)
          print ("else: redirect_port:", redirect_port)
          print ("else: #####################################")


except psycopg2.Error as e:
    if e.pgcode == '23505': print ("# 23505 ##########################################################################")
    print(e.pgcode, e.pgerror)
finally:
    if conn:
       cursor.close()
       conn.close()
       print("Соединение с PostgreSQL закрыто")