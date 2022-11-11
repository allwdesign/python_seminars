"""
Write a program to remove all words containing 'абв' from text.
The FIND and COUNT functions cannot be used.
"""


def filter_substring(pattern: str, text: str) -> str:
    """
    The function will return a string without words containing the pattern.
    Case-insensitive implementation.

    :param pattern: str. The pattern you want to filter.
    :param text: str. Original string.
    :return: str. A string without words containing the pattern.
    """
    pattern = pattern.lower()
    splited = text.split()

    # case-insensitive: АБВ or абв
    insensitive_result = list(
        filter(lambda word: pattern not in word.lower(), splited))

    return ' '.join(insensitive_result)


try:
    substring = 'абв'
    text = ('ыуабваплдулпабвабввабззждв Папа силен, мама хотела уехать в '
            'Зимбабве ЗИМБАБВЕ, Тулу забвение, читая абвгдейку, Мастер и '
            'Маргарита.')

    print(f'Original text: {text}')
    print(f'After delete: {filter_substring(substring, text)}')

except Exception:
    print('Something went wrong!')
