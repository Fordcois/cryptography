def check_accuracy(user_answer,correct_answer):
    total_characters=0
    correct_characters=0
    # Check Length is the same
    if len(user_answer) != len(correct_answer):
        print ('Lengths do not match')
        return False
    
    for i in range(len(user_answer)):
        total_characters += 1
        if user_answer[i] == correct_answer[i]:
            correct_characters += 1

    accuracy = (correct_characters / total_characters) * 100
    print (f'Accuracy is {accuracy:.2f}%')
    return accuracy


