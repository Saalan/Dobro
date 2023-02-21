import re

def reader(filename):
    with open(filename) as f:
        log = f.read()
    print(log)


if __name__ == "__main__":
    reader ('arpalert.log')