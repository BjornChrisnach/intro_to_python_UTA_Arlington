# Write a function that normalizes a vector (finds the unit vector).
# A vector can be normalized by dividing each individual component
# of the vector by its magnitude. Your input for this function will
# be a vector i.e. 1 dimensional list containing 3 integers.
def normalize_vector(vector):
    result = []
    x = vector[0]
    y = vector[1]
    z = vector[2]
    mag = ((x**2) + (y**2) + (z**2))**(1/2)
    for element in vector:
        unit_vector = element / mag
        result.append(unit_vector)
    return result

# or
#
# def _unit_vector_sample_(vector):
#     # calculate the magnitude
#     x = vector[0]
#     y = vector[1]
#     z = vector[2]
#     mag = ((x**2) + (y**2) + (z**2))**(1/2)
#     # normalize the vector by dividing each component with the magnitude
#     new_x = x/mag
#     new_y = y/mag
#     new_z = z/mag
#     unit_vector = [new_x, new_y, new_z]
#     return unit_vector
