def cipher(text, shift, encrypt=True):
    '''
    Caesar cipher is an encryption techniques.
    Each letter is replaced by a letter some fixed number of positions down the alphabet.

    Parameters
    ----------
    text: str
        A string of text that people would like to encrypt or decrypt
    shift: int
        A interger for shifts incidating the number of digits that people would like to encrypt or decrypt
    encrypt: boolean
        A boolean value indicating either True or False for encrypt or decrypt

    Returns
    ----------
    new_text: str 
        A string of text that has been encrypted or decrpted with shifts from text

    Examples
    ----------
    >>> from cipher_liao_ziqi import cipher_liao_ziqi
    >>> cipher_liao_ziqi.cipher('Practice',3)
    'Sudfwlfh'

    '''

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