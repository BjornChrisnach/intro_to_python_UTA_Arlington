# Write a function that accepts a list of integers and returns the average. Assume that the input list
# contains only numbers. Do NOT use the built-in sum() function.
def average_of_list(num_list):
    result_sum = 0
    for element in num_list:
        result_sum = result_sum + element
    result = result_sum / len(num_list)
    return result

# for testing purposes
# print(average_of_list([1, 2, 3, 4, 5]))

# or
#
# def _average_sample_(sample_list):
#     # Initialize total_sum to 0
#     total_sum = 0
#     # Number of elements in sample_list
#     number_of_elements = len(sample_list)
#     # Iterate through the list
#     for item in sample_list:
#         # Add each element to total_sum
#         total_sum = total_sum + item
#     # Calculate the average
#     average = total_sum / number_of_elements
#     # return the average
#     return average
