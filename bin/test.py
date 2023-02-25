#!/usr/bin/env python3
import subprocess
import json
import re

cmd = "journalctl -f -o json -u arpalert --no-pager --since '2021-02-20 00:00:00'"
#cmd = "journalctl -f -u arpalert --since '2023-01-20 00:00:00'"
#cmd = "tail -f aaa.txt"

sp = subprocess.Popen(cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

for out in iter(sp.stdout.readline,b''):
    data = json.loads(out.decode('utf-8'))
#     print (type(out))
#    date=re.findall(r"^b'(\S{3})", line)
#    print(date,line)
#    print(data)
#    if data['SYSLOG_IDENTIFIER': 'arpalert']
#    if re.match(r'^(seq=.*)', data['MESSAGE']):

    print(
       data['__REALTIME_TIMESTAMP'],
       data['MESSAGE']
    )
    if re.match(r'^seq=', data['MESSAGE']):
       msg = re.findall(r'mac=((?:[0-9a-f]{2}:|){6})', data['MESSAGE'])
       print(msg)


#   
#       msg=dict()
#      #  print(type(data['MESSAGE']))
#       line=str(data['MESSAGE'])
#       print(line.split(', '))
#       cut_line=data['MESSAGE'].split(r'"')
#       for i in cut_line:
#          print(
#          if ( % 2) == 0:
#          else
#          pair=i.split('=')
#          print(pair[1])
#          msg[pair[0]]=pair[1]
#          a=i[:i.index('=')]
#          b=i[i.index('=')+1:]
#          msg[a]=b
#       print (msg)

#    if re.match(r'(seq=)', data['MESSAGE']):
#       print(
#         data['__REALTIME_TIMESTAMP'],
#         data['MESSAGE']
#       )
#       msg = re.findall(r'mac=((?:[0-9a-f]{2}:){5}[0-9a-f]{2}),\sip=((?:\d{1,3}\.){3}\d{1,3}).*vendor="(?.*)"$', data['MESSAGE'])
#       msg = re.findall(r'mac=((?:[0-9a-f]{2}(?::|)){6}', data['MESSAGE'])



#    message = dict((a, b)
#       for a, b in (pair.split('=') 
#          for pair in data['MESSAGE'].split(',')))

#    for pair in iter(data['MESSAGE'].split(','),'=')
#	   print(type(data['MESSAGE'].split(',')))
#	print(pair)

#import re

#for line in stdin:
#    print(line)


#def reader(filename):
#    regexp = r'ip=(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}),'
#
#    with open(filename) as f:
#        log = f.read()
#
#        ip_list = re.findall(regexp, log)
#    print(log)
#    print(ip_list)


#if __name__ == "__main__":
#    main()
#    reader('arpalert.log')
#    reader('journalctl - f - u arpalert --since '2023-01-30 00:00:00'')
