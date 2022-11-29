"""
Create a program to play 'noughts and crosses'. Human vs Bot.
"""

from random import choice
from x0_bot import do_bot_step

CHOICE_MSG = 'Enter the noughts(0) or crosses(x): '
WHAT_POSITION = 'Enter the coordinates where to place the '
FORMAT = ' in the specified format (row, column):'
PLAYER = 'player'
HUMAN = 'human'
BOT = 'bot'

who_play_data = {1: HUMAN, 2: BOT}


def get_values(coordinates, field):
    values = list()
    # key: 'left_top_diagonal' or 'right_top_diagonal'
    for key in coordinates:
        if key == 'left_top_diagonal' or key == 'right_top_diagonal':
            values.append(
                ''.join([field[row][col] for row, col in coordinates[key]]))
        else:
            # key: 'rows' or 'columns'
            # rows: [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)),
            #       ((2, 0), (2, 1), (2, 2))]
            for items in coordinates[key]:
                values.append(''.join([field[row][col] for row, col in items]))

    return values


def get_coordinates(field):
    r_temp = list()
    c_temp = list()
    rows = list()
    columns = list()
    coordinates = dict()
    size = len(field)  # 3

    # [(0,0), (1,1), (2,2)] from left top to right bottom
    coordinates['left_top_diagonal'] = [(i, i) for i in range(size)]
    # from right top to left bottom
    # range(2, -1, -1) => 2, 1, 0 for right diagonal
    j_range = range(size - 1, -1, -1)
    # range(3) => 0, 1, 2
    i_range = range(size)
    # [(0, 2), (1, 1), (2, 0)] from right top to left bottom
    coordinates['right_top_diagonal'] = list(zip(i_range, j_range))

    for i in range(size):
        for j in range(size):
            r_temp.append((i, j))
            c_temp.append((j, i))
        # Important: temp is a mutable object, we have to convert it to a tuple
        rows.append(tuple(r_temp))
        columns.append(tuple(c_temp))

        r_temp.clear()
        c_temp.clear()
        # rows = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)),
        #         ((2, 0), (2, 1), (2, 2))]
        coordinates['rows'] = rows
        # columns=[((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)),
        #          ((0, 2), (1, 2), (2, 2))]
        coordinates['columns'] = columns
    return coordinates


def print_all_steps(first_pl, second_pl):
    print('-' * 20, 'All player steps', '-' * 20)
    print(who_play_data[1].capitalize(), PLAYER, 'steps:', first_pl)
    print(who_play_data[2].capitalize(), PLAYER, 'steps:', second_pl)


def print_field(field):
    for row in field:
        for column in row:
            print('|', column, end=' ')
        print('|')
        continue


def is_winner(coords: dict, field: list) -> bool:
    winner = False
    # values: ['x0-', 'x0-', 'x0x', 'x0-', '---', 'xx-', '00-', 'x--']
    values = get_values(coords, field)
    if ('000' in values) or ('xxx' in values):
        winner = True
    return winner


def in_the_range(row: int, column: int) -> bool:
    start = 0
    end = 2
    flag = False
    # if both coordinate values in the range [0, 2]
    if (start <= row <= end) and (start <= column <= end):
        flag = True
    return flag


def humanize_coordinates(row: int, column: int) -> tuple:
    # Humanize coordinate: (1, 1) Not: (0, 0)
    return row + 1, column + 1


def do_human_step(user_char: str, field: list, free_cells: list) -> tuple:
    """
    Enter and save the coordinates of a free cell to put the char it got
    (cross or noughts).

    :param user_char: str. Cross or noughts.
    :param field: list with chars: '-' or 'x' or '0'
    :param free_cells: list with coordinates of free cells.
    :return: tuple with coordinates.
    """
    user_input = input(WHAT_POSITION + user_char + FORMAT)
    # Index value for the program: reduce indexes because matrix indexes
    # start with 0,0
    row, column = [int(el.strip()) - 1 for el in user_input.split(',')]

    if not in_the_range(row, column):
        raise ValueError('Value value must be between 1 and 3 inclusive!')

    if (row, column) not in free_cells:
        raise ValueError('This cell is already taken!')

    if user_char not in 'x0':
        raise ValueError('Value value must be 0 or x!')

    field[row][column] = user_char
    # Remove all occurrences of these coordinates
    free_cells.pop(free_cells.index((row, column)))
    # Return humanize coordinate
    return row, column


def play(beginer: int) -> None:
    # Don't do this : [['-'] * 3] * 3
    field = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    coordinates = get_coordinates(field)
    # free_cells: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2),
    #              (2, 0), (2, 1), (2, 2)]
    free_cells = [el for item in coordinates['rows'] for el in item]
    human_steps = dict()
    bot_steps = dict()
    choices = dict()
    step = 0
    who_play = beginer
    print_field(field)

    # If 1st play Human: what char he wants to play OR
    # If 1st play Bot: random choice char
    user_choice = input(CHOICE_MSG).lower() if who_play == 1 else choice('x0')
    # Char for another player
    another_user_choice = '0' if user_choice == 'x' else 'x'
    # Save user choice
    choices[who_play] = user_choice
    choices[2 if who_play == 1 else 1] = another_user_choice

    # step < 9
    while step < len(field) ** 2:
        step += 1
        msg = who_play_data[who_play]
        print('-' * 18, f'{msg.capitalize()} {PLAYER} do step {step}',
              '-' * 18)

        if who_play == 1:
            # Human step
            row, col = do_human_step(choices[who_play],
                                     field,
                                     free_cells)
            # For information output
            human_steps[step] = humanize_coordinates(row, col)
        else:
            # Bot step
            row, col = do_bot_step(choices[who_play], field, free_cells)
            row, col = humanize_coordinates(row, col)

            print(WHAT_POSITION, choices[who_play], FORMAT, f'{row}, {col}')
            # For information output
            bot_steps[step] = row, col

        print_field(field)
        if step > 4:
            if is_winner(coordinates, field):
                print(f'Winner: {msg} {PLAYER}: {choices[who_play]}!!!')
                print_all_steps(human_steps, bot_steps)
                break

        # Who to start with the next step:
        # if the last to make the move 1st, then from the 2nd else 1st
        who_play = 2 if who_play == 1 else 1
    else:
        print("Drawn game!")
        print_all_steps(human_steps, bot_steps)


if __name__ == "__main__":
    try:
        # Return a random element from the non-empty sequence.
        draw = choice([1, 2])

        player_str = who_play_data[draw]

        print('This program to play noughts and crosses.')
        print('-' * 20, 'Rules of the game', '-' * 20)
        print('1. This game for two players (human vs bot) who take turns '
              'marking the spaces in a three-by-three grid with X or O.\n'
              '2. Two players play making a step after each other.\n'
              '3. The first step is determined by a draw.\n'
              '4.  The player who succeeds in placing three of their marks in'
              ' a horizontal, vertical, or diagonal row is the winner.\n')
        print('-' * 60)
        print(f'Goes first: {player_str} {PLAYER}.')
        print('-' * 60)

        play(draw)

    except ValueError as error:
        print(error.args[0])
