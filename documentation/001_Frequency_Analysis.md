## Caesar Ciphers

For the first steps into cryptography, i'm focusing on cracking simple substitution ciphers. Substitution ciphers involve replacing letters in the plaintext with other letters. There are several ways to achieve this, but for our initial encryption example, we’ll examine the Caesar cipher.

The Caesar cipher works by shifting the alphabet by a set number of characters and using the shifted letters as the new alphabet. For instance, if we use a shift of one:

```
ABCDE  
↓↓↓↓↓  
BCDEF  
```

And with a shift of three:

```
ABCDE  
↓↓↓↓↓  
DEFGH  
```

I’ve written a simple script to create a Caesar cipher for encrypting texts [Link to code]. The offset can be manually set as a parameter, but if none is provided, the offset will be randomised between 1 and 25 (as 26 would result in a complete cycle where A becomes A again, and an offset of 27 is equivalent to an offset of 1).

Caesar ciphers are weak because there are only 25 possible solutions. In fact, we can use the same encryption tool to decrypt them—the second encryption offset just needs to undo the first. This can be calculated as:

```
26 - original_offset = decryption_offset  
```

Since there are only 25 possible solutions, we could manually review all the options quickly enough, or we can brute-force the solution.

For example, the following code:

```python
def solve_caesar(cipher_text):  
    for i in range(1, 26):  
        decrypted_message = caesar_cipher_encrypt(cipher_text, i)  
        if valid_words(decrypted_message):  
            return decrypted_message  

print(solve_caesar('K jqrg pqdqfa hkpfu oa jkffgp oguucig'))  
```

Correctly produces the solution:  

**'I hope nobody finds my hidden message'**

### Keyword Ciphers

Keyword ciphers are a more secure form of substitution cipher that provide far more combinations than the 25 possible with a Caesar cipher. These require a keyword which is placed at the beginning of the alphabet (with duplicate letters removed). The remaining letters of the alphabet are appended after the keyword, excluding those already in it.

For example, using the keyword `KEYWORD`, we get the following new alphabet:

```
KEYWORDABCFGHIJLMNPQSTUVXZ  
↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  
ABCDEFGHIJKLMNOPQRSTUVWXYZ  
```

Offsetting the letters no longer works in the same way as with a Caesar cipher. For instance, if we use the above alphabet and shift the bottom row to align the A’s, we still don’t achieve a correct translation:

```
ABCFGHIJLMNPQSTUVXZKEYWORD  
↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  
ABCDEFGHIJKLMNOPQRSTUVWXYZ  
```

The code featured in the encryption folder features a method for encoding keyword ciphers with a simple script. [Link to code]
## Frequency Analysis

Since using a substitution cipher preserves the structure of the text, we can use clues to deduce the substitutions for each letter. Frequency Analysis examines the occurrence of symbols in the cipher text and compares these to their typical frequencies in regular English language and we should see a strong correlation between the frequency of symbols in the cipher text and the letters they represent in plain English.

Within the project files, I have extracts from several famous public domain novels to use as examples—including the first chapter of _A Tale of Two Cities_ by Charles Dickens, the first chapter of _The Great Gatsby_ by F. Scott Fitzgerald, and the first chapter of _Moby-Dick_ by Herman Melville, as well as the complete text of _Crime and Punishment_ by Dostoevsky.

Using a simple script, we can count the frequency of each letter within the text. For example, if we analyse the extract from _A Tale of Two Cities_, the top row shows the most common letters in the extract, while the bottom row represents the most common letters in English.

```
# Text Extract
ETAONRSIHDLFUWCMGYPBVKJQXZ
ETAOINSHRDLUCWMFYGPBVKJXQZ
# General English 
```

We see that 14 out of 26 letters are exact matches based solely on frequency and 22 out of 26 are either exact or just one position off.
 Running the same frequency analysis on our other extract we see that our extract from The Great Gatsby and Moby Dick also have 22 characters as either an exact match or only 1 position out of place while Crime & Punishment has 20 Characters as either an exact match or one out.

This level of accuracy remains consistent regardless of the shift used, as while individual letters change, their frequency does not. 

For example, if we encrypt the extract from A Tale of Two Cities with the keyword `CHARLESDICKENS` .... and then encrypt it with a caesar cipher offset by 3.

Our text is now fully scrambled but when we run our frequency analysis on the scrambled text, and compare this to normal english frequency we still have 14/26 correct - So when we substitute those letters our first line is revealed as :
```
Ht was tre best ou thfes, ht was tre wonst ou thfes
```

Which is definitely not perfect but arguably guessable, especially if we have some context clues about the contents of the message.

Just looking at the above line we could probably guess that 'WAS' & 'BEST' is correct. Knowing that 't' is probably correct we can swap the h's with i's .. and so on, even more so if we have the rest of the message to draw on - but l want to either automate this completely or at least vastly reduce human input.