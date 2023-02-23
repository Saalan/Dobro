import re
#import subprocess


#arg = ["journalctl","-f","-u arpalert","--since '2023-02-20 00:00:00'"]
#proccess = subprocess.Popen(arg, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#while True:
#    line = proccess.stdout.readline()
#    print(line)





#arp_log = os.system('journalctl -f -u arpalert --since \'2023-02-20 00:00:00\'')
#s = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
#arp_log = os.system('tail -f aaa.txt')
#for line in arp_log:
#    out = re.findall(s, line)
#    print (line)
#    print (out)

import subprocess
f = subprocess.Popen(["journalctl","-f -u arpalert --since '2023-02-22 00:00:00'"],\
#f = subprocess.Popen(['tail','-f aaa.txt'],\
    stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#while True:
#    line = f.stdout.readline()
#    print(line)
data = f.communicate()
for line in data:
    print(line)



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
