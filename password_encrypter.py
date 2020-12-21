

import string

test_key = "FUN"

# The cipher needs to deal with alphanumerics
# As well as being case sensitive


def vigenere_encrypt(key_word, plaintext):
    alphabet = string.ascii_lowercase

    result = ""

    for i in list(range(len(plaintext))):


        if plaintext[i].isalpha(): #check if alphanumeric.

            key_idx = i % len(key)
            key_pos = alphabet.find(key[kew_idx].lower())
            pt_pos = alphabet.find(pt[i].lower())


        elif plaintext.[i].isnum(): # check if num


        else: # the char at this index is a symbol or a whitespace
            result += plaintext[i]


def permuntation_encrypt:
    pass
