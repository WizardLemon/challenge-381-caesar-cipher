import string

alphabet_list = list(string.ascii_lowercase)


def warmup(letter: str, shift_by: int) -> str:
    """
    Caesar shift alphabet function

    :param letter: letter to shift
    :param shift_by: shift modulo
    :return: alphabet letter shifted by modulo parameter
    """

    index_original = alphabet_list.index(letter)
    index_new = (index_original + shift_by) % 26
    result = alphabet_list[index_new]

    return result
