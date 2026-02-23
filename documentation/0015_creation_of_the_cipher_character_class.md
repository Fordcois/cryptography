# The Cipher Symbol Class
The Cipher Character class is established to store information on cipher characters, So we can use multiple ethods to find and consolidate our information on the potential plaintext reading. By centralising the mapping logic in the class, we can more easily manage complex ciphers—such as those using non-English symbols (like the Zodiac) or homophonic ciphers where a single symbol can stand for multiple plaintext letters.

For example if we use straight single letter Frequency Analysis we can store the likelyhood in the object class, we can then do further analysis such as bigrams/trigram analysis and add this into our object which will work to improve our confidence level. The Class should also be able to offer a best guess or lock in certain readings so that we're able to manually decrypt remaining letters if needed.


## Goals of the Class
- Take a cipher Symbol aand store probability of each letter
- Be able to update probabilities
- return best guess(es) of characters

## Potential roadblocks and Considerations

**Confidence Levels**
The class initialises with a 0% confidence for each letter and as data is fed this will grow although the significant levels of confidence growth will need to be explored.

**Understand the strength of certain approaches**
For example depending on the cipher text a single letter substituiton ciphers may not be as concrete in determinig a character as an I 7% Frequency against an N (6.7% Frequency) but we find stronger distinction by analysing bigrams - IN (2.43%) vs NI 0.338% Frequency and even further evidence looking at the trigrams with both ING,ION,ING being in the top 3 most frequence (Data from [Peter Norvig](https://norvig.com/mayzner.html)).We will want to explore and test the realtive strengths of these different approaches to help with our mapping confidence.


