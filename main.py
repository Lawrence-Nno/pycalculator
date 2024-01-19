import math

calc_ascii = """
 _____________________
|  _________________  |
| | Lawrence     0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""

def add(arg1, *args):
    """
    This function calculates the sum of it's inputs
    :param arg1: An Integer or float
    :param args: Integers or/and floats
    :return: The sum of the inputs
    """
    total = arg1
    for arg in args:
        total += arg
    return total


def subtract(arg1, *args):
    """
    This function subtracts the subsequent inputs(*args) from the first entered input(arg1)
    :param arg1: An Integer or float to be subtracted from
    :param args: Integers or/and floats that will be subtracted from arg1
    :return: The result of the subtraction
    """
    total = arg1
    for arg in args:
        total -= arg
    return total


def multiply(arg1, *args):
    """
    This function multiplies the inputs
    :param arg1: An integer/float
    :param args: Integers/Floats
    :return: The result of the multiplication
    """
    total = arg1
    for arg in args:
        total *= arg
    return total


def divide(arg1, *args):
    """
    This function divides the first number inputted in it with the subsequent numbers
    :param arg1: The first number to be divided.
    :param args: The subsequent numbers to divide with.
    :return: The result of the division
    """
    total = arg1
    for arg in args:
        total /= arg
    return total


def percent_of(percent, num):
    """
    This function calculates the percentage of any number
    :param percent: The percent of the number seek
    :param num: The number you want to know its percentage
    :return: The percentage
    """
    total = (percent/100) * num
    return total


def log_to_base(num, base):
    """
    This function calculates the logarithm of any number to any base.
    :param num:The number whose logarithm you want to know.
    :param base: The base of the logarithm
    :return: The result of the calculation
    """
    if base == 1:
        print("Log 1 is always 0, choose a diff base")
        return None
    else:
        total = math.log(num) / math.log(base)
        return total


def log_to_base_10(num):
    """
    This function calculates the logarithm to base 10 of any number.
    :param num: The number.
    :return: The result.
    """
    total = math.log(num)
    return total


def num1():
    while True:
        try:
            number_1 = float(input("Choose your initial number\n"))
        except ValueError:
            print("Number has to be an integer or a float")
        else:
            break
    return number_1


def num2():
    while True:
        try:
            number_2 = float(input("Choose a subsequent number\n"))
        except ValueError:
            print("Number has to be an integer or a float")
        else:
            break
    return number_2


def choose_operation():
    for operate in operation:
        print(operate, end="  ")
    while True:
        ops = input("Choose an operation:\n")
        if ops in operation:
            break
        else:
            print("Choose a valid operation")
    return ops


operation = {
    '+': add,
    '-': subtract,
    '/': divide,
    '*': multiply,
    '%': percent_of,
    'log_b': log_to_base,
    'log_10': log_to_base_10
}

print(calc_ascii)
ops_ = choose_operation()
num1_ = num1()
num2_ = num2()

chosen_func = operation[ops_]
result = chosen_func(num1_, num2_)
print(result)
while True:
    go_on = input("Do you want to calculate further with this result? Type 'yes' or 'no\n")
    if go_on == 'yes':
        ops_ = choose_operation()
        num2_ = num2()
        chosen_func = operation[ops_]
        result = chosen_func(result, num2_)
        print(result)
    else:
        break




