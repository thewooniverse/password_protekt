# password_protekt

Simple python implementation of encrypting your password with python and a implementation of Vigenere + Permutation box cipher.


Protekk.py will allow you to pass a .txt or .md file - it will prompt you to input a key word and a key number;
These are your two private keys which will later be used for decryption.
It will execute the encryption logic in encryptor.py and produce a new .txt file with the encrypted password.

Unlock.py will allow you to pass a .txt file of ciphertext - and prompt you to input a key word and a key number;
It will execute the decryption logic in decryptor.py, and produce a new .txt file - which if the keys were correct would result in the
plaintext version of the password.


- The program is Case sensitive, and retains cases in encrypted password.
- The vigenere will encrypt numbers as well as letters.



### Future developments

- QT / GUI implementation




#### TO DO LIST

3. Wrapper Protekk
4. Wrapper Unlock
5. PasswordProtekt.py
6. Add more cipher logic!!

Testing


Done;
1. Implement Vigenere Encrypt and Decrypt
2. Implement Permutation Encrypt and Decrypt

