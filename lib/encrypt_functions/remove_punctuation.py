import unicodedata
import string

def remove_punctuation_and_normalise(text):
    output_string = ""
    for char in text:
        # Normalize character (remove accents)
        normalized_char = unicodedata.normalize('NFKD', char)
        # Remove diacritics and convert to uppercase
        stripped_char = ''.join(c for c in normalized_char if not unicodedata.combining(c)).upper()
        # Remove punctuation
        if stripped_char not in string.punctuation:
            output_string += stripped_char

    return output_string