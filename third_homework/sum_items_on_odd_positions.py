"""
Specify a list of several numbers. Write a program that will find the sum of the list items,
standing in an odd position.
*Example:*

[2, 3, 5, 9, 3] -> elements 3 and 9 in odd positions, answer: 12
"""


def sum(indeces: list, numbers: list) -> int:
    """
    The function get sum of the numbers list items, standing in an odd position.
    :param indeces: list with odd indeces.
    :param numbers: list with numbers.
    :return: int. The sum of the list items, standing in an odd position.
    """
    sum = 0

    for idx in indeces:
        sum += numbers[idx]

    return sum


try:
    numbers = [2, 3, 5, 9, 3]
    odd_indeces = list(range(1, len(numbers), 2))

    msg = " and ".join([str(numbers[idx]) for idx in odd_indeces])

    print(f"Original list: {numbers}")
    print(f"Odd positions indeces: {odd_indeces}")
    print(f"Elements on odd positions: {msg}")
    print(f"Sum of elements: {sum(odd_indeces, numbers)}")

except ValueError as error:
    print(error)