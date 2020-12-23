import string


test_str_key = "FUN"
test_num_key = "133"
test_pt = "RUN"


# later it all needs to be added as str(input())


def vigenere_encrypt(key_word, key_num, plaintext):
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase
    numbers = string.digits

    result = ""

    for i in list(range(len(plaintext))):

        char = plaintext[i]

        if char.isalpha():  # check if it is alphabet.

            # check which character of the key_word will be used to encrypt this letter
            key_idx = i % len(key_word)
            key_char = key_word[key_idx]
            # find out at which index, the key_char is in the alphabet
            key_pos = alphabet_lower.find(key_char.lower())
            # find out at which index, the char is in the alphabet
            char_pos = alphabet_lower.find(char.lower())
            new_pos = (key_pos + char_pos) % 26

            # adding to resul with case sensitivity
            if char.islower():
                result += alphabet_lower[new_pos]

            elif char.isupper():
                result += alphabet_upper[new_pos]

        # check if it is a digit
        elif char.isdigit():
            # check which digit of the key_num will be used to encrypt this num
            key_idx = i % len(key_num)
            key_digit = key_num[key_idx]

            new_digit = (int(char) + int(key_digit)) % 10
            result += str(new_digit)

        # otherwise it is whitspace or symbols
        else:
            result += char

    return result


plain = "111123333455556ABC"


def permuntation_encrypt(plaintext, block_size=3, rotation=1):
    result = ''

    for i in list(range(len(plaintext))):
        # if we find the beginning of the block
        if i % block_size == 0:
            plain_block = plaintext[i:(i + block_size)]
            if len(plain_block) == block_size:
                cipher_block = plain_block[-rotation:] + \
                    plain_block[:block_size - rotation]

                result += cipher_block

            else:
                result += plaintext[i:]

    return result


print(permuntation_encrypt(plain, 5, 3))

print(vigenere_encrypt(test_str_key, test_num_key, test_pt))
