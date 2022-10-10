"""
The program takes coordinates as input points (X and Y),
with X ≠ 0 and Y ≠ 0. And return the number of a quarter of the plane in which this point is located.

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
"""


def get_quarter(x: int, y: int) -> str:
    """
    Checks the coordinates of a point and return a string with coordinate quarter it is located.

    :param x: int. x - coordinate of point.
    :param y: int. y - coordinate of point.
    :return: str. String with the number of the quarter in which the point is located.
    """
    msg_quarter = ""
    if x > 0 and y > 0:
        msg_quarter = "1st"
    elif x < 0 and y > 0:
        msg_quarter = "2nd"
    elif x < 0 and y < 0:
        msg_quarter = "3nd"
    else:
        msg_quarter = "4th"
    return msg_quarter


try:
    x = int(input("Enter x coordinates for point: "))
    y = int(input("Enter y coordinates for point: "))
    if x == 0 or y == 0:
        raise ValueError

    str_quarter = get_quarter(x, y)

    print(f"The point ({x}, {y}) is in the {str_quarter} quarter")

except ValueError:
    print("X and Y should be a number but X ≠ 0 and Y ≠ 0")