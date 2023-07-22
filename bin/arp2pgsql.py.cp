#!/usr/bin/env python3
import re
import json
import psycopg2
import subprocess
from psycopg2 import Error

try:
    conn = psycopg2.connect(user="dobro_dbuser",
                          password="~6331dobro",
                          host="192.168.1.90",
                          port="5432",
                          database="dobro")

    cursor = conn.cursor()
    cursor.execute("SELECT (MAX(time)+INTERVAL '0.000001 second')::timestamp FROM public.arpalert_log")
    max_time = str(cursor.fetchone()[0])
    if max_time == "None": max_time = "2000-01-01 00:00:00"
    cmd = "journalctl -f -o json -u arpalert --no-pager --since '"+max_time+"'"
    # print(cmd,'\n')
    #cmd = "journalctl -o json -u arpalert --since '2023-02-23 00:00:00'"
    #cmd = "journalctl -f -u arpalert --since '2023-01-20 00:00:00'"
    # 1677497734201256 seq=3614267, mac=00:15:5d:01:0c:03, ip=192.168.1.14, type=new, dev=eth0, vendor="Microsoft Corporation"
    sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for out in iter(sp.stdout.readline,b''):
       data = json.loads(out.decode('utf-8'))
       if re.match(r'^seq=', data['MESSAGE']):
          # print (data['MESSAGE'])
          data_log = data['__REALTIME_TIMESTAMP'][:10]+'.'+data['__REALTIME_TIMESTAMP'][10:]
          msg=re.search(r'mac=((?:[0-9a-f]{2}:?){6}), ip=((?:\d{1,3}\.?){4}),.*?vendor="(.*)"$', data['MESSAGE'])
          # print(data_log, msg[1], msg[2], msg[3])
          cursor.execute("INSERT INTO public.arpalert_log (time,mac,ipv4,vendor) VALUES (TO_TIMESTAMP(%s)+INTERVAL '3 HOURS',%s,%s,%s)",
          (data['__REALTIME_TIMESTAMP'][:10]+'.'+data['__REALTIME_TIMESTAMP'][10:], msg[1], msg[2], msg[3]))
          conn.commit()


except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Соединение с PostgreSQL закрыто")


