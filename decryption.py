import string


def vigenere_decrypt(ciphertext, key_word, key_num):
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase
    numbers = string.digits

    result = ""

    for i in list(range(len(ciphertext))):

        char = plaintext[i]

        if char.isalpha():

            # determine which character of key_word will be used and find out its alphabet position
            key_idx = i % len(key_word)
            key_char = key_word[key_idx]
            key_pos = alphabet_lower.find(key_char.lower())

            # find out which index the ciphertext is in the alphabet
            char_pos = alphabet_lower.find(char.lower())

            new_pos = char_pos - key_pos

            if new_pos < 0:
                new_pos += 26
