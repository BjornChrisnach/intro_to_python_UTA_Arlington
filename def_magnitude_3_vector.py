# Write a function that finds the magnitude of a given 3-dimensional
# vector. The magnitude of a vector is the square root of sum of squares
# of all the components of the vector.
import math


def magnitude_3num_vector(component_list):
    result = math.sqrt(component_list[0]**2 + component_list[1]**2 + component_list[2]**2)
    return result

# or
#
# def _magnitude_of_a_vector_sample_(vector):
#     x = vector[0]
#     y = vector[1]
#     z = vector[2]
#     mag = ((x**2) + (y**2) + (z**2))**(1/2)
#     return mag
