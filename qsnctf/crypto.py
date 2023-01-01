import json


def caesar_encrypt(text, shift):
    # 凯撒加密 （重新写的）
    ciphertext = ''
    for p in text:
        if p.islower():
            ciphertext += chr(ord('a') + (ord(p) - ord('a') + shift) % 26)
        elif p.isupper():
            ciphertext += chr(ord('A') + (ord(p) - ord('Z') + shift) % 26)
        else:
            ciphertext += p
    return ciphertext


def caesar_decrypt(text, shift):
    # 凯撒解密 （一样，重新写的）
    ciphertext = ''
    for p in text:
        if p.islower():
            ciphertext += chr(ord('a') + (ord(p) - ord('a') - shift) % 26)
        elif p.isupper():
            ciphertext += chr(ord('A') + (ord(p) - ord('Z') - shift) % 26)
        else:
            ciphertext += p
    return ciphertext


def caesar_decrypt_cracking(ciphertext):
    # 凯撒解密爆破，返回值为列表
    results = {
        '1': '', '2': '', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '', '9': '', '10': '', '11': '', '12': '',
        '13': '', '14': '', '15': '', '16': '', '17': '', '18': '', '19': '', '20': '', '21': '', '22': '', '23': '',
        '24': '', '25': ''
    }
    for i in range(1, 26):
        plaintext = caesar_decrypt(ciphertext, i)
        results[str(i)] = plaintext
    return json.dumps(results)


def caesar_encrypt_cracking(ciphertext):
    # 凯撒解密爆破，返回值为列表
    results = {
        '1': '', '2': '', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '', '9': '', '10': '', '11': '', '12': '',
        '13': '', '14': '', '15': '', '16': '', '17': '', '18': '', '19': '', '20': '', '21': '', '22': '', '23': '',
        '24': '', '25': ''
    }
    for i in range(1, 26):
        plaintext = caesar_encrypt(ciphertext,i)
        results[str(i)] = plaintext
    return json.dumps(results)


def bacon_encrypt(string):
    # 培根密码加密
    bacon = {'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB',
             'E': 'AABAA', 'F': 'AABAB', 'G': 'AABBA', 'H': 'AABBB',
             'I': 'ABAAA', 'J': 'ABAAB', 'K': 'ABABA', 'L': 'ABABB',
             'M': 'ABBAA', 'N': 'ABBAB', 'O': 'ABBBA', 'P': 'ABBBB',
             'Q': 'BAAAA', 'R': 'BAAAB', 'S': 'BAABA', 'T': 'BAABB',
             'U': 'BABAA', 'V': 'BABAB', 'W': 'BABBA', 'X': 'BABBB',
             'Y': 'BBAAA', 'Z': 'BBAAB', 'a': 'AAAAA', 'b': 'AAAAB',
             'c': 'AAABA', 'd': 'AAABB', 'e': 'AABAA', 'f': 'AABAB',
             'g': 'AABBA', 'h': 'AABBB', 'i': 'ABAAA', 'j': 'ABAAB',
             'k': 'ABABA', 'l': 'ABABB', 'm': 'ABBAA', 'n': 'ABBAB',
             'o': 'ABBBA', 'p': 'ABBBB', 'q': 'BAAAA', 'r': 'BAAAB',
             's': 'BAABA', 't': 'BAABB', 'u': 'BABAA', 'v': 'BABAB',
             'w': 'BABBA', 'x': 'BABBB', 'y': 'BBAAA', 'z': 'BBAAB'}
    encoded_string = ''
    for char in string:
        char = char.upper()
        if char in bacon:
            encoded_string += bacon[char]
    return encoded_string


def bacon_decrypt(string):
    bacon = {'AAAAA': 'A', 'AAAAB': 'B', 'AAABA': 'C', 'AAABB': 'D',
             'AABAA': 'E', 'AABAB': 'F', 'AABBA': 'G', 'AABBB': 'H',
             'ABAAA': 'I', 'ABAAB': 'J', 'ABABA': 'K', 'ABABB': 'L',
             'ABBAA': 'M', 'ABBAB': 'N', 'ABBBA': 'O', 'ABBBB': 'P',
             'BAAAA': 'Q', 'BAAAB': 'R', 'BAABA': 'S', 'BAABB': 'T',
             'BABAA': 'U', 'BABAB': 'V', 'BABBA': 'W', 'BABBB': 'X',
             'BBAAA': 'Y', 'BBAAB': 'Z'}
    decoded_string = ''
    for i in range(0, len(string), 5):
        chunk = string[i:i+5]
        if chunk in bacon:
            decoded_string += bacon[chunk]
    return decoded_string