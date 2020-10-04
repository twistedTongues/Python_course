import datetime
from numbers import numbers
import os
import time
from generator import generator


def sleep(n):
    time.sleep(n)


def clear_screen():
    os.system('cls')


def get_current_time():
    current_time = datetime.datetime.now().time()
    current_time_str = current_time.strftime("%H.%M.%S")
    return current_time_str


def print_digits(current_time):
    print_line = ""
    for value in range(1, 6):
        for digit in current_time:
            if digit in "0123456789":
                print_line += numbers[digit][value] + '  '
            else:
                line_number = next(generator(current_time))
                if line_number == value:
                    print_line += "\u2588  "
                else:
                    print_line += "   "
        print(print_line)
        print_line = ""
