def get_char_type(char):
    """
    Returns a string denoting the type of char.
    """
    operators = {'*', '/', '+', '-'}
    if char.isdigit():
        char_type = 'number'
    elif char.isalpha():
        char_type = 'letter'
    elif char in operators:
        char_type = 'operator'
    else:
        char_type = 'other'
    return char_type


def tokenize(string):
    """
    Generates tokens from a mathematical statement string.

    """
    token_type = get_char_type(string[0])
    token = ''
    for char in string:
        if char == ' ':
            continue  # Spaces are not included
        new_type = get_char_type(char)
        if new_type != token_type:  # A new type of token has been found
            yield token
            token_type = new_type
            token = ''
        token += char
    if len(token) > 0:
        yield token

print(list(tokenize('3 + (4 ∗ 5)')))
l = list(tokenize('3 + (4 ∗ 5)'))



