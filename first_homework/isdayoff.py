"""
This program takes in a digit indicating the day of the week and checks whether this day is a day off.

Output:
- 6 -> Yes
- 7 -> Yes
- 1 -> No
- """


def is_dayoff(num: int) -> bool:
    """
    This function takes in a weekday number and checks whether this day is a day off.

    :param num: int. A weekday number.
    :return: bool. Shows whether this day is a day off.
    """
    day_off_numbers = [6, 7]
    answer = False
    if num in day_off_numbers:
        answer = True
    return answer


def print_answer(answer_flag: bool) -> None:
    """
    This function print answer for user.

    :param answer_flag: bool. Use to choose which message to print.
    :return: None.
    """
    if answer_flag:
        print("Yes this is day off")
    else:
        print("This is not day off")


try:
    number = int(input("Enter a weekday number: "))
    print_answer(is_dayoff(number))
except ValueError:
    print("That was no valid number. Try again.")
