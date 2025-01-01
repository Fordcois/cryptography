import string
class CipherSymbol:
    def __init__(self, symbol):
        self.symbol = symbol  
        self.solved = False 
        self.plaintext_letter = None
        self.likelihoods = {letter: 0.03846153846 for letter in string.ascii_uppercase} # Equal 1/26 Chance

    def most_likely(self):
        max_likelihood = max(self.likelihoods.values())
        return [letter for letter, likelihood in self.likelihoods.items() if likelihood == max_likelihood]
    
    def best_guess(self):
        return max(self.likelihoods, key=self.likelihoods.get)
    
    def __repr__(self):
        if self.solved:
            return f"{self.plaintext_letter}!"
        else:
            return f"{self.symbol}?"
