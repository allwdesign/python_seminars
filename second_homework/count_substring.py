"""
The program determines the amount occurrences of one string in another.
The strings are set by the user from the keyboard.
"""


def find_substring(pattern: str, text: str) -> list:
    """
    The function find a substring in a string.

    :param pattern: str. The substring you want to find. Set by the user from the keyboard.
    :param text: str. The string to find for. Set by the user from the keyboard.
    :return: list with indices or [] if not find pattern in text.
    """
    indices = list()
    if pattern not in text:
        return []
    # if length_text=19 length_pattern=3 then we iterate 19 - 3 + 1 = 17
    times = len(text) - len(pattern) + 1
    for i in range(times):
        # move the border of the text slice on every iteration
        # [0:3][1:4][2:5] etc.
        if pattern == text[i:len(pattern) + i]:
            indices.append(i)
    return indices


def count_substring(indices: list) -> int:
    """
    The function count how many times a substring occurs in a string.

    :param indices: list with indices.
    :return: int. How many times a substring occurs in a string.
    """
    return len(indices)


def print_result(string: str, substring: str, amount: int) -> None:
    """
    The function print result to console.

    :param string: str. The string to find for. Set by the user from the keyboard.
    :param substring: str. The substring you want to find. Set by the user from the keyboard.
    :param amount: int. How many times a substring occurs in a string.
    :return: None.
    """
    print("Sting: ", string)
    print("Substring: ", substring)
    print("Amount: ", amount)


def program_check():
    print("-" * 10, "Program Check", "-" * 10)
    amount  = 0
    data = [
        ('xrm', 'erjgrxrmxrmeggwaskl'),
        ("qz", 'erjgrxrmxrmeggwaskl'),
        ("wdi", "a"),
        ("pop", "popincetevgpop"),
        ("popi", "popincetevgpopi"),
        ("p", "popincpppetevgpopi")]

    for substring, string in data:
        print("-" * 30)
        amount = count_substring(find_substring(substring, string))
        print_result(string, substring, amount)
    print("-" * 10, "End Program Check", "-" * 10, "\n")


try:
    program_check()
    print("The program determines the amount occurrences of one string in another. "
          "The strings are set by the user from the keyboard.")
    string = input("Enter the string to find for: ")
    substring = input("Enter the substring you want to find: ")

    amount = count_substring(find_substring(substring, string))

    print_result(string, substring, amount)
except ValueError as e:
    print(e)
