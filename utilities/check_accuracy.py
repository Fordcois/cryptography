def check_accuracy(user_answer,correct_answer,return_sub_key=False):
    # print(f'User Answer: {user_answer}')
    # print(f'Correct Answer: {correct_answer}')
    total_characters=0
    correct_characters=0
    individual_letters = 0
    correct_letters = 0
    substitution_key = {}
    # Check Length is the same
    if len(user_answer) != len(correct_answer):
        print ('Lengths do not match')
        return False
    
    for i in range(len(user_answer)):
        if user_answer[i].isalpha() and correct_answer[i].isalpha():
            total_characters += 1
            if correct_answer[i].upper() not in substitution_key:
                individual_letters += 1
                substitution_key[correct_answer[i].upper()] = user_answer[i].upper()
                if correct_answer[i].upper() == user_answer[i].upper():
                    correct_letters += 1

            if user_answer[i] == correct_answer[i]:
                correct_characters += 1

    accuracy = (correct_characters / total_characters) * 100

    print ( f'Passage Accuracy is {accuracy:.2f}% with {correct_letters}/{individual_letters} letters')
    # TODO - Return Substitution Key in alphabetical order for ease of use
    if return_sub_key:
        print (substitution_key)
        return accuracy,substitution_key
    # print (substitution_key)
    return accuracy


