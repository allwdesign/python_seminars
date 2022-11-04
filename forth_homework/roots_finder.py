"""
This program will find the roots of a quadratic equation,
the equation is entered through the console user.
Example: 6*x^2+5*x+6=0.
"""
import re
from fractions import Fraction

POSITIVE_ONE = '+'
NEGATIVE_ONE = '-'
FIRST_ROOT = 'First root: x ='
SECOND_ROOT = 'Second root: x ='


def get_roots(a: Fraction, b: Fraction, c: Fraction) -> str:
    """
    Calculates the roots of a quadratic equation. The result rounds up to two
    decimal places.

    Full quadratic equation: a*x^2+b*x+c=0, where a!=0.
    Incomplete quadratic equation:
    1. a*x^2+b*x=0, where a!=0, b!=0, c=0
    2. a*x^2+c=0,   where a!=0, b=0,  c!=0.

    :param a: Fraction. Coefficient of a quadratic equation.
        Example: Fraction(6, 1)
    :param b: Fraction. Coefficient of a quadratic equation.
        Example: Fraction(5, 1)
    :param c: Fraction. Coefficient of a quadratic equation.
        Example: Fraction(6, 1)
    :return: str. String with result.
    """
    try:
        roots_msg = ""

        if b != 0 and c != 0:
            # a*x^2+b*x+c=0. Examples: 6*x^2+5*x+6=0  or -6*x^2-5*x-6=0.
            d = b ** 2 - 4 * a * c
            if d > 0:
                # Two roots
                x1 = float((-b + d ** 0.5) / (2 * a))
                x2 = float((-b - d ** 0.5) / (2 * a))
                roots_msg = f'{FIRST_ROOT} {x1:.2f}. {SECOND_ROOT} {x2:.2f}.'
            elif d < 0:
                roots_msg = "No real roots!"
            else:
                # d=0
                x1 = float(-(b / (2 * a)))
                roots_msg = f"Two equal roots: x = {x1:.2f}."
        elif b == 0 and c == 0:
            # a*x^2=0. Example: 10*x^2=0.
            roots_msg = "One root: x = 0."
        elif c == 0:
            # a*x^2+b*x=0. Example: 6*x^2+5*x=0.
            x2 = float(- b / a)
            roots_msg = f'{FIRST_ROOT} 0. {SECOND_ROOT} {x2:.2f}.'
        else:
            # b=0, a*x^2+c=0. Example: x^2 + 5= 0.
            if -c / a > 0:
                x1 = float((-c / a) ** 0.5)
                x2 = float(-((-c / a) ** 0.5))
                roots_msg = f'{FIRST_ROOT} {x1:.2f}. {SECOND_ROOT} {x2:.2f}.'
            else:
                # -c / a < 0
                roots_msg = "No solutions!"

        return roots_msg
    except ZeroDivisionError as e:
        raise ZeroDivisionError('Error: Division by zero! ')


def convert(coefficients: dict) -> dict:
    """
    Convert the coefficient of the quadratic equation to the Fraction type

    Full quadratic equation: a*x^2+b*x+c=0, where a!=0.
    Incomplete quadratic equation:
    1. a*x^2+b*x=0, where a!=0, b!=0, c=0
    2. a*x^2+c=0,   where a!=0, b=0,  c!=0.

    a,b,c - coefficients of quadratic equation.
    a -> coefficients['a']
    b -> coefficients['b']
    c -> coefficients['c']

    The coefficient standing before x equal to one is omitted when writing.
    Examples:
    if x^2+x=0, then a='' and b='+' it means a=1 and b=1
    if -x^2-x=0, then a=b='-' it means a=b=-1
    b=c=None - it means b=с=0

    :param coefficients: dict.
        Example: {'a': '6', 'b': '+5', 'c': '+6'}
    :return: dict.
        Example:
            {'a': Fraction(6, 1), 'b': Fraction(5, 1), 'c': Fraction(6, 1)}
    """
    coef = None
    nums = dict()

    for key, val in coefficients.items():
        if ((key == 'a' and not val)
                or (key == 'b' and val == POSITIVE_ONE)):
            # a='' or b='+'
            coef = Fraction(1)
        elif not val:
            # b=c='' or None
            coef = Fraction(0)
        elif val == NEGATIVE_ONE:
            # a=b='-'
            coef = Fraction(-1)
        else:
            # If a,b,c > 0  or a,b,c < 0
            coef = Fraction(val)

        nums[key] = coef

    return nums


