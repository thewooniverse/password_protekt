# Key Chain

A python program for encrypting, accessing and editing a plaintext file containing any secretive info.
- In my case, it is used to hide vague hints for different password combinations I use for different websites.

In the current version encryption is done using a combination of Vigenere + Permutation box cipher.

The program is case sensitive, and retains cases in the encrypted text, but symbols are not.
The permutation box is applied to all characters giving some security to symbols in the password by mixing the order around.

It can be executed through the terminal, and prompts the user for a key word and key number to encrypt a filename.txt file using the encryption algorithms;
The output of the software is a cipher_filename.txt file which contains the encrypted version of the text from filename.txt.
This is your encrypted file, which you can unlock into the correct plaintext with the correct key word and key number.


Usage:
wrapper.py -lock filename : Locks keychain
wrapper.py -lock filename D : Locks keychain, deletes original pt file
wrapper.py -unlock filename : Unlocks ciphertext keychain to original plaintext with given encryption keys, if correct, correct pt is generated.






### Future developments

- QT / GUI implementation
- New data structure instead of txt

New usage;
-update filename A : adds new lines


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

