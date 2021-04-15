# Write a function which accepts an input list of numbers and returns the
# smallest number in the list (Do not use python's built-in min() function).
def smallest_number(num_list):
    result = num_list[0]
    for element in num_list:
        if result > element:
            result = element
    return result

# or

# def _find_min_sample_(sample_list):
#     # Initially set the first element
#     # of the list as the minimum
#     my_min = sample_list[0]     # this is your current minimum
#     # Iterate through the list
#     for item in sample_list:
#         # Compare each item from the list
#         # to the current minimum. If the item is smaller
#         # than your current minimum then set that item
#         # to be your current minimum instead
#         if item < my_min:
#             my_min = item
#     # finally return the minimum value
#     return my_min
