#!/usr/bin/python3
import string

for a in string.ascii_lowercase:
    if a == 'q' or a == 'e':
        continue
    print("{}".format(a), end="")
