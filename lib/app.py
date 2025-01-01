import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
#Utilities
from utilities.txt_import import read_txt
from utilities.check_accuracy import check_accuracy

#Encryption Functions
from lib.encrypt_functions.caesar_cipher import caesar_cipher_encrypt

eng_freq_dict = {1: 'E', 2: 'T', 3: 'A', 4: 'O', 5: 'N', 6: 'R', 7: 'I', 8: 'S', 9: 'H', 10: 'D', 11: 'L', 12: 'F', 13: 'C', 14: 'M', 15: 'U', 16: 'G', 17: 'Y', 18: 'P', 19: 'W', 20: 'B', 21: 'V', 22: 'K', 23: 'J', 24: 'X', 25: 'Z', 26: 'Q'}

def create_substitution_dict(text):
    frequency_dict = {}
    for letter in text:
        if letter.isalpha():
            if letter.upper() in frequency_dict:
                frequency_dict[letter.upper()] += 1
            else:
                frequency_dict[letter.upper()] = 1
        else:
            continue
    sorted_list = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)
    sub_dict = {}
    for i in range(len(sorted_list)):
        sub_dict[sorted_list[i][0]] = i+1
    return sub_dict



def decode_with_substituion(cipher_text):
    cipher_freq_dict = create_substitution_dict(cipher_text)
    print ('Cipher Frequency Dictionary')
    print (cipher_freq_dict)
    print(' ')
    print ('English Frequency Dictionary')
    print (eng_freq_dict)
    
    decoded_text = ''
    for letter in cipher_text:
        if letter.isalpha():
            uppercase = letter.upper()
            decoded_letter = eng_freq_dict[cipher_freq_dict[uppercase]]
            if letter.islower():
                decoded_text += decoded_letter.lower()
            else:
                decoded_text += decoded_letter
        else:
            decoded_text += letter
    return decoded_text

# Encrypt plain text
plain_text = read_txt('cipher_texts/a_tale_of_two_cities.txt')
cipher_text = caesar_cipher_encrypt(plain_text)


# Decode cipher text
decoded = decode_with_substituion(cipher_text)
check_accuracy(plain_text,decoded)



# the English letter frequency sequence as 
# ETAONRISHDLFCMUGYPWBVKJXZQ' 
# the most common letter pairs as 
# "TH HE AN RE ER IN ON AT ND ST ES EN OF TE ED OR TI HI AS TO", 

# the most common doubled letters as "LL EE SS OO TT FF RR NN PP CC".

