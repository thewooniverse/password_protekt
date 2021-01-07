#! /usr/bin/python

# wrapper.py for Password Protector - is a script for using the decryption, encryption logic to process files.
# usage:
#   wrapper.py lock filename - locks filename to produce a filename_locked
#   wrapper.py dlock filename - locks filename but also deleted
#   wrapper.py unlock filename - unlocks a filename to product a filename



import os, sys, shutil
import pyperclip
from decryption import combination_decrypt as decrypt
from encryption import combination_encrypt as encrypt



functionality = sys.argv[1] # lock, dlock, unlock etc...
filename = sys.argv[2] # filename


# user facing to accept key_str and key_num
usr_str_key =  input("Please type in your key word:\n")
usr_num_key = input("Please type in your key number:\n")

usr_block_size = input("Please enter your block size if you specified one, leave blank for default:\n")
if not usr_block_size:
    usr_block_size = 3
else:
    usr_block_size = int(usr_block_size)

usr_rotation = input("Please enter your rotation key specified one, leave blank for default:\n")
if not usr_rotation:
    usr_rotation = 1
else:
    usr_rotation = int(usr_rotation)





if functionality == "lock" or functionality == "dlock":
    with open(filename, 'r') as rf:
        with open("locked_" + filename, 'w') as wf:
            for line in rf.readlines():
                cipher_line = encrypt(line, usr_str_key, usr_num_key, usr_block_size, usr_rotation)
                wf.write(cipher_line + '\n')

    print(f'{filename} is locked!!\nRemember to write down your key num and key word!!')


# if it is to unlock, read the filename, and create the filename without locked_ in fron.
if functionality == "unlock":
    with open(filename, 'r') as rf:
        with open(filename.strip('locked_'), 'w') as wf:
            for line in rf.readlines():
                plaintext_line = decrypt(line, usr_str_key, usr_num_key, usr_block_size, usr_rotation)
                wf.write(plaintext_line + '\n')

    print(f'{filename} is now unlocked, if it looks like jumbles then try again with the correct key_num and key word!!')

















