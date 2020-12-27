import string

ct = "dibtq5256yugnmgmycrmfniei????"
test_str_key = "FUNFUNRUNRUN"
test_num_key = "023654"

tst_ct = "112113343355655CDEABF"


comb_ciphered = "btdi25q5ug6ygmnmrmyciefn??i??"


def vigenere_decrypt(ciphertext, key_word, key_num):
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase
    numbers = string.digits

    result = ""

    for i in list(range(len(ciphertext))):

        char = ciphertext[i]

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

            if char.islower():
                result += alphabet_lower[new_pos]

            elif char.isupper():
                result += alphabet_upper[new_pos]

        elif char.isdigit():

            key_idx = i % len(key_num)
            key_digit = key_num[key_idx]

            new_digit = (int(char) - int(key_digit))

            if new_digit < 0:
                new_digit += 10

            result += str(new_digit)

        else:
            result += char

    return result


# print(vigenere_decrypt(ct, test_str_key, test_num_key))


def permutation_decrypt(ciphertext, block_size, rotation):
    result = ""

    for i in list(range(len(ciphertext))):
        # if we find the beginning of the block
        if i % block_size == 0:
            cipher_block = ciphertext[i:(i + block_size)]

            # make sure that we are not rotating blocks that are smaller
            if len(cipher_block) == block_size:
                plain_block = cipher_block[rotation:] + cipher_block[:rotation]
                result += plain_block

            else:
                result += ciphertext[i:]

    return result


# print(permutation_decrypt(tst_ct, 5, 3))


def combination_decrypt(ciphertext, key_word, key_num, block_size, rotation):
    perm_decrypted = permutation_decrypt(ciphertext, block_size, rotation)
    vig_decrypted = vigenere_decrypt(perm_decrypted, key_word, key_num)

    return vig_decrypted


# print(combination_decrypt(comb_ciphered, test_str_key, test_num_key, 4, 2))
