import random

def caesar_cipher_encrypt(text,shift=None,):
    result = []

    if shift is None:
        shift = random.randint(1, 25)  # Random shift between 1 and 25

    result = []
    for char in text:
        if char.isalpha():  # Process only alphabetic characters
            # Determine base (A/a) for correct ASCII conversion
            base = ord('A') if char.isupper() else ord('a')
            # Apply the shift and wrap within alphabet bounds
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)
        else:
            # Non-alphabetic characters remain unchanged
            result.append(char)
    
    return ''.join(result)
