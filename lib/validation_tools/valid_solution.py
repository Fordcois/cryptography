import enchant

def valid_words(decoded_text, threshold=100.00, extra_whitelist_words=[]):
    pyenchant = enchant.DictWithPWL("en_US", "whitelisted_words.txt")
    individual_words = decoded_text.split()
    correct_words = 0
    total_words = len(individual_words)
    # Add extra words to the whitelist temporarily 
    for word in extra_whitelist_words:
        pyenchant.add_to_session(word)
    
    for word in individual_words:
        # Remove punctuation from the word
        word = ''.join(char for char in word if char.isalnum())
        if pyenchant.check(word):
            correct_words += 1
    
    accuracy = (correct_words / total_words) * 100
    # print (f'Threshold is {threshold:.2f}%')
    # print (f'Accuracy is {accuracy:.2f}% with {correct_words}/{total_words} words')
    
    return accuracy >= threshold
    
