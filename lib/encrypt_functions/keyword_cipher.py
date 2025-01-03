def keyword_cipher_encrypt(keyword,plaintext):
    keyword = keyword.upper()
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    shifted_alphabet = ''
    substitution_key={}
    for char in keyword+alphabet:
        if char not in shifted_alphabet:
            shifted_alphabet += char
    
    for i in range (len(shifted_alphabet)):
        substitution_key[alphabet[i]] = shifted_alphabet[i]

    decoded_message=''
    for char in plaintext:
        uppercase = char.upper() == char
        if char.isalpha():
            if uppercase:
                decoded_message += substitution_key[char]
            else:
                decoded_message += substitution_key[char.upper()].lower()
        else:
            decoded_message += char
    return decoded_message






print(keyword_cipher_encrypt('keyword','plaintext'))