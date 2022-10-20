"""
Write a program that converts a decimal number to a binary number.
You can't use out-of-the-box features.
*Example:*

- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""


def convert_to_binary(number: int) -> str:
    """
    The function convert the number of the decimal numeral system to binary numeral system.
    :param number:int.The number of the decimal numeral system that needs to be converted.
    :return: str. String with binary number.
    """
    result = ""

    while number > 0:
        result += str(number % 2)
        number //= 2

    return result[:: -1]


def program_check():
    print("-" * 10, "Program Check", "-" * 10, "\n")
    values = [45, 3, 2, 5]

    for val in values:
        print(f"A decimal number: {val} Binary number: {convert_to_binary(val)}")

    print("-" * 10, "End Program Check", "-" * 10, "\n")


try:
    program_check()
    print("This program converts a decimal number to a binary number.")
    decimal_num = int(input("Enter the number of the decimal numeral system that needs to be converted: "))
    print(f"A decimal number: {decimal_num} Binary number: {convert_to_binary(decimal_num)}")
except ValueError as error:
    print(error)
