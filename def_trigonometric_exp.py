# Write a function that accepts a number x and evaluates the following
# expression: y=sin(x)−cos(x)+sin(x)cos(x) and returns the value of y.
# (Hint: Use math module)
import math


def trigonometric_expressions(num_x):
    result = math.sin(num_x) - math.cos(num_x) + math.sin(num_x) * math.cos(num_x)
    return result

# or
#
# import math
# def _evaluate_expression_sample3_(x):
#     y = math.sin(x) - math.cos(x) + math.sin(x)*math.cos(x)
#     return y
