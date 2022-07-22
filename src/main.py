#!/usr/bin/env python

# David Dudov
# 2022

# SimpleCryptTool

import sys
from os.path import exists

def print_help():
    print("usage: " + sys.argv[0] + " <key/file> <plaintext/file> [other files]")
    return None

def encrypt(key_string, plaintext):
    # TODO
    return "TODO"

def encrypt_file(key_string, filename):
    if (exists(filename)):
        f = open(filename, "r")
        plaintext = f.read()
        f.close()

        ciphertext = encrypt(key_string, plaintext)
        return ciphertext
    else:
        ciphertext = encrypt(key_string, filename)
        return ciphertext

def main():
    argc = len(sys.argv)
    
    if (argc < 3):
        print_help()
        return None

    key = sys.argv[1]
    files = sys.argv[2:]

    is_key_file = exists(key)

    if (is_key_file):
        f = open(key, "r")
        key_string = f.read()
        f.close()
    else:
        key_string = key

    for file in files:
        if (exists(file)):
            ciphertext = encrypt_file(key_string, file)
            f = open((file + ".sct"), "w")
            f.write(ciphertext)
            f.close()
        else:
            ciphertext = encrypt(key_string, file)
            print("===== CIPHERTEXT =====")
            print(ciphertext)
            print("===== CIPHERTEXT =====")

if (__name__ == "__main__"):
    main()
