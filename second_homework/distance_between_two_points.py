"""
The program takes input N, and the coordinates of two points and finds
the distance between them in N-dimensional space.

For 2D:
A (3,6); B (2,1) -> 5.10
A (7,-5); B (1,-1) -> 7.21

For 3d:
A (3,6,8); B (2,1,-7), -> 15.84
A (7,-5, 0); B (1,-1,9) -> 11.53
"""
from decimal import Decimal


def get_distance(point_a: tuple, point_b: tuple, dimention: int) -> Decimal:
    """
    The function calculates the distance between two points in N-dimensional space.

    :param a: tuple. The coordinates for A point.
    :param b: tuple. The coordinates for B point.
    :param dimention: int. The quantity of dimentions.
    :return: Decimal. The distance between two points in N-dimensional space.
    """
    result = Decimal()
    sum_of_squares = Decimal()
    sqrt = Decimal(0.5)

    for i in range(dimention):
        coordinate_a, coordinate_b = point_a[i], point_b[i]
        # the quantity  of coordinates depends on quantity of dimention (x, y, z, etc.)
        sum_of_squares += (coordinate_a - coordinate_b)**2

    result = sum_of_squares**sqrt

    return result


def convert_totuple(string: str) -> tuple:
    """
    Convert string to tuple with integers coordinates for point.

    :param string: str. The string with coordinates for point.
    :return: tuple. The tuple with integers coordinates for point.
    """
    string_numbers = string.split(',')
    coordinates = tuple([int(s_num) for s_num in string_numbers])
    return coordinates


def print_result(point_a: tuple, point_b: tuple, distance: Decimal) -> None:
    """
    The function print result to console.

    :param point_a: tuple. The coordinates for A point.
    :param point_b: tuple. The coordinates for B point.
    :param distance: Decimal. The distance between two points in N-dimensional space.
    :return: None.
    """
    print(f'A point: {point_a}',
          f'B point: {point_b}',
          '-> {:.2f}'.format(distance))


def program_check():
    print("-" * 10, "Program Check", "-" * 10)
    data = [((3, 6), (2, 1), 2),
            ((7, -5), (1, -1), 2),
            ((3, 6, 8), (2, 1, -7), 3),
            ((7, -5, 0), (1, -1, 9), 3)]

    for point_a, point_b, dimention in data:
        print("-" * 30)
        distance = get_distance(point_a, point_b, dimention)
        print_result(point_a, point_b, distance)
    print("-" * 10, "End Program Check", "-" * 10, "\n")


try:
    program_check()
    print("The program takes input N, and the coordinates of two points and finds "
          "the distance between them in N-dimensional space.")
    print("Coordinates must be separated by commas without spaces. Example: 3,6,8 or 2,1,-7")
    dimention = int(input("Enter a number of dimentions: "))

    point_a = input("Enter a coordinates for A point: ")
    point_b = input("Enter a coordinates for B point: ")

    point_a = convert_totuple(point_a)
    point_b = convert_totuple(point_b)

    if dimention == len(point_a) == len(point_b):
        distance = get_distance(point_a, point_b, dimention)
        print_result(point_a, point_b, distance)
    else:
        raise ValueError("The quantity of coordinates must be equal to the quantity of dimentions.")

except ValueError as e:
    print(e.args[0])