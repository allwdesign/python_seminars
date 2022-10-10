"""
Write a simple calculator that reads three strings from user input: the first number, the second number, and
operation, after which it applies the operation to the entered numbers ('first number' 'operation' 'second number')
and outputs result on screen.
Supported operations: +, -, /, *, mod, pow, div, where
mod is taking the remainder of the division,
pow - exponentiation,
div is an integer division.
If division is being performed and the second number is 0, output the string 'Division by 0!'.
Please note that real numbers come to the input of the program.
Sample Input 1:
5.0
0.0
mod
Sample Output 1:
Division by 0!
Sample Input 2:
-12.0
-8.0
*
Sample Output 2:
96.0
Sample Input 3:
5.0
10.0
/
Sample Output 3:
0.5
"""
from decimal import Decimal


permitted_operations = ["+", "-", "/", "*", "mod", "pow", "div"]
divide_operations = ["/", "mod", "div"]


def calculate(a: Decimal, b: Decimal, operation: str) -> None:
    """
    Applies mathematical operations from the permitted list to numbers and displays the result on the screen.

    :param a: Decimal. Number A.
    :param b: Decimal. Number B.
    :param operation: str. Mathematical operations applies to number A and number B.
    :return: None. Displays the result on the screen.
    """
    if operation not in permitted_operations:
        raise ValueError("You must enter permitted operations!")

    if operation in divide_operations and not b:
        raise ZeroDivisionError

    result = Decimal(0.0)

    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "pow":
        result = a ** b
        operation = "**"
    elif operation == "/":
        result = a / b
    elif operation == "mod":
        result = a % b
        operation = "%"
    elif operation == "div":
        result = a // b
        operation = "//"
    else:
        raise ValueError

    print('{:.2f} {} {:.2f} = {:.2f}'.format(a, operation, b, result))


try:
    print("This program is a simple calculator")
    print("Supported operations: +, -, /, *, mod, pow, div")

    first_number = Decimal(input("Enter first number: "))
    second_number = Decimal(input("Enter second number: "))

    operation = input("Enter what kind operation do you want: ")

    calculate(first_number, second_number, operation)

except ValueError as e:
    print("Wrong value!", e)
except ZeroDivisionError:
    print("Division by 0!")
except TypeError:
    print("TypeError")



