import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from lib.encrypt_functions.keyword_cipher import keyword_cipher_encrypt

def test_keyword_cipher_encrypt_keyword_one():
    cipher = keyword_cipher_encrypt('keyword','this is my secret message')
    assert cipher == 'qabp bp hx poynoq hoppkdo'

def test_keyword_cipher_encrypt__keyword_one_keeping_capitalisation():
    cipher = keyword_cipher_encrypt('keyword','This Is My Secret Message')
    assert cipher == 'Qabp Bp Hx Poynoq Hoppkdo'

def test_keyword_cipher_encrypt_keyword_two():
    cipher = keyword_cipher_encrypt('secretpassword','my evil plan is within this text thats why i have hidden it')
    assert cipher == 'gy tuof jfsh om vonwoh nwom ntxn nwsnm vwy o wsut worrth on'

def test_keyword_cipher_encrypt__keyword_two_keeping_capitalisation():
    cipher = keyword_cipher_encrypt('secretpassword','My evil plan is within this text thats why I have hidden it')
    assert cipher == 'Gy tuof jfsh om vonwoh nwom ntxn nwsnm vwy O wsut worrth on'

def test_keyword_cipher_encrypt_ignores_non_alpha_characters():
    cipher = keyword_cipher_encrypt('secretpassword','The code to the safe is 1234 - do not forget it!')
    assert cipher == 'Nwt cirt ni nwt mspt om 1234 - ri hin pilatn on!'