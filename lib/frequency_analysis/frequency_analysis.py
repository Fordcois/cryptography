import sys
from pathlib import Path
import math
sys.path.append(str(Path(__file__).parent.parent))

# Analysis completed with the UK english list from Gwicks just words - file removed from repo to save space but can be redownload from the resource in the README


with open('englishwordlist.txt', 'r', encoding='latin-1') as file:
    words = [line.strip().lower() for line in file]

# Temp
# words = [
#     "apple", "breeze", "capture", "dragon", "elegant", "forest", "glow", "horizon", "ignite", "jungle",
#     "kettle", "lunar", "mystic", "noble", "ocean", "parade", "quest", "ripple", "shadow", "thunder",
#     "umbrella", "vivid", "whisper", "xenon", "yonder", "zephyr", "anchor", "brisk", "clover", "dusk",
#     "ember", "fable", "glisten", "harbor", "island", "jester", "knight", "lilac", "meadow", "nectar",
#     "opal", "prism", "quartz", "rustic", "saffron", "timber", "utopia", "velvet", "wander", "zodiac"
# ]


frequency_dict ={
    'letters':{},
    'bigrams':{},
    'trigrams':{},
    }

def analyse_word(word):
    word_length = len(word)
    # Letter Count
    for index,letter in enumerate(word):
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
