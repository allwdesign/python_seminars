"""
Generate an array of random integers with dimensions m*n (the dimension is entered from the keyboard),
and so that the number of elements is even. Display a beautiful table on the screen.
Randomly shuffle the elements of an array so that each is guaranteed to move
to another place and do it in m*n / 2 iterations. That is, if the array is three by four, then it is necessary
perform no more than 6 iterations. And then at the end again display it as a table.
"""
from random import randint, randrange, choice


def shuffle_matrix(numbers: list):
    """
    Shuffles the matrix. We mix the first element and the last
    element as a pair, the second and penultimate element, etc.

    # :param numbers: list of integer numbers.
    # :param times:
    # :return:
    """
    length = len(numbers)

    for i in range(length // 2):
        numbers[i], numbers[length - 1 - i] = numbers[length - 1 - i], numbers[i]

    return numbers


def get_matrix(rows: int, cols: int, uniq_numbers: list) -> list:
    """
    Fills a matrix with random unique integer numbers from a list.

    :param rows: int. The number of row.
    :param cols: int. The number of column.
    :param uniq_numbers: list. We fill the matrix with elements from this list.
    :return: list - matrix.
    """
    matrix = []

    for i in range(rows):
        row = [uniq_numbers[i] for i in range(cols)]
        matrix.append(row)
        uniq_numbers = uniq_numbers[cols:]

    return matrix


def get_unique_numbers(size: int, diapozone) -> list:
    """
    Creates a list of unique integers.

    :param size: int. Size to create a list with unique elements.
    :param diapozone: int. Use for create a random integer from [0; diapozone - 1].
    :return: list with unique integer numbers.
    """
    unique_numbers = set()
    while len(unique_numbers) < size:
        # randrange(diapozone) returns a random integer from [0; diapozone - 1]
        unique_numbers.add(randrange(diapozone))

    return list(unique_numbers)


def print_matrix(matrix: list, msg: str) -> None:
    """
    Formatted output of the matrix to the console.

    :param matrix: list.
    :param msg: str.
    :return: None.
    """
    print(f"{msg} Matrix:")
    for row in matrix:
        print(str(row), sep='\t')


try:
    print("Generate an array of random integers with dimensions m*n.\n"
          "Shuffles the matrix. We mix the first element and the last "
          "element as a pair, the second and penultimate element, etc.")
    rows_num = int(input("Enter the number of row: "))
    cols_num = int(input("Enter the number of column: "))

    if cols_num % 2 != 0:
        raise ValueError("The number of elements must be even!")

    numbers = get_unique_numbers(rows_num * cols_num, 100)

    matr = get_matrix(rows_num, cols_num, numbers)
    print_matrix(matr, "Original")
    shuffle_nums = shuffle_matrix(numbers)
    print_matrix(get_matrix(rows_num, cols_num, shuffle_nums), "Shuffle")
except ValueError as error:
    print(error)
