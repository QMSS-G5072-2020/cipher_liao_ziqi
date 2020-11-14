'''
Caesar cipher is an encryption techniques.
Each letter is replaced by a letter some fixed number of positions down the alphabet.

Parameters
----------
text: text that people would like to encrypt
shift: number of shifts that people would like to have when encrypting

Returns
----------
new_text that has been encrypted with shifts from text


Examples
----------
 >>> from cipher_zl2988 import cipher_zl2988
 >>> cipher_zl2988.cipher('Practice',3)
'Sudfwlfh'

'''
def cipher(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text