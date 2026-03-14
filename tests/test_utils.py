import pytest
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from utilities.utils import clean_text

def test_alphabetic_characters_are_kept():
    assert clean_text('123Hello World!') == 'Hello World'

def test_numbers_and_symbols_are_removed():
    assert clean_text('fo@0o0 B@ar99') == 'foo Bar'

def test_empty_string_returns_empty_string():
    assert clean_text('') == ''

def test_only_special_characters_returns_empty_string():
    assert clean_text('123!@#') == ''

def test_only_spaces_are_kept_by_default():
    assert clean_text('   ') == '   '

def test_spaces_are_removed_when_keep_spaces_is_false():
    assert clean_text('123Hello World!', False) == 'HelloWorld'

def test_numbers_symbols_and_spaces_are_removed_when_keep_spaces_is_false():
    assert clean_text('fo@0 oB@ar99', False) == 'fooBar'

def test_only_spaces_returns_empty_string_when_keep_spaces_is_false():
    assert clean_text('   ', False) == ''

def test_allowed_chars_are_kept_alongside_letters_and_spaces():
    assert clean_text('123Hello, world!', True, ['!', ',']) == 'Hello, world!'

def test_allowed_chars_are_kept_while_spaces_are_removed():
    assert clean_text('Hello, world 12345!', False, ['!', '1', '2', '3']) == 'Helloworld123!'

def test_empty_allowed_chars_list_behaves_like_none():
    assert clean_text('hello, world!', allowedChars=[]) == 'hello world'

def test_numbers_can_be_included_via_allowed_chars():
    assert clean_text('h3ll0 w0rld', allowedChars=['3', '0']) == 'h3ll0 w0rld'