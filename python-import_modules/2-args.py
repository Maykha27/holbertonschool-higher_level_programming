#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len = len(argv)
    print("{:d}{:s}{:s}".format(len - 1,
                                 "argument" if len <= 2 else "arguments",
                                 "." if len == 1 else ":"))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))
