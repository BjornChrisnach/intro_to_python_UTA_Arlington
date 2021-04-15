# Write a function that accepts two positive integers which are the height
# and width of a rectangle and returns a list that contains the area and perimeter
# of that rectangle.

def area_perimeter_rectangle(height, width):
    result = []
    result_area = height * width
    result_perim = 2*(height + width)
    result.append(result_area)
    result.append(result_perim)
    return result


# for testing purposes
print(area_perimeter_rectangle(4, 5))

# or
#
# def _rectangle_sample_(length, breadth):
#     # Calculate the area
#     area = length * breadth
#     # Calculate the perimeter
#     perimeter = 2*length + 2*breadth
#     # Put area and perimeter
#     # in a list called "output_list"
#     output_list = [area, perimeter]
#     # return output_list
#     return output_list
