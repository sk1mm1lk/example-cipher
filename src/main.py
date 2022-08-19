#!/usr/bin/env python

# David Dudov
# 2022

import sys

PRIME = 111191111

def print_help():
    print("usage: " + sys.argv[0] + " <key> <plaintext> <e|d>")
    print("    where e = encrypt")
    print("          d = decrypt")
    return None

def encrypt(key, plaintext):
    key_length    = len(plaintext)
    string_length = len(plaintext)

    key_string = ""
    key_index = 0

    if (key_length < string_length):
        for i in range(string_length):
            key_index = i % key_length
            key_string = key_string + key[key_index]

def decrypt(key, ciphertext):
    key_length    = len(plaintext)
    string_length = len(plaintext)

    key_string = ""
    key_index = 0

    if (key_length < string_length):
        for i in range(string_length):
            key_index = i % key_length
            key_string = key_string + key[key_index]

def main():
    argc = len(sys.argv)
    
    if (argc == 4):
        print_help()
        return None

    key = sys.argv[1]
    plaintext = sys.argv[2]

    if (argv[3] == "e"):
        ciphertext = encrypt(key, plaintext)

        print("===== CIPHERTEXT =====")
        print(ciphertext)
        print("===== CIPHERTEXT =====")
    elif (argv[3] == "d"):
        plaintext = decrypt(key, plaintext)

        print("===== PLAINTEXT =====")
        print(plaintext)
        print("===== PLAINTEXT =====")
    else:
        ciphertext = encrypt(key, plaintext)

        print("===== CIPHERTEXT =====")
        print(ciphertext)
        print("===== CIPHERTEXT =====")

        plaintext = decrypt(key, plaintext)

        print("===== PLAINTEXT =====")
        print(plaintext)
        print("===== PLAINTEXT =====")

if (__name__ == "__main__"):
    main()
