#!/usr/bin/python3

from sys import argv
i = len(argv) - 1

if i == 0:
    print("0")
else:
    j = int(0)
    while i > 0:
        j += int(argv[i])
        i -= 1
    print("{}".format(j))

if __name__ == "__main__":
    pass
