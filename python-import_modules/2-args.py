#!/usr/bin/python3
from sys import argv
i = len(argv) - 1

if i == 1:
    print("{} argument:".format(i))
elif i == 0:
    print("{} arguments.".format(i))
else:
    print("{} arguments:".format(i))

j = 0
while j < i:
    j += 1
    print("{}: {}".format(j, argv[j]))

if __name__ == "__main__":
    pass
