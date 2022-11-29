"""
Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +,-,/,*. приоритет операций стандартный.
"""
import re

RIGHT_BRACKET = ')'
LEFT_BRACKET = '('

op_priorities = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '(': 3,
    ')': 3,

}
brackets = [LEFT_BRACKET, RIGHT_BRACKET]


def calc(a, b, operation):
    print('calc:', a, b)
    res = 0
    if operation == '*':
        res = a * b
    elif operation == '/':
        try:
            res = a / b
        except ZeroDivisionError:
            print("Division by 0!")
    elif operation == '+':
        res = a + b
    else:
        # operation == '-'
        res = a - b
    return res


def check_priority(digits, ops_stack, current):
    if not ops_stack:
        ops_stack.append(current)


    # Смотрим, что лежит в стеке до этого символа
    before = ops_stack[len(ops_stack) - 1]

    if current == RIGHT_BRACKET:
        while before != LEFT_BRACKET:

            res = calc(digits.pop(len(digits) - 2),
                       digits.pop(len(digits) - 1),
                       ops_stack.pop(len(ops_stack) - 1))
            digits.append(res)
            before = ops_stack[len(ops_stack) - 1]

        # Удаляем символ открывающейся скобки
        ops_stack.pop(len(ops_stack) - 1)
        return

    if before in brackets:
        ops_stack.append(current)
        return

    if op_priorities[current] > op_priorities[before]:
        print('Приоритет больше, чем у предыдущей операции')
        ops_stack.append(current)
        return

    elif op_priorities[current] < op_priorities[before]:
        print('Приоритет меньше, чем у предыдущей операции')
        # ops:[+, *, (, +, /]  '1+2*(3+4/2-(1+2))*2+1'

        res = calc(digits.pop(len(digits) - 2),
                   digits.pop(len(digits) - 1),
                   ops_stack.pop(len(ops_stack) - 1))
        digits.append(res)
        check_priority(digits, ops_stack, current)
    else:
        print('Приоритеты равны')
        res = calc(digits.pop(len(digits) - 2),
                   digits.pop(len(digits) - 1),
                   ops_stack.pop(len(ops_stack) - 1))
        digits.append(res)

        if len(ops_stack) > 1:
            check_priority(digits, ops_stack, current)
        elif len(ops_stack) == 1:
            ops_stack.append(current)
            return
        else:
            ops_stack.append(current)
            return


def check_equation(input_string: str):
    ops_stack = []
    digits = []
    res = 0

    # '1+2*(3+4/2-(1+2))*2+1'
    for i, char in enumerate(input_string):
        if char.isdigit():
            digits.append(float(char))
            print(f'Digits: {digits}')
            if i == len(input_string) - 1:
                res = calc(digits.pop(len(digits) - 2),
                           digits.pop(len(digits) - 1),
                           ops_stack.pop(len(ops_stack) - 1))
        elif char in op_priorities:
            if ops_stack:
                check_priority(digits, ops_stack, char)
            else:
                ops_stack.append(char)
        else:
            raise ValueError('Wrong input!')
        print('Result:', res)


if __name__ == "__main__":

    try:
        print("The program for calculating the arithmetic expression specified "
              "by a string.")
        user_input = '1+2*(3+4/2-(1+2))*2+1'
        user_input2 = '7*3+42'
        #['+', '*', '(', '+', '/', '-', '(', '+', ')', ')', '*', '+']
        ops = re.findall(r'[+*-/)(]', '1+2*(3+4/2-(1+2))*2+1')
        #['1', '2', '3', '4', '2', '1', '2', '2', '1']
        digits = re.findall(r'\d+', '1+2*(3+4/2-(1+2))*2+1')


        print(f'User Input: {user_input}')
        print(f'User Input2: {user_input2}')
        check_equation(user_input)
        check_equation(user_input2)

    except ValueError as error:
        print(error.args[0])
    except AttributeError as error:
        print(error)
    except Exception as error:
        print(error)
