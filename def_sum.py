# Write a function that accepts a list of integers and returns the sum
# of all the numbers in the list. Assume that the input list contains
# only numbers. Do NOT use the built-in sum() function.
def return_sum(list):
    result = 0
#   for element in list :
#       result = result + element
#   return result
    for i in range(len(list)):
        result = result + list[i]
    return result
