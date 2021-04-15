# Write a function which accepts an input list of numbers and returns the largest number in the list
# (Do not use python's built-in max() function).
def find_maximum_of_list(num_list):
    result = num_list[0]
    for element in num_list:
        if result < element:
            result = element
    return result

# for testing purposes
#print(find_maximum_of_list([1, 0, 2, 3, 8, 9, 4]))

# or
#
# def _find_max_sample_(sample_list):
#     # Initially set the first element
#     # of the list as the maximum
#     my_max = sample_list[0]     # this is the current maximum
#     # Iterate through the list
#     for item in sample_list:
#         # Compare each item from the list
#         # to the current maximum. If the item is larger
#         # than your current maximum then set that item
#         # to be your current maximum instead
#         if item > my_max:
#             my_max = item
#     # finally return the maximum value
#     return my_max
