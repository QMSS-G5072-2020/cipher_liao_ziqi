from cipher_liao_ziqi import __version__
from cipher_liao_ziqi import cipher_liao_ziqi

def test_version():
    assert __version__ == '0.1.0'
    
def cipher_liao_ziqi(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ'
    new_text = ''
    if type(shift) != int:
        raise ValueError('The parameter shift should be an integer')

    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index + 1]
    return new_text


def test_single():
    text = 'a'
    shift = 1
    expect = 'b'
    out = cipher_liao_ziqi(text , shift)
    assert out == expect