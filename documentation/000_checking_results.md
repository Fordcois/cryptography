The aim of this project is to automatically validate as much as possible without human intervention. Ultimately, I want to pass in cipher text and have the program return english.

So how will the program know an answer is correct?

I’ve initially written two functions that will help us evaluate the accuracy of our proposed solutions. The first is `check_accuracy` [Code Here](https://github.com/Fordcois/cryptography/blob/main/lib/validation_tools/check_accuracy.py), which takes our generated answer as well as the correct plaintext and returns the percentage of characters in the correct position, along with the number of letters we have guessed correctly. It can also provide the substitution key we’re using, allowing for manual adjustments if needed.

This function offers both the overall passage accuracy and the number of correct letters. Both pieces of information are essential for making further guesses at the correct solution. For instance, if we’ve guessed the top five most common letters correctly but the rest incorrectly, our accuracy score might seem relatively high, even though most of the letters are wrong. Similarly, if we’ve got 23 letters correct but the top three wrong, our accuracy score could be disproportionately low, even though a few small adjustments could lead to a fully correct answer.

### Verification without the plaintext
What happens , as is typical with most ciphers, we don’t have the plaintext?
The above function is primarily for assisting in my own development and testing of tools but my aim is to build something for practical applications and so we require a way to verify the correctness of a solution - without human review.

The `valid_words` function takes the decoded text as input and checks each word within the passage to see if it is a valid word in US English. If all the words in the passage are correct, it’s likely we’ve achieved a complete and accurate decipherment. You can see the [code here](https://github.com/Fordcois/cryptography/blob/main/lib/validation_tools/valid_solution.py)

The function also accepts two other arguments:

1. **`threshold`** – This specifies the minimum percentage of correct words required for the translation to be considered valid. By default, this is set to 100%, but it can be lowered to account for incomplete translations or intentional or unintentional misspellings by the cipher’s creator.
2. **`whitelisted_words`** – This optional argument allows us to include certain words that should be counted as valid. For example, the Zodiac deliberately misspelled “Paradise” as “Paradice” in the 1969 Z408 Cipher and subsequent communications. This same misspelling appeared in the Z340 cipher, which remained unsolved until 2020 and had this spelling appeared in earlier decryption attempts, wouldn't have been discounted. This argument lets us account for that. There’s a separate text file for more permanent additions to the dictionary, included as a form of future-proofing; potentially to add names or locations that may not appear in our traditional dictionary.

The results and applications of these functions, along with any shortcomings or adaptations, will be addressed as the project progresses.