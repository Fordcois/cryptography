import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from lib.encrypt_functions.caesar_cipher import caesar_cipher_encrypt

def test_caesar_cipher_offset_1():
    """Test encryption of Caesar cipher - offset 1"""
    assert caesar_cipher_encrypt('AbCdEfGhIjKlMnOpQrStUvWxYz', 1) == 'BcDeFgHiJkLmNoPqRsTuVwXyZa'

def test_caesar_cipher_offset_2():
    """Test encryption of Caesar cipher - offset 2"""
    assert caesar_cipher_encrypt('AbCdEfGhIjKlMnOpQrStUvWxYz', 2) == 'CdEfGhIjKlMnOpQrStUvWxYzAb'

def test_caesar_cipher_offset_3():
    """Test encryption of Caesar cipher - offset 3"""
    assert caesar_cipher_encrypt('AbCdEfGhIjKlMnOpQrStUvWxYz', 3) == 'DeFgHiJkLmNoPqRsTuVwXyZaBc'

def test_caesar_cipher_offset_4():
    """Test encryption of Caesar cipher - offset 4"""
    assert caesar_cipher_encrypt('AbCdEfGhIjKlMnOpQrStUvWxYz', 4) == 'EfGhIjKlMnOpQrStUvWxYzAbCd'

def test_caesar_cipher_offset_5():
    """Test encryption of Caesar cipher - offset 5"""
    assert caesar_cipher_encrypt('AbCdEfGhIjKlMnOpQrStUvWxYz', 5) == 'FgHiJkLmNoPqRsTuVwXyZaBcDe'

def test_caesar_cipher_offset_6():
    """Test encryption of Caesar cipher - offset 6"""
    assert caesar_cipher_encrypt('AbCdEfGhIjKlMnOpQrStUvWxYz', 6) == 'GhIjKlMnOpQrStUvWxYzAbCdEf'

def test_caesar_cipher_offset_7():
    """Test encryption of Caesar cipher - offset 7"""
    assert caesar_cipher_encrypt('AbCdEfGhIjKlMnOpQrStUvWxYz', 7) == 'HiJkLmNoPqRsTuVwXyZaBcDeFg'

def test_caesar_cipher_offset_8():
    """Test encryption of Caesar cipher - offset 8"""
    assert caesar_cipher_encrypt('AbCdEfGhIjKlMnOpQrStUvWxYz', 8) == 'IjKlMnOpQrStUvWxYzAbCdEfGh'

def test_caesar_cipher_offset_9():
    """Test encryption of Caesar cipher - offset 9"""
    assert caesar_cipher_encrypt('AbCdEfGhIjKlMnOpQrStUvWxYz', 9) == 'JkLmNoPqRsTuVwXyZaBcDeFgHi'

def test_caesar_cipher_offset_10():
    """Test encryption of Caesar cipher - offset 10"""
    assert caesar_cipher_encrypt('AbCdEfGhIjKlMnOpQrStUvWxYz', 10) == 'KlMnOpQrStUvWxYzAbCdEfGhIj'

def test_caesar_cipher_offset_11():
    """Test encryption of Caesar cipher - offset 11"""
    assert caesar_cipher_encrypt('AbCdEfGhIjKlMnOpQrStUvWxYz', 11) == 'LmNoPqRsTuVwXyZaBcDeFgHiJk'

def test_caesar_cipher_offset_12():
    """Test encryption of Caesar cipher - offset 12"""
    assert caesar_cipher_encrypt('AbCdEfGhIjKlMnOpQrStUvWxYz', 12) == 'MnOpQrStUvWxYzAbCdEfGhIjKl'

def test_caesar_cipher_offset_13():
    """Test encryption of Caesar cipher - offset 13"""
    assert caesar_cipher_encrypt('AbCdEfGhIjKlMnOpQrStUvWxYz', 13) == 'NoPqRsTuVwXyZaBcDeFgHiJkLm'

def test_caesar_cipher_offset_14():
    """Test encryption of Caesar cipher - offset 14"""
    assert caesar_cipher_encrypt('AbCdEfGhIjKlMnOpQrStUvWxYz', 14) == 'OpQrStUvWxYzAbCdEfGhIjKlMn'

def test_caesar_cipher_offset_15():
    """Test encryption of Caesar cipher - offset 15"""
    assert caesar_cipher_encrypt('AbCdEfGhIjKlMnOpQrStUvWxYz', 15) == 'PqRsTuVwXyZaBcDeFgHiJkLmNo'

def test_caesar_cipher_offset_16():
    """Test encryption of Caesar cipher - offset 16"""
    assert caesar_cipher_encrypt('AbCdEfGhIjKlMnOpQrStUvWxYz', 16) == 'QrStUvWxYzAbCdEfGhIjKlMnOp'

def test_caesar_cipher_offset_17():
    """Test encryption of Caesar cipher - offset 17"""
    assert caesar_cipher_encrypt('AbCdEfGhIjKlMnOpQrStUvWxYz', 17) == 'RsTuVwXyZaBcDeFgHiJkLmNoPq'

def test_caesar_cipher_offset_18():
    """Test encryption of Caesar cipher - offset 18"""
    assert caesar_cipher_encrypt('AbCdEfGhIjKlMnOpQrStUvWxYz', 18) == 'StUvWxYzAbCdEfGhIjKlMnOpQr'

def test_caesar_cipher_offset_19():
    """Test encryption of Caesar cipher - offset 19"""
    assert caesar_cipher_encrypt('AbCdEfGhIjKlMnOpQrStUvWxYz', 19) == 'TuVwXyZaBcDeFgHiJkLmNoPqRs'

def test_caesar_cipher_offset_20():
    """Test encryption of Caesar cipher - offset 20"""
    assert caesar_cipher_encrypt('AbCdEfGhIjKlMnOpQrStUvWxYz', 20) == 'UvWxYzAbCdEfGhIjKlMnOpQrSt'

def test_caesar_cipher_offset_21():
    """Test encryption of Caesar cipher - offset 21"""
    assert caesar_cipher_encrypt('AbCdEfGhIjKlMnOpQrStUvWxYz', 21) == 'VwXyZaBcDeFgHiJkLmNoPqRsTu'

def test_caesar_cipher_offset_22():
    """Test encryption of Caesar cipher - offset 22"""
    assert caesar_cipher_encrypt('AbCdEfGhIjKlMnOpQrStUvWxYz', 22) == 'WxYzAbCdEfGhIjKlMnOpQrStUv'

def test_caesar_cipher_offset_23():
    """Test encryption of Caesar cipher - offset 23"""
    assert caesar_cipher_encrypt('AbCdEfGhIjKlMnOpQrStUvWxYz', 23) == 'XyZaBcDeFgHiJkLmNoPqRsTuVw'

def test_caesar_cipher_offset_24():
    """Test encryption of Caesar cipher - offset 24"""
    assert caesar_cipher_encrypt('AbCdEfGhIjKlMnOpQrStUvWxYz', 24) == 'YzAbCdEfGhIjKlMnOpQrStUvWx'

def test_caesar_cipher_offset_25():
    """Test encryption of Caesar cipher - offset 25"""
    assert caesar_cipher_encrypt('AbCdEfGhIjKlMnOpQrStUvWxYz', 25) == 'ZaBcDeFgHiJkLmNoPqRsTuVwXy'
