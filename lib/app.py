import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

#Utilities
from utilities.txt_import import read_txt
from lib.validation_tools.check_accuracy import check_accuracy
from lib.validation_tools.valid_solution import valid_words
from utilities.CipherSymbol_class import CipherSymbol

#Encryption Functions
from lib.encrypt_functions.caesar_cipher import caesar_cipher_encrypt
from lib.encrypt_functions.keyword_cipher import keyword_cipher_encrypt


# A 	8.2% 	
# B 	1.5% 	
# C 	2.8% 	
# D 	4.3% 	
# E 	12.7% 	
# F 	2.2% 	
# G 	2.0% 	
# H 	6.1% 	
# I 	7.0% 	
# J 	0.15% 	
# K 	0.77% 	
# L 	4.0% 	
# M 	2.4% 		
# N 	6.7% 	
# O 	7.5% 		
# P 	1.9% 		
# Q 	0.095% 		
# R 	6.0% 		
# S 	6.3% 		
# T 	9.1% 		
# U 	2.8% 	
# V 	0.98% 		
# W 	2.4% 		
# X 	0.15% 		
# Y 	2.0% 		
# Z 	0.074% 	


eng_freq_dict = {1: 'E', 2: 'T', 3: 'A', 4: 'O', 5: 'I', 6: 'N', 7: 'S', 8: 'H', 9: 'R', 10: 'D', 11: 'L', 12: 'U', 13: 'C', 14: 'W', 15: 'M', 16: 'F', 17: 'Y', 18: 'G', 19: 'P', 20: 'B', 21: 'V', 22: 'K', 23: 'J', 24: 'X', 25: 'Q', 26: 'Z'}

# TODO - Rename to frequency analysis dict
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



def get_text_results(filename):
    print(f'Filename: {filename}')
    text = read_txt(f'plain_texts/{filename}.txt')
    first_cipher_text = keyword_cipher_encrypt('charlesdickens',text)
    cipher_text = caesar_cipher_encrypt(first_cipher_text,3)

    decoded = decode_with_substituion(cipher_text)
    print(decoded[0:51]) 




# Lets work on Turning cipher objects into classes

# the English letter frequency sequence as 

# the most common letter pairs as 
# "TH HE AN RE ER IN ON AT ND ST ES EN OF TE ED OR TI HI AS TO", 

# the most common doubled letters as "LL EE SS OO TT FF RR NN PP CC".





