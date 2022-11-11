"""
Given a list of numbers. Create a list containing the numbers that describe
the maximum increasing sequence. The order of the elements cannot be changed.

Examples:
[1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
[1, 5, 2, 3, 4, 1, 7, 8, 15, 1] => [1, 5]
"""


def get_max_ascending_sequence(nums: list):
    """
    Creates and returns a list containing numbers that describe the maximum
    ascending sequence or message 'No max ascending sequence!'.

    :param nums: list with numbers.
    :return: list with [min_value, max_value_in_sequence] or message.
    """
    min_value = min(nums)
    max_value_in_sequence = min_value
    while max_value_in_sequence + 1 in nums:
        max_value_in_sequence += 1
    if min_value == max_value_in_sequence:
        return 'No max ascending sequence!'
    return [min_value, max_value_in_sequence]


try:
    data = [
            [1, 5, 2, 3, 4, 6, 1, 7],
            [1, 5, 2, 3, 4, 1, 7, 8, 15, 1],
            [1, 2, 8, 12, 3, 4, 1, 7],
            [5, 2, 3, 4, 7, 8, 15],
            [5, 9, 13, 24, 17, 1],
    ]
    for numbers in data:
        print(f'{numbers} => {get_max_ascending_sequence(numbers)}')

except Exception:
    print('Something went wrong!')

