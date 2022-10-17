"""
A program that takes a number N as input and outputs a list of products of numbers from 1 to N.

*Example:*
N = 4, then [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
"""


def get_production(num: int) -> list:
    """
    A function that takes integer number and return a list of products of numbers
    in the range from 1 to number.

    :param num: int. Number
    :return: list of products.
    """
    result = list()
    production = 1
    for i in range(1, num + 1):
        production *= i
        result.append(production)

    return result


try:
    print("A program that takes a number N as input and outputs a list of products of numbers from 1 to N.")
    number = int(input("Enter a number: "))
    print(f"N = {number}, then", get_production(number))
except ValueError as e:
    print(e)