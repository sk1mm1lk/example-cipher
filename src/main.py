#!/usr/bin/env python

# David Dudov
# 2022

import sys
import base64

PRIME = 111191111
# CHAR = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
CHAR = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
N_CHAR = len(CHAR)

def print_help():
    print("usage: " + sys.argv[0] + " <key> <plaintext>")
    return None

def get_char(index):
    return CHAR[index]

def get_index(char):
    for i in range(N_CHAR):
        if char == CHAR[i]:
            return i

    # Shouldn't happen
    print("Character not in character set")
    exit()

def encrypt(key, plaintext):
    key_length    = len(key)
    plaintext = base64.b64encode(plaintext.encode('ascii')).decode().replace("=", "")
    string_length = len(plaintext)

    ciphertext = ""

    for index in range(string_length):
        ch     = get_index(plaintext[index])
        ch_key = get_index(key[index % key_length])

        addition = PRIME * ch_key

        ciphertext += get_char((ch + addition) % N_CHAR)

    return ciphertext


def decrypt(key, ciphertext):
    key_length    = len(key)
    string_length = len(ciphertext)

    plaintext = ""

    for index in range(string_length):
        ch     = get_index(ciphertext[index])
        ch_key = get_index(key[index % key_length])

        subtraction = PRIME * ch_key

        plaintext += get_char((ch - subtraction) % N_CHAR)

    plaintext += "=="
    plaintext = base64.b64decode(plaintext.encode('ascii')).decode()
    return plaintext

def main():
    argc = len(sys.argv)
    
    if (argc != 4):
        print_help()
        return None

    key = sys.argv[1]
    plaintext = sys.argv[2]
    mode = sys.argv[3]

    if ("e" in list(mode)):
        ciphertext = encrypt(key, plaintext)

        print("===== CIPHERTEXT =====")
        print(ciphertext)
        print("===== CIPHERTEXT =====")
    
    else:
        plaintext = decrypt(key, plaintext)
        print("===== PLAINTEXT =====")
        print(plaintext)
        print("===== PLAINTEXT =====")
if (__name__ == "__main__"):
    main()
