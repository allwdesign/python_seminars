"""
The natural power of pow is given. Randomly generate a list of coefficients
(values from 0 to 100) of the polynomial and write the polynomials of degree
pow to the file.
*Example:*

- pow=2 => 2*x² + 4*x + 5 = 0 or x² + 5 = 0 or 10*x² = 0
"""
from random import randint


def check_coefficient(coef: int) -> str:
    """
    Function to check the value of the coefficient is equal to one.

    :param coef: int. If coefficient=1, then: 'x', not '1*x'
    :return: str. String with coefficient for polynomial.
    """
    return "x" if coef == 1 else f"{coef} * x"


def check_pow(pow: int) -> str:
    """
    Function to check if the pow of polynomial is equal to one.

    :param pow: int. The pow of polynomial.
    :return: str. String with pow for polynomial.
    """
    return "" if pow == 1 else f" ^ {pow}"


# Для первой степени количество коэффициентов: 2
# Для второй количество коэффициентов: 1, 2 или 3


def get_coefficients(pow: int) -> list:
    """
    Get coefficients for polynomial. The possible number of coefficients
    is pow+1.

    :param pow: int. The pow of polynomial.
    :return: list with coefficients.
    """
    coefficients = list()

    quantity = randint(1, pow + 1)
    # print(quantity)

    for i in range(0, quantity):
        # a != 0 - the first coefficient should not be zero
        if not i:
            coefficients.append(randint(1, 101))
        else:
            coefficients.append(randint(0, 101))

    return coefficients


def create_polynomial(pow: int, coefficients: list) -> str:
    """
    Create a string with polynomial to write to a file.

    :param pow: int. The pow of polynomial.
    :param coefficients: list. The coefficients for polynomial.
    :return: str. String with polynomial.
    """
    res = ""
    # "coef * x ^ pow" or "x ^ pow" or "x"
    res = check_coefficient(coefficients[0]) + check_pow(pow)

    if len(coefficients) > 1:
        # first_coef = res
        last = f"{coefficients[-1]}"
        others = " + "
        for coef in coefficients[1:-1]:
            # print("pow:", pow)
            while pow > 0:
                pow -= 1
            others += check_coefficient(coef) + check_pow(pow) + " + "
        res += others + last

    res += " = 0"

    return res


def write_polynomial(filename: str, line: str) -> None:
    """
    Writes a string with polynomial to a file with the specified filename
    in current directory.

    :param filename: str.
    :param line: str. String with polynomial.
    :return: None.
    """
    with open(filename, "a") as data:
        data.write(line + "\n")


try:
    print('The program randomly generate a list of coefficients (values from'
          ' 0 to 100) of the polynomial and write the polynomials of degree '
          'pow to the file.')
    for k in range(0,5):
        coeffs = get_coefficients(k)
        print(f"The natural power of pow={k}. Coefficients: {coeffs}.")
        polynomial = create_polynomial(k, coeffs)
        print("Polynomial:", polynomial)
        write_polynomial("polynomial.txt", polynomial)
except ValueError as error:
    print(error)
