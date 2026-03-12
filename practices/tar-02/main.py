# Vigenère con alfabeto restringido A-Q (17 letras)
# A = 0, B = 1, ..., Q = 16
ALPHABET_START = ord('A')
ALPHABET_SIZE = 17
# 65
# A-Q
def _pad_key(text, key):
    padded_key = ''
    i = 0
    for char in text:
        if char.isalpha():
            padded_key += key[i % len(key)]
            i += 1
        else:
            padded_key += ' '
    return padded_key
def _cifrar_decifrar_char(text_char, key_char, mode='cifrar'):
    if text_char.isalpha():
        base = ord('A')
        m = ord(text_char.upper()) - base
        k = ord(key_char.upper()) - base
        if mode == 'cifrar':
            c = (m + k) % ALPHABET_SIZE
        else:
            c = (m - k + ALPHABET_SIZE) % ALPHABET_SIZE
        return chr(c + base)
    return text_char
def cifrar(text, key):
    result = ''
    padded_key = _pad_key(text, key)
    for t_char, k_char in zip(text, padded_key):
        result += _cifrar_decifrar_char(t_char, k_char)
    return result
def descifrar(text, key):
    result = ''
    padded_key = _pad_key(text, key)
    for t_char, k_char in zip(text, padded_key):
        result += _cifrar_decifrar_char(t_char, k_char, mode='decrypt')
    return result