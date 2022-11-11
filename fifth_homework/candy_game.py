"""
Create a program to play with candy man versus man.
Task Condition: There are 2021 candies on the table. Two players play making
a step after each other. The first step is determined by a draw.
A maximum of 28 candies can be picked up in one turn.
All the opponent's candy goes to the one who made the last step.
"""

from random import choice


INPUT_MSG = "Enter the number of sweets from 1 to 28 that you want to take: "
PLAYER = 'player'
FIRST = 'first'
SECOND = 'second'

who_play_data = {1: FIRST, 2: SECOND}


def do_step(player: int, step: int) -> int:
    max_quantity = 28
    who_play_msg = who_play_data[player]
    print(
        '-'*18,
        f'{who_play_msg.capitalize()} {PLAYER} do step {step}',
        '-'*18,
    )
    number = int(input(INPUT_MSG))
    if number > max_quantity:
        raise ValueError('Value must be less or equal 28!')

    return number


def is_winner(quantity: int, msg: str) -> bool:
    winner = False
    if not quantity:
        print(f'Winner: {msg} {PLAYER}!!!')
        winner = True
    return winner


def calc(q: int, num: int) -> int:
    q -= num
    return q


def play(candy: int, beginer: int) -> None:
    first_pl = dict()
    second_pl = dict()
    step = 0
    quantity = candy
    who_play = beginer

    while quantity > 0:
        step += 1
        msg = who_play_data[who_play]
        num = do_step(who_play, step)
        quantity = calc(quantity, num)
        if who_play == 1:
            first_pl[step] = num
        else:
            second_pl[step] = num

        if is_winner(quantity, msg):
            print('-'*20, 'All player steps', '-'*20)
            print(who_play_data[1].capitalize(), PLAYER, 'steps:', first_pl)
            print(who_play_data[2].capitalize(), PLAYER, 'steps:', second_pl)
            break

        # Who to start with the next step:
        # if the last to make the move 1st, then from the 2nd else 1st
        who_play = 2 if who_play == 1 else 1

        print(f'It was {candy} candy.'
              f'{msg.capitalize()} {PLAYER} take: {num}.')
        print(f'Candy left: {quantity}.')


if __name__ == "__main__":
    try:
        # Return a random element from the non-empty sequence seq.
        draw = choice([1, 2])
        candy = 2021
        player_str = who_play_data[draw]

        print('This program to play with candy man versus man.')
        print('-'*20, 'Rules of the game', '-'*20)
        print('1. There are 2021 candies on the table.\n'
              '2. Two players play making a step after each other.\n'
              '3. The first step is determined by a draw.\n'
              '4. A maximum of 28 candies can be picked up in one turn.\n'
              '5. All the opponent\'s candy goes to the one who made the last '
              'step.')
        print('-' * 60)
        print(f'Goes first: {player_str} {PLAYER}.')
        print('-' * 60)

        play(candy, draw)

    except ValueError as error:
        print(error.args[0])
    except Exception as error:
        print(error)
