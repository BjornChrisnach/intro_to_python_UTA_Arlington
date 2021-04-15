# Write a function that finds the distance between two points and returns it.
# The distance between two points with x,y, and z components can be calculated as:
# distance=(x2−x1)2+(y2−y1)2+(z2−z1)2 The input for this function will be two 1
# Dimensional lists that contain the x,y,z coordinates each.
import math


def distance_betw_2_points(num_list_a, num_list_b):
    num1_a = num_list_a[0]
    num2_a = num_list_a[1]
    num3_a = num_list_a[2]
    num1_b = num_list_b[0]
    num2_b = num_list_b[1]
    num3_b = num_list_b[2]
    result = math.sqrt(((num1_b-num1_a)**2) + ((num2_b-num2_a)**2) + ((num3_b-num3_a)**2))
    return result

# for testing purposes
# print(distance_betw_2_points([2, 3, -5], [4, -3, 12]))

# or
#
# def _find_distance_sample_(a, b):
#     x1, y1, z1 = a[0], a[1], a[2]
#     x2, y2, z2 = b[0], b[1], b[2]
#     distance = ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2 )**(1/2)
#     return distance
