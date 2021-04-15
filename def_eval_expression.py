# Write a function that accepts a number x and evaluates the following expression:
# y=abs(x3)+cos(3x−−√) and returns the value of y. Hint: Use the math module!
import math


def evaluate_expression(num_x):
    result = abs(math.pow(num_x, 3)) + math.cos(math.sqrt(3*num_x))
    return result

# or
#
# import math
# def _evaluate_expression_sample3_(x):
#     y = abs(x**3) + math.cos(math.sqrt(3*x))
#     return y