def del_spaces(items) -> dict:
    """
    Remove spaces from the input data.

    :param items: dict_items.
        Example:
        dict_items([('quadratic', '6 * x ^ 2 + 5 * x + 6 = 0'),
                    ('a', '6'), ('b', '+ 5'), ('c', '+ 6')])
    :return: dict with data without spaces.
        Example: {'quadratic': '6*x^2+5*x+6=0','a': '6', 'b': '+5', 'c': '+6'}
    """
    # filter object:('quadratic': '-x^2 + 9 = 0'),('a': '-'),('c': '+ 9')
    without_none_values = filter(lambda item: item[1] is not None, items)

    # none_values: {'b': None}
    none_values = dict(filter(lambda item: item[1] is None, items))

    # without_space_values: {'quadratic': '-x^2+9=0', 'a': '-', 'c': '+9'}
    without_space_values = dict(map(
        lambda item: (item[0], re.sub(r"\s+", "", item[1])),
        without_none_values))

    # {'quadratic': '-x^2+9=0', 'a': '-', 'b': None,'c': '+9'}
    without_space_values.update(none_values)

    return without_space_values


def check_equation(input_string: str) -> dict:
    """
    Check whether the quadratic equation is entered by the user and whether
    it matches one of the patterns.

    :param input_string: str. Input data is entered through the console
    user. Example: '6 * x ^ 2 + 5 * x + 6 = 0'
    :return: dict. Example: {
        'quadratic': '6 * x ^ 2 + 5 * x + 6 = 0',
        'a': '6', 'b': '+ 5', 'c': '+ 6'}
    """

    res = re.search(
        r"^(?P<quadratic>((?P<a>-?\d*[./]?\d*)\s?\*?\s?x\s?\^\s?2)\s?"
        r"((?P<b>[+-]\s?\d*[./]?\d*)?\s?\*?\s?x)?\s?"
        r"(?P<c>[+-]\s?\d+[./]?\d*)?\s?=\s?0)$",
        input_string)

    # Non-quadratic equation: equation failed validation
    if res is None:
        raise Exception("It doesn't match. Wrong input! "
                        "You must enter a quadratic "
                        "equation in one of the given formats.")

    # a-coefficient - should not be zero!!!
    if res.groupdict()['a'] == "0":
        raise ValueError("The first coefficient should not be zero!")

    return res.groupdict()


if __name__ == "__main__":

    try:
        print("This program will find the roots of a quadratic equation")
        print("Possible input formats:",
              '6*x^2+5*x+6=0',
              '6 * x ^ 2 + 5 * x + 6 = 0',
              'x^2 + 5 = 0',
              '10*x^2= 0',
              '-76*x^2-6*x=0',
              '5x^2-14x-3=0',
              'x^2 + 2.5*x - 1.125=0',
              '7.5*x^2-2.5*x+3=0',
              '2/3*x^2=0',
              sep="\n")

        # -x^2+9=0
        user_input = input("Enter a quadratic equation: ")
        # 1.Check whether the data entered by the user is a quadratic equation
        checked = check_equation(user_input)

        # 2.Remove spaces from the input data
        # coefficients:
        # {'quadratic': '-x^2+9=0', 'a': '-', 'b': None, 'c': '+9'}
        coefficients = del_spaces(checked.items())
        # quadratic_equation: '-x^2+9=0'
        quadratic_equation = coefficients.pop('quadratic')

        # 3.Convert the coefficient of the quadratic equation
        # to the Fraction type
        numbers = convert(coefficients)
        a = numbers['a']
        b = numbers['b']
        c = numbers['c']

        # 4. Get roots and print result to the console
        print(f'Quadratic equation:{quadratic_equation}\n'
              f'Coefficients: a: {float(a)}, b: {float(b)},'
              f' c: {float(c)}\n'
              f'{get_roots(a, b, c)}'
              )

    except ValueError as error:
        print(error.args[0])
    except AttributeError as error:
        print(error)
    except Exception as error:
        print(error)
