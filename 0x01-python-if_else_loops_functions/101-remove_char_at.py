#!/usr/bin/python3
def remove_char_at(str, n):
    for i in str:
        if str.index(i) == n:
            str2 = str.replace(i, "")
            return str2
        else:
            pass
    return str
