#!/usr/bin/python3
def write_file(filename="", text=""):
    """function that writes a string to text file(UTF8)"""
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
