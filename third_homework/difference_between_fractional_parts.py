"""
Specify a list of real numbers. Write a program that will find the difference between the maximum
and the minimum value of the fractional part of the elements.
*Example:*

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""
from fractions import Fraction


def difference(numbers: list) -> float:
    """
    The functions that will find the difference between the maximum
    and the minimum value of the fractional part of the elements.

    :param numbers: list of real numbers.
    :return: float number - difference between the maximum and the minimum
            value of the fractional part of the elements.
    """
    parts = list()
    for number in numbers:
        # Check whether the number is float type, if not, move on to the next one.
        if type(number) == float:
            # Cut off the fractional part
            fractional_part = Fraction((number - int(number)))  # 1.23 - 1 = 0.23
            # Add fractional parts of numbers to list
            parts.append(fractional_part)

    min_fr = parts[0]
    max_fr = parts[0]

    for fr_part in parts:
        if fr_part > max_fr:
            # Previous max became min
            min_fr = max_fr
            max_fr = fr_part
        else:
            # Then fr_part <= previous max_fr,
            # check whether it is a minimum (whether it is less than min_fr )
            if fr_part < min_fr:
                min_fr = fr_part

    return float(round((max_fr - min_fr), 2))


try:
    print("The program that will find the difference between the maximum \n"
          "and the minimum value of the fractional part of the elements.\n")

    numbers = [1.1, 1.2, 3.1, 5, 10.01]

    print("Original lists:", numbers, "=>", "Difference:", difference(numbers))
except ValueError as error:
    print(error)
