#! /usr/bin/python
# wrapper.py for Password Protector - is a script for using the decryption, encryption logic to process files.
# usage:
#   wrapper.py lock filename - locks filename to produce a locked_filename
#   wrapper.py unlock filename - unlocks a filename to product a filename
#   wrapper.py lock filename D - locks filename but also deleted

import os, sys, pyperclip, shutil
from decryption import combination_decrypt as decrypt
from encryption import combination_encrypt as encrypt


# read sys argv


# open and delete.


































### testing ###
# Basic test for functionality after import
# test_str_key = "FUNFUNRUNRUN"
# test_num_key = "023654"
# test_pt = "yooow1233hatisthepassword????"
# print(test_pt)
# tst_ct = (encrypt(test_pt, test_str_key, test_num_key, 3, 2))
# print(tst_ct)
# print(decrypt(tst_ct, test_str_key, test_num_key, 3, 2))


