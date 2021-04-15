# Write a function that accepts a number x and evaluates the
# following polynomial expression: y=x4−12x3+13x2+11 and returns
# the value of y

# given x**4 - 12*x**3 + 13*x**2 + 11
def polynomial_exp(num_x):
    result = num_x**4 - 12*num_x**3 + 13*num_x**2 + 11
    return result

# or
# def _evaluate_expression_sample3_(x):
#     y = x**4 - 12*x**3 + 13*x**2 + 11
#     return y
