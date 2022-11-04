"""
Set the natural number N. Write a program that will make a list of prime
multipliers of the number N.
"""


def factorize(n: int) -> list:
    """
    Decomposes the number of prime multipliers.

    :param n: int. The number to be decomposed into prime factors.
    :return: list. List with prime multipliers.
    """
    res = list()
    d = 2
    while d * d <= n:
        if n % d == 0:
            res.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        res.append(n)
    return res


try:
    print('The program will make a list of prime multipliers of the number N.')
    number = int(input("Enter a integer number: "))

    print(f'The number to be decomposed: {number}')
    multipliers = ', '.join(str(x) for x in factorize(number))
    print(f"The prime multipliers: {multipliers}.")
except ValueError as error:
    print(error, 'Value must be integer number!')