#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0
    n = len(sys.argv) - 1
    for i in range(n):
        add = add + int(sys.argv[i + 1])
    print("{}".format(add))
