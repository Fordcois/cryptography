import sys
from pathlib import Path
import math
sys.path.append(str(Path(__file__).parent.parent))

# Analysis completed with the UK english list from Gwicks just words - file removed from repo to save space but can be redownload from the resource in the README


with open('englishwordlist.txt', 'r', encoding='latin-1') as file:
    words = [line.strip().lower() for line in file]

# Temp
words2 = [
    "apple", "breeze", "capture", "dragon", "elegant", "forest", "glow", "horizon", "ignite", "jungle",
    "kettle", "lunar", "mystic", "noble", "ocean", "parade", "quest", "ripple", "shadow", "thunder",
    "umbrella", "vivid", "whisper", "xenon", "yonder", "zephyr", "anchor", "brisk", "clover", "dusk",
    "ember", "fable", "glisten", "harbor", "island", "jester", "knight", "lilac", "meadow", "nectar",
    "opal", "prism", "quartz", "rustic", "saffron", "timber", "utopia", "velvet", "wander", "zodiac"
]


frequency_dict ={
    'letters':{},
    'bigrams':{},
    'trigrams':{},
    }

def analyse_word(word):
    word_length = len(word)
    # Letter Count
    for index,l in enumerate(word):
        letter = l.upper()
        # Letter Count
        if letter not in frequency_dict['letters']:
            frequency_dict['letters'][letter] = 1
        else: 
            frequency_dict['letters'][letter] += 1
    # bigrams
        if index <= (word_length - 2):
            bigram = word[index]+word[index+1]
            if bigram not in frequency_dict["bigrams"]:
                frequency_dict["bigrams"][bigram] = 1
            else:
                frequency_dict["bigrams"][bigram] += 1
    # Trigrams
        if index <= (word_length - 3):
            trigram = word[index]+word[index+1]+word[index+2]
            if trigram not in frequency_dict["trigrams"]:
                frequency_dict["trigrams"][trigram] = 1
            else:
                frequency_dict["trigrams"][trigram] += 1
        
        
    
    
for word in words:
    analyse_word(word)


print (frequency_dict["letters"])
# Find Total
seen_letters = sum(frequency_dict["letters"].values())
print (f' {seen_letters}')
for letter in frequency_dict["letters"]:
    print (letter)
    print (frequency_dict['letters'][letter])
    percentage = (frequency_dict['letters'][letter]/seen_letters) * 100
    frequency_dict["letters"][letter] = percentage

# 'E':'12.49',
# 'A':'8.04',
# 'T':'9.28',
# 'O':'7.64',
# 'I':'7.57',
# 'N':'7.23',
# 'R':'6.28',
# Update Each entry with percentage
print (frequency_dict['letters']['E'])
print (frequency_dict['letters']['A'])
print (frequency_dict['letters']['T'])
print (frequency_dict['letters']['O'])
print (frequency_dict['letters']['I'])
print (frequency_dict['letters']['N'])
print (frequency_dict['letters']['R'])

