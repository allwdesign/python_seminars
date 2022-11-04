"""
Specify a sequence of numbers. Write a program that displays a list of
non-repeating elements of the original sequence.
"""


def get_sequence() -> list:
    numbers = [num*3 for num in range(0, 7)]
    numbers.extend([3, 4, 9, 0]*2)  # [3, 4, 9, 0, 3, 4, 9, 0]
    return numbers


try:
    sequence = get_sequence()
    print("Original sequence:", sequence)
    print("Sequence with unique numbers:", set(sequence))
except Exception as error:
    print(error)