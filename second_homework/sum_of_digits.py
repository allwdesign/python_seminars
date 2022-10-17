"""
Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр.
Через строку нельзя решать.
*Пример:*

- 6782 -> 23
- 0,56 -> 11
"""
from fractions import Fraction


def sum_of_digits(number: Fraction) -> int:
    """

    :param number: Fraction.
    :return:
    """
    sum = 0
    fractional_part = Fraction((number - int(number)))  # 1.23 - 1 = 0.23

    while fractional_part > 0:
        number = number * 10  # 12.3
        temp = fractional_part * 10  # 2.3
        digit = int(temp)  # 2.3 return 2
        fractional_part = temp - digit  # 2.3 - 2 = 0.3

    while number > 0:
        digit = number % 10
        number //= 10
        sum += int(digit)

    return sum


def program_check():
    print("-" * 10, "Program Check", "-" * 10)
    data = ["6782", "0.56", "111.23",
            "45", "714.3", "500.3",
            "197.22", "16.232", "54211.85643"]

    for num in data:
        print("-" * 30)
        res = sum_of_digits(Fraction(num))
        print(f"Number: {num} -> {res}")
    print("-" * 10, "End Program Check", "-" * 10, "\n")


try:
    program_check()
    number = Fraction(input("Enter a number: "))
    print(f"Number: {float(number)} -> {sum_of_digits(number)}")
except ValueError:
    print("You entered wrong value!")


