"""
Write a program to find the product of pairs of numbers in a list. We count the first one as a couple
and the last element, second and penultimate, etc.
*Example:*

[2, 3, 4, 5, 6] => [12, 15, 16];
[2, 3, 5, 6] => [12, 15]
"""


def multiply_pair_elements(numbers: list) -> list:
    """
    This program to multiply the pairs of numbers in a list.
    We count the first one as a couple and the last element, second and penultimate, etc.

    :param numbers: list with integer numbers.
    :return: list with results of multiply items from numbers list.
    """
    prods = list()
    length = len(numbers)

    if length % 2 != 0:
        size = range(length // 2 + 1)
    else:
        size = range(length // 2)

    for i in size:
        prods.append(numbers[i]*numbers[length - 1 - i])

    return prods


try:
    print("This program to multiply the pairs of numbers in a list. \n"
          "We count the first one as a couple "
          "and the last element, second and penultimate, etc.")
    lists = [[2, 3, 4, 5, 6], [2, 3, 5, 6]]
    for numbers in lists:
        print("Original list with numbers:", numbers, "=>", "Result of multiply:", multiply_pair_elements(numbers))

except ValueError as error:
    print(error)





