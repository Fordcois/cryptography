from CipherSymbolClass import CipherSymbol


class Cipher:
    def __init__(self,cipher_text):
        self.cipher_text:str = cipher_text
        self.symbols:dict[str,CipherSymbol] ={}
        self.cipher_length: int =len(cipher_text)
    
    def details(self):
        print(f'Cipher Length: {self.cipher_length} - Unique Symbols: {len(self.symbols)}')
            
    def analyse_frequency(self):

        for char in self.cipher_text:
            if char in self.symbols:
                self.symbols[char].increase_appearances()
            else:
                self.symbols[char] = CipherSymbol(char)


    def print_ciphertext(self):
        print(self.cipher_text)
    def return_symbols(self):
        print (self.symbols)

    def best_guess(self):
        pass
    
    def __str__(self):
        return str(self.best_guess())
    
    
