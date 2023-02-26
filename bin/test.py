#!/usr/bin/env python3
import subprocess
import json
import re
import psycopg2
from psycopg2 import Error

try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user="dobro_dbuser",
                                  password="~6331dobro",
                                  host="192.168.1.90",
                                  port="5432",
                                  database="dobro")

    cursor = connection.cursor()
#    print(connection.get_dsn_parameters(), "\n")
#    cursor.execute("SELECT extract(epoch from MAX(time)) AS last_time FROM public.arpalert_log;")
    cursor.execute("SELECT time::timestamp AS ZZZ FROM public.arpalert_log;")


#UPDATE "public"."arpalert_log" SET "time"=to_timestamp(1653159187.197742) WHERE "id"=1;
#SELECT extract(epoch from MAX(time)) AS time FROM public.arpalert_log; */
#SELECT TIME::timestamp FROM public.arpalert_log; 


    record = cursor.fetchone()
    print(record, "\n")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")


cmd = "journalctl -o json -u arpalert --no-pager --since '2023-02-23 00:00:00'"
#cmd = "journalctl -f -u arpalert --since '2023-01-20 00:00:00'"
#cmd = "tail -f aaa.txt"

sp = subprocess.Popen(cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

for out in iter(sp.stdout.readline,b''):
    data = json.loads(out.decode('utf-8'))
    if re.match(r'^seq=', data['MESSAGE']):
       print(
          data['__REALTIME_TIMESTAMP'],
          data['MESSAGE']
       )
#       mac = re.findall(r'mac=((?:[0-9a-f]{2}:?){6})', data['MESSAGE'])
#       ip  = re.findall(r'ip=((?:\d{1,3}\.?){4})', data['MESSAGE'])
#       vnd = re.findall(r'vendor="(.*)?"$', data['MESSAGE'])
#       print(mac,ip,vnd)
       msg=re.search(r'mac=((?:[0-9a-f]{2}:?){6}), ip=((?:\d{1,3}\.?){4}),.*?vendor="(.*)"$', data['MESSAGE'])
       print(msg[1], msg[2], msg[3])
