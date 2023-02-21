import re

def reader(filename):

    regexp = r'ip=(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}),'

    with open(filename) as f:
        log = f.read()

        ip_list = re.findall(regexp, log)
    print(log)
    print(ip_list)


if __name__ == "__main__":
    reader('arpalert.log')