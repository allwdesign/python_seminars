"""
Task 5 : Specify a two-dimensional array of integers.
The number of rows and columns is set from the keyboard.
Sort items in ascending order from left to right and top to bottom.
For example, given an array::
1 4 7 2
5 9 10 3
Sorted:
1 2 3 4
5 7 9 10
"""
from random import randint


def test_fill_matrix_random_numbers(rows: int, cols: int) -> None:
    print("-"*10, "Test Fill Matrix Random Numbers", "-"*10)
    matrix = fill_matrix(rows, cols)
    print_matrix("Sorted", matrix)

    print("-" * 10, "End Test Fill Matrix Random Numbers", "-" * 10)


def test_fill_matrix_sorted_numbers(rows: int, cols: int, numbers: list) -> None:
    print("-"*10, "Test Fill Matrix Sorted Numbers", "-"*10)
    matrix = fill_matrix(rows, cols, numbers)
    print_matrix("Sorted", matrix)

    print("-" * 10, "End Test Fill Matrix Sorted Numbers", "-" * 10)


def test_sort(matrix: list, numbers: list) -> None:
    print("-"*10, "Test Sort", "-"*10)
    print_matrix("Initial", matrix)
    sort_list(numbers)
    print("-" * 10, "End Test Sort", "-" * 10)


def test_get_elements(matrix: list) -> None:
    print("-" * 10, "Test Get Elements", "-" * 10)
    numbers = get_elements(matrix)
    print("Joined: ", numbers)
    print("-" * 10, "End Test Get Elements", "-" * 10)


def program_check():
    print("-" * 10, "Program Check", "-" * 10, "\n")
    test_fill_matrix_random_numbers(2, 5)

    matrix1 = [[7, -29, 53], [-92, -100, 88]]
    test_get_elements(matrix1)
    nums1 = get_elements(matrix1)
    test_sort(matrix1, nums1)
    test_fill_matrix_sorted_numbers(2, 3, nums1)

    matrix2 = [[1, 4, 7, 2], [5, 9, 10, 3]]
    test_get_elements(matrix2)
    nums2 = get_elements(matrix2)
    test_sort(matrix2, nums2)
    test_fill_matrix_sorted_numbers(2, 4, nums2)

    print("-" * 10, "End Program Check", "-" * 10, "\n")


def get_elements(matrix: list) -> list:
    """
    Join matrix rows into a numbers list.

    :param matrix: list. 2d matrix(a two-dimensional array of integers).
    :return: list. Unsorted list with integers.
    """
    numbers = list()
    for row in matrix:
        numbers += row

    return numbers


def sort_list(numbers: list) -> None:
    """
    Sort list items in ascending order. Bubble sort method.

    :param numbers: list. Unsorted list with integers.
    :return: None.
    """
    for m in range(len(numbers)-1, 1, -1):
        for i in range(m):
            if numbers[i] > numbers[i + 1]:
                # Swap
                temp = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = temp
    print("Sorted list: ", numbers)


def fill_matrix(rows: int, cols: int, array=None) -> list:
    """
    Fills a matrix with random integers or numbers from a list.

    :param rows: int. The number of row.
    :param cols: int. The number of column.
    :param array: None. Optional argument. If list passed, then
    fill the matrix with elements from this list.
    :return: list. 2d matrix(a two-dimensional array of integers).
    """
    matrix = list()
    k = 0
    for i in range(rows):
        new_row = list()
        for j in range(cols):
            if array:
                number = array[k]
                k += 1
            else:
                number = randint(-100, 100)
            new_row.append(number)
        matrix.append(new_row)
    return matrix


def print_matrix(msg, matrix):
    print(f"{msg} matrix: {matrix}")
    for row in matrix:
        for item in row:
            print(item, end=" ")
        print()


try:
    program_check()

    rows_num = int(input("Enter the number of row: "))
    cols_num = int(input("Enter the number of column: "))

    matrix = fill_matrix(rows_num, cols_num)
    print_matrix("Initial: ", matrix)
    numbers = get_elements(matrix)
    sort_list(numbers)
    sorted_matrix = fill_matrix(rows_num, cols_num, numbers)
    print_matrix("Sorted", sorted_matrix)
except ValueError:
    print("You entered an invalid number!")
except IndexError:
    print("Index out of the range!")