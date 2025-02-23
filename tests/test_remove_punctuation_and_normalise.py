import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from lib.encrypt_functions.remove_punctuation import remove_punctuation_and_normalise

def test_normalise_string_lower_case():
    """Turns String Uppercase"""
    assert remove_punctuation_and_normalise('hello world') == 'HELLO WORLD'

def test_normalise_string_both_case():
    """Turns String all Uppercase"""
    assert remove_punctuation_and_normalise('Hello World') == 'HELLO WORLD'

def test_normalise_string_mixed_case():
    """Turns string all uppercase when mixed in"""
    assert remove_punctuation_and_normalise('HeLlO WoRlD') == 'HELLO WORLD'

def test_normalise_string_ignore_punctuation():
    """Ignores punctuation of passed strings"""
    assert remove_punctuation_and_normalise('Hello World! How are you?') == 'HELLO WORLD HOW ARE YOU'