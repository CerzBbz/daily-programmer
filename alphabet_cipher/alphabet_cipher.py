# /r/DailyProgrammer
# [2018-03-26] Challenge #355 [Easy] Alphabet Cipher
# https://www.reddit.com/r/dailyprogrammer/comments/879u8b/20180326_challenge_355_easy_alphabet_cipher/
# Author: CerzBbz

from string import ascii_lowercase


def encrypt(secret, message, decrypt=False):
    secret_values = [ascii_lowercase.find(char) for char in secret]
    message_values = [ascii_lowercase.find(char) for char in message]
    secret_values = [secret_values[i % len(secret_values)] for i in range(len(message))]
    final = []
    for index, message_value in enumerate(message_values):
        if decrypt:
            final.append(ascii_lowercase[(message_value - secret_values[index] ) % 26])
        else:
            final.append(ascii_lowercase[(secret_values[index] + message_value) % 26])
    return ''.join(final)


print('# Encrypted ')
print(encrypt('bond', 'theredfoxtrotsquietlyatmidnight'))
print(encrypt('train', 'murderontheorientexpress'))
print(encrypt('garden', 'themolessnuckintothegardenlastnight'))


print('\n# Decrypted ')
print(encrypt('cloak', 'klatrgafedvtssdwywcyty', True))
print(encrypt('python', 'pjphmfamhrcaifxifvvfmzwqtmyswst', True))
print(encrypt('moore', 'rcfpsgfspiecbcc', True))
