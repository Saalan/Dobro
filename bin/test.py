#!/usr/bin/env python3
import re
import subprocess

cmd = "journalctl -f -u arpalert --since '2023-01-20 00:00:00'"
#cmd = "tail -f aaa.txt"

#Feb 21 20:55:11 dbr-ubnt arpalert[913]: seq=1507410, mac=00:15:5d:01:0c:3c, ip=192.168.1.91, type=new, dev=eth0, vendor="Microsoft Corporation"
#Feb 08 14:53:43 dbr-ubnt arpalert[438121]: seq=3263636, mac=30:85:a9:96:5b:dc, ip=192.168.1.254, reference=169.254.51.111, type=ip_change, dev=eth0, vendor="ASUSTek COMPUTER INC."


def pars_log(line):
    return (param)

sp = subprocess.Popen(cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

for out in iter(sp.stdout.readline,b''):
    print(out)
#    date=re.findall(r"\[\s*(\d+/\D+/.*?)\]", sp.stdout)
    print(type(out))




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
