#!/usr/bin/python3
import hidden_4

list = dir(hidden_4)
j = len(list)
i = 0
while i < j:
    if list[i][0] == "_":
        pass
    else:
        print("{}".format(list[i]))
    i += 1

if __name__ == "__main__":
    pass
