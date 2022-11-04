import unittest
from fractions import Fraction
from roots_finder import check_equation, del_spaces, convert, get_roots


class TestQuadraticEquation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # with spaces in string
        cls.data_int_coefficients = {
            '6 * x ^ 2 + 5 * x + 6 = 0': {'a': '6', 'b': '+ 5', 'c': '+ 6'},
            '-6*x^2-5*x-6=0': {'a': '-6', 'b': '-5', 'c': '-6'},
            '-76*x^2 - 6*x=0': {'a': '-76', 'b': '- 6', 'c': None},
            '-10 * x^2=0': {'a': '-10', 'b': None, 'c': None},
            '-x^2 - x = 0': {'a': '-', 'b': '- ', 'c': None},
            'x^2 + 0*x +5 = 0': {'a': '', 'b': '+ 0', 'c': '+5'},
            'x^2 + x +5 = 0': {'a': '', 'b': '+ ', 'c': '+5'},
            'x^2+x=0': {'a': '', 'b': '+', 'c': None},
            'x^2 + 5 = 0': {'a': '', 'c': '+ 5', 'b': None},
            '-x^2+9=0': {'a': '-', 'b': None, 'c': '+9'},
            '9*x^2+4=0': {'a': '9', 'b': None, 'c': '+4'},
            '2*x^2-32x=0': {'a': '2', 'b': '-32', 'c': None},
            'x^2=0': {'a': '', 'b': None, 'c': None},
            'x^2-8*x+12=0': {'a': '', 'b': '-8', 'c': '+12'},
            '5*x^2+3*x+7=0': {'a': '5', 'b': '+3', 'c': '+7'},
            '5*x^2-14*x-3=0': {'a': '5', 'b': '-14', 'c': '-3'},
            '-4*x^2+28*x - 49=0': {'a': '-4', 'b': '+28', 'c': '- 49'},
        }
        cls.data_with_fractions_coefficients = {
            'x^2 + 2.5*x - 1.125=0': {'a': '', 'b': '+ 2.5', 'c': '- 1.125'},
            '0.5 * x^2 +0.125*x=0': {'a': '0.5', 'b': '+0.125', 'c': None},
            '7.5*x^2-2.5*x+3=0': {'a': '7.5', 'b': '-2.5', 'c': '+3'},
            '2/3*x^2=0': {'a': '2/3', 'b': None, 'c': None},
        }
        # key is equation with spaces
        # value is dict with equation and coefficients without spaces
        cls.cleaned_data = {
            '6 * x ^ 2 + 5 * x + 6 = 0': {
                'quadratic': '6*x^2+5*x+6=0',
                'a': '6', 'b': '+5', 'c': '+6'},
            '-6*x^2-5*x-6=0': {
                'quadratic': '-6*x^2-5*x-6=0',
                'a': '-6', 'b': '-5', 'c': '-6'},
            '-76*x^2 - 6*x=0': {
                'quadratic': '-76*x^2-6*x=0',
                'a': '-76', 'b': '-6', 'c': None,
            },
            '-10 * x^2=0': {
                'quadratic': '-10*x^2=0',
                'a': '-10', 'b': None, 'c': None,
            },
            '-x^2 - x = 0': {
                'quadratic': '-x^2-x=0',
                'a': '-', 'b': '-', 'c': None},
            'x^2 + 0*x +5 = 0': {
                'quadratic': 'x^2+0*x+5=0',
                'a': '', 'b': '+0', 'c': '+5'},
            'x^2 + x +5 = 0': {
                'quadratic': 'x^2+x+5=0',
                'a': '', 'b': '+', 'c': '+5',
            },
            'x^2+x=0': {
                'quadratic': 'x^2+x=0',
                'a': '', 'b': '+', 'c': None,
            },
            'x^2 + 5 = 0': {
                'quadratic': 'x^2+5=0',
                'a': '', 'c': '+5', 'b': None,
            },
            '-x^2+9=0': {
                'quadratic': '-x^2+9=0',
                'a': '-', 'b': None, 'c': '+9',
            },
            '9*x^2+4=0': {
                'quadratic': '9*x^2+4=0',
                'a': '9', 'b': None, 'c': '+4',
            },
            '2*x^2-32x=0': {
                'quadratic': '2*x^2-32x=0',
                'a': '2', 'b': '-32', 'c': None,
            },
            'x^2=0': {
                'quadratic': 'x^2=0',
                'a': '', 'b': None, 'c': None,
            },
            'x^2-8*x+12=0': {
                'quadratic': 'x^2-8*x+12=0',
                'a': '', 'b': '-8', 'c': '+12',
            },

            '5*x^2+3*x+7=0': {
                'quadratic': '5*x^2+3*x+7=0',
                'a': '5', 'b': '+3', 'c': '+7',
            },
            '5*x^2-14*x-3=0': {
                'quadratic': '5*x^2-14*x-3=0',
                'a': '5', 'b': '-14', 'c': '-3',
            },
            '-4*x^2+28*x - 49=0': {
                'quadratic': '-4*x^2+28*x-49=0',
                'a': '-4', 'b': '+28', 'c': '-49',
            },
        }
        cls.cleaned_data_with_fractions_coefficients = {
            'x^2+2.5*x-1.125=0': {'a': '', 'b': '+2.5', 'c': '-1.125'},
            '0.5*x^2+0.125*x=0': {'a': '0.5', 'b': '+0.125', 'c': None},
            '7.5*x^2-2.5*x+3=0': {'a': '7.5', 'b': '-2.5', 'c': '+3'},
            '2/3*x^2=0': {'a': '2/3', 'b': None, 'c': None},
        }
        cls.converted_with_fractions = {
            'x^2+2.5*x-1.125=0': {
                'a': Fraction(1, 1),
                'b': Fraction(5, 2),
                'c': Fraction(-9, 8),
            },
            '0.5*x^2+0.125*x=0': {
                'a': Fraction(1, 2),
                'b': Fraction(1, 8),
                'c': Fraction(0, 1),
            },
            '7.5*x^2-2.5*x+3=0': {
                'a': Fraction(15, 2),
                'b': Fraction(-5, 2),
                'c': Fraction(3, 1),
            },
            '2/3*x^2=0': {
                'a': Fraction(2, 3),
                'b': Fraction(0, 1),
                'c': Fraction(0, 1),
            }
        }
        cls.converted_with_int = {
            '6*x^2+5*x+6=0': {
                'a': Fraction(6, 1),
                'b': Fraction(5, 1),
                'c': Fraction(6, 1),
            },
            '-6*x^2-5*x-6=0': {
                'a': Fraction(-6, 1),
                'b': Fraction(-5, 1),
                'c': Fraction(-6, 1),
            },
            'x^2+5=0': {
                'a': Fraction(1, 1),
                'c': Fraction(5, 1),
                'b': Fraction(0, 1),
            },
            'x^2+0*x+5=0': {
                'a': Fraction(1, 1),
                'b': Fraction(0, 1),
                'c': Fraction(5, 1),
            },
            'x^2+x+5=0': {
                'a': Fraction(1, 1),
                'b': Fraction(1, 1),
                'c': Fraction(5, 1),
            },
            '-76*x^2-6*x=0': {
                'a': Fraction(-76, 1),
                'b': Fraction(-6, 1),
                'c': Fraction(0, 1),
            },
            '-10*x^2=0': {
                'a': Fraction(-10, 1),
                'b': Fraction(0, 1),
                'c': Fraction(0, 1),
            },
            '5*x^2-14*x-3=0': {
                'a': Fraction(5, 1),
                'b': Fraction(-14, 1),
                'c': Fraction(-3, 1),
            },
            '-x^2-x=0': {
                'a': Fraction(-1, 1),
                'b': Fraction(-1, 1),
                'c': Fraction(0, 1),
            },
            'x^2+x=0': {
                'a': Fraction(1, 1),
                'b': Fraction(1, 1),
                'c': Fraction(0, 1),
            },
            '-x^2+9=0': {
                'a': Fraction(-1, 1),
                'c': Fraction(9, 1),
                'b': Fraction(0, 1),
            },
            '9*x^2+4=0': {
                'a': Fraction(9, 1),
                'c': Fraction(4, 1),
                'b': Fraction(0, 1),
            },
            '2*x^2-32x=0': {
                'a': Fraction(2, 1),
                'b': Fraction(-32, 1),
                'c': Fraction(0, 1),
            },
            'x^2=0': {
                'a': Fraction(1, 1),
                'b': Fraction(0, 1),
                'c': Fraction(0, 1),
            },
            'x^2-8*x+12=0': {
                'a': Fraction(1, 1),
                'b': Fraction(-8, 1),
                'c': Fraction(12, 1),
            },
            '5*x^2+3*x+7=0': {
                'a': Fraction(5, 1),
                'b': Fraction(3, 1),
                'c': Fraction(7, 1),
            },
            '-4*x^2+28*x-49=0': {
                'a': Fraction(-4, 1),
                'b': Fraction(28, 1),
                'c': Fraction(-49, 1),
            },
        }
        cls.expected_int_roots = {
            '6*x^2+5*x+6=0': 'No real roots!',
            '-6*x^2-5*x-6=0': 'No real roots!',
            'x^2+5=0': 'No solutions!',
            'x^2+0*x+5=0': 'No solutions!',
            'x^2+x+5=0': 'No real roots!',
            '-76*x^2-6*x=0': 'First root: x = 0. Second root: x = -0.08.',
            '-10*x^2=0': 'One root: x = 0.',
            '-x^2-x=0': 'First root: x = 0. Second root: x = -1.00.',
            'x^2+x=0': 'First root: x = 0. Second root: x = -1.00.',
            '-x^2+9=0': 'First root: x = 3.00. Second root: x = -3.00.',
            '9*x^2+4=0': 'No solutions!',
            '2*x^2-32x=0': 'First root: x = 0. Second root: x = 16.00.',
            'x^2=0': 'One root: x = 0.',
            'x^2-8*x+12=0': 'First root: x = 6.00. Second root: x = 2.00.',
            '5*x^2+3*x+7=0': 'No real roots!',
            '5*x^2-14*x-3=0': 'First root: x = 3.00. Second root: x = -0.20.',
            '-4*x^2+28*x-49=0': "Two equal roots: x = 3.50."
        }
        cls.expected_fractions_roots = {
            'x^2+2.5*x-1.125=0':
                'First root: x = 0.39. Second root: x = -2.89.',
            '0.5*x^2+0.125*x=0':
                'First root: x = 0. Second root: x = -0.25.',
            '7.5*x^2-2.5*x+3=0': 'No real roots!',
            '2/3*x^2=0': 'One root: x = 0.',
        }

    def test_check_equation_fail(self):
        wrong_data = [
            # not a quadratic equation
            '',
            'x^2+=0',
            '7x',
            '8*x^2',
            '-3.5*x^2-5*x',
            '-3.5 * x ^ 2 - 5 * x =',
            '8.1*x+19=0',
            '7x=0',
            '7*x=0',
            # wrong pow
            '-x^5+9*x-7=0',
            'x^27=0',
            # wrong fractions
            # ..
            '-3..5 * x ^ 2 - 5 * x = 0',
            '-3.5 * x ^ 2 - 5...9 * x = 0',
            '3.5 * x ^ 2 - 5 * x + 4..1 = 0',
            # //
            '-3.5 * x ^ 2 - 5//9 * x = 0',
            '3.5 * x ^ 2 - 5.9 * x + 4//1 = 0',
            '-3//5 * x ^ 2 - 5 * x = 0',
            # ./
            '-3./5 * x ^ 2 - 5 * x = 0',
            '-3../5 * x ^ 2 - 5 * x = 0',
            '-3/.5 * x ^ 2 - 5.9 * x = 0',
            '-3//.5 * x ^ 2 - 5.9 * x = 0',
            '-3//..5 * x ^ 2 - 5.9 * x = 0',

            '-3.5 * x ^ 2 - 5./9 * x = 0',
            '-3.5 * x ^ 2 - 5../9 * x = 0',
            '-3.5 * x ^ 2 - 5..//9 * x = 0',
            '-3.5 * x ^ 2 - 5/.9 * x = 0',

            '-3.5 * x ^ 2 - 5//.9 * x = 0',
            '-3.5 * x ^ 2 - 5///.9 * x = 0',
            '-3.5 * x ^ 2 - 5//..9 * x = 0',

            '3.5 * x ^ 2 - 5.9 * x + 4./1 = 0',
            '3.5 * x ^ 2 - 5.9 * x + 4../1 = 0',
            '3.5 * x ^ 2 - 5.9 * x + 4..//1 = 0',

            '3.5 * x ^ 2 - 5.9 * x + 4//.1 = 0',
            '3.5 * x ^ 2 - 5 * x + 4//..1 = 0',
            '3.5 * x ^ 2 -- 5 * x + 4 = 0',
            # wrong operations ++, --, -+, +-
            '3.5 * x ^ 2 ++ 5 * x + 4 = 0',
            '3.5 * x ^ 2 +- 5 * x + 4 = 0',
            '3.5 * x ^ 2 -+ 5 * x + 4 = 0',
            '3.5 * x ^ 2 + 5.2 * x -- 4 = 0',
            '3.5 * x ^ 2 + 5.2 * x ++ 4 = 0',
            '3.5 * x ^ 2 + 5.2 * x -+ 4 = 0',
            '3.5 * x ^ 2 + 5.2 * x +-- 4 = 0',

            '3.5 * x ^ 2 / 5.2 * x + 4 = 0',
            '3.5 * x ^ 2 * 5.2 * x + 4 = 0',
            '3.5 * x ^ 2 - 5.2 ** x + 4 = 0',
            '3.5 * x ^ 2 - 5.2 * x / 4 = 0',
            '3.5 * x ^ 2 - 5.2 * x * 4 = 0',
            '3.5 * x ^ 2 - 5.2 * x ** 4 = 0',

            '3.5 ** x ^ 2 - 5.2 * x + 4 = 0',
            '3.5 / x ^ 2 - 5.2 * x - 4 = 0',
            '2 / 3 * x^2=0',
        ]
        for equation in wrong_data:
            self.assertRaises(Exception, check_equation, equation)

        a_0_coefficient = '0*x^2+9*x-7=0'
        self.assertRaises(ValueError, check_equation, a_0_coefficient)

    def test_check_equation_with_fraction_coefficients(self):
        for equation in self.data_with_fractions_coefficients:
            self.assertIsNotNone(check_equation(equation))

    def test_check_equation_with_int_coefficients(self):
        for equation in self.data_int_coefficients:
            self.assertIsNotNone(check_equation(equation))

    def test_del_spaces(self):
        for row_equation in self.data_int_coefficients:
            data = {
                **self.data_int_coefficients[row_equation],
                **{'quadratic': row_equation},
            }
            coefficients = del_spaces(data.items())  # type: dict

            self.assertEqual(
                coefficients,
                self.cleaned_data[row_equation],
            )

    def test_convert_with_fractions_coefficients(self):
        cleaned_with_fractions = self.cleaned_data_with_fractions_coefficients

        for key, val in cleaned_with_fractions.items():
            self.assertEqual(
                convert(val),
                self.converted_with_fractions[key],
            )

    def test_convert(self):
        for row_equation in self.cleaned_data:
            # {'quadratic': '-x^2+9=0', 'a': '-', 'b': None,'c': '+9'}
            cleaned = self.cleaned_data[row_equation]

            # ! Method .pop('quadratic') will change the original dictionary
            equation = cleaned['quadratic']

            keys = list(filter(lambda k: k != 'quadratic', cleaned.keys()))

            # {'a': '-', 'b': None,'c': '+9'}
            coefficients = {k: cleaned[k] for k in keys}

            self.assertEqual(
                convert(coefficients),
                self.converted_with_int[equation],
            )

    def test_get_roots(self):
        data = [
            self.converted_with_int,
            self.converted_with_fractions,
        ]
        for dataset in data:
            if dataset == self.converted_with_int:
                expected = self.expected_int_roots
            else:
                expected = self.expected_fractions_roots
            for equation in dataset:
                a = dataset[equation]['a']
                b = dataset[equation]['b']
                c = dataset[equation]['c']

                self.assertEqual(
                    get_roots(a, b, c),
                    expected[equation],
                )

    def test_get_roots_division_by_zero(self):
        with self.assertRaises(
                ZeroDivisionError,
                msg='A divide by zero error was expected'):
            get_roots(Fraction(0, 1), Fraction(-7, 1), Fraction(3, 1))

if __name__ == "__main__":
    unittest.main()
