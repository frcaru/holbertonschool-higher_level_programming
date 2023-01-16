#!/usr/bin/python3
def uppercase(str):
    strupper = ""
    for i in range(len(str)):
        if str[i] >= 'a' and str[i] <= 'z':
            strupper += chr(ord(str[i]) - 32)
        else:
            strupper += str[i]
    print("{}".format(strupper))
