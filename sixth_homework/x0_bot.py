from random import choice


def do_bot_step(user_char: str, field: list, free_cells: list) -> tuple:
    """
    Selects random coordinates of a free cell to put the char it got
    (cross or noughts)

    :param user_char: str. Cross or noughts.
    :param field: list with chars: '-' or 'x' or '0'
    :param free_cells: list with coordinates of free cells.
    :return: tuple with coordinates.
    """
    row, column = free_cells.pop(free_cells.index(choice(free_cells)))
    field[row][column] = user_char

    return row, column


