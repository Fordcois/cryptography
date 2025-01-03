import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from lib.validation_tools.valid_solution import valid_words

def test_checks_correct_spelling_of_single_word():
    result = valid_words('hello')
    assert result == True

def test_checks_incorrect_spelling_of_single_word():
    result = valid_words('heelo')
    assert result == False

def test_checks_correct_spelling_of_multiple_words():
    result = valid_words('Hello world Welcome to London')
    assert result == True

def test_checks_incorrect_spelling_of_multiple_words():
    result = valid_words('Heelo world Welcome to London')
    assert result == False

def test_checks_correct_spelling_of_multiple_words_ignores_punctuation():
    result = valid_words('Hello world! Welcome to London. Where are you going to go first?')
    assert result == True

def test_checks_incorrect_spelling_of_multiple_words_ignores_punctuation():
    result = valid_words('Heelo world! Welcome to London. Where are you going to go first?')
    assert result == False

def test_invalid_when_below_threshold():
    result = valid_words('Heello Woorld aree you happy?',50.00)
    assert result == False

def test_valid_when_equal_to_threshold():
    result = valid_words('Heello Woorld are you happy?',60.00)
    assert result == True

def test_valid_when_above_threshold():
    result = valid_words('Heello World are you happy?',75.00)
    assert result == True

def test_checks_word_not_in_temp_wordlist():
    result = valid_words('floozelwurt is not a word')
    assert result == False

def test_checks_incorrect_spelling_of_multiple_words():
    result = valid_words('floozelwurt is not a word',100,['floozelwurt'])
    assert result == True


