import string

alphabet_list = list(string.ascii_lowercase)
alphabet_list_uppercase = list(string.ascii_uppercase)


def warmup(letter: str, shift_by: int) -> str:
    """
    Caesar shift alphabet function, works for one letter

    :param letter: letter to shift
    :param shift_by: shift modulo
    :return: alphabet letter shifted by modulo parameter
    """
    if letter in string.whitespace or letter in string.punctuation:
        return letter

    if letter.isupper():
        index_original = alphabet_list_uppercase.index(letter)
        index_new = (index_original + shift_by) % 26
        result = alphabet_list_uppercase[index_new]
    else:
        index_original = alphabet_list.index(letter)
        index_new = (index_original + shift_by) % 26
        result = alphabet_list[index_new]

    return result


def caesar(original_string: str, shift_by: int) -> str:
    """
    Casar shift alphabet function, shifts an entire string

    :param original_string: string to encrypt
    :param shift_by: shift modulo
    :return: resulting string from original string, shifted by modulo operator
    """

    char_list = [c for c in original_string]
    shifted_char_list = [warmup(c, shift_by) for c in char_list]

    return "".join(shifted_char_list)
