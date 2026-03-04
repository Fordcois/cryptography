import string
import math

class CipherSymbol:
    def __init__(self,character):
        self.character = character
        self.solved = False
        self.letter_confidence = {letter: 0.0 for letter in string.ascii_uppercase}
        self.single_frequency_mapping = {
'E': 12.49,
'A':8.04,
'T':9.28,
'O':7.64,
'I':7.57,
'N':7.23,
'R':6.28,
'S':6.51,
'H':5.05,
'L':4.07,
'D':3.82,
'C':3.34,
'U':2.73,
'M':2.51,
'F':2.40,
'P':2.14,
'G':1.87,
'W':1.68,
'Y':1.66,
'B':1.48,
'V':1.05,
'K':0.54,
'X':0.23,
'J':0.16,
'Q':0.12,
'Z':0.09
}

    def best_guess(self,return_value_dict=False):
        most_likely_letters = {k: v for k, v in self.letter_confidence.items() if v == max(self.letter_confidence.values())}
        if return_value_dict:
            return most_likely_letters
        else:
            return list(most_likely_letters.keys())
        
    def get_letter_confidence(self,letter):
        return self.letter_confidence.get(letter,0.00)
        
    def set_confidence(self,letter,new_confidence_value):
        self.letter_confidence[letter]=new_confidence_value
    
    def calculate_likelyhood_single_letter(self,cipher_length,letter,seen_frequency):

        observed_frequency = seen_frequency / 100.0
        expected_frequency = self.single_frequency_mapping[letter] / 100.0

        sigma = math.sqrt((expected_frequency * (1 - expected_frequency)) / cipher_length)
        z_score = (observed_frequency - expected_frequency) / sigma

        likelihood = math.exp(- (z_score ** 2) / 2)
    
        print(f"Letter: {letter}, Observed: {observed_frequency:.4f}, Expected: {expected_frequency:.4f}, Sigma: {sigma:.4f}, Z: {z_score:.2f}, Likelihood: {likelihood:.4f}")
    
        return likelihood
    
    def calculate_all_letters(self, cipher_length: int, letter_seen_dict: dict[str, float]) -> dict[str, float]:
        output_dict: dict[str, float] = {}
        for letter, seen_frequency in letter_seen_dict.items():
            output_dict[letter] = self.calculate_likelyhood_single_letter(cipher_length, letter, seen_frequency)

        print(output_dict)
        return output_dict

        

    


    




    def __str__(self):
        return str(self.best_guess())
    
    

# # Example usage
# H=CipherSymbol('H')
# H.calculate_likelyhood_single_letter(10000,'E',0.49)
# test_dict = {'A':15.6,'B':9.6,'C':2.8}
# H.calculate_all_letters(200,test_dict)
