#!/usr/bin/python3
def read_file(filename=""):
    """fonction that read _file """
    with open(filename, encoding='utf-8') as a_file:
        print(a_file.read(), end="")
