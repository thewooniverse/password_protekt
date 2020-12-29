# Key Chain

A python program for encrypting, accessing and editing a text file containing any secretive info.
- In my case, it is used to hide vague hints for different password combinations I use for different websites.

In the current version encryption is done using a combination of Vigenere + Permutation box cipher.

The program is case sensitive, and retains cases in the encrypted text;
The program encrypts alphanumeric characters and the permutation box is applied to all characters giving some security to symbols and spaces.

It can be executed through the terminal, and prompts the user for a key word and key number to encrypt a filename.txt file using the encryption algorithms;
The output of the software is a cipher_filename.txt file which contains the encrypted version of the text from filename.txt.
This is your encrypted file, which you can unlock into the correct plaintext with the correct key word and key number.


Arguments;
-U : Unlock keychain
-L : Lock a new txt file with cipher and new password.






### Future developments

- QT / GUI implementation
- New data structure instead of txt

    Future development
    -E : edit function
    -C : Copy, unencrypts a given password and copies it to clipboard.


#### TO DO LIST

3. Wrapper Protekk
4. Wrapper Unlock
5. PasswordProtekt.py
6. Add more cipher logic!!
7. Can we update passwords without revealing?
- New data types, using python dictionary potentially.


Testing


Done;
1. Implement Vigenere Encrypt and Decrypt
2. Implement Permutation Encrypt and Decrypt

