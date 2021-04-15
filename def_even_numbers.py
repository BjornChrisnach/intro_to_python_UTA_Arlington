# Write a function which accepts an input list of numbers and
# returns a list which includes only the even numbers in the
# input list. If there are no even numbers in the input numbers
# then your function should return an empty list.
def even_numbers(num_list):
    result = []
   for element in num_list :
       if element % 2 ==0 :
           result.append(element)
   return result
# or
    # for i in range(len(num_list)) :
    #     if num_list[i] % 2 == 0 :
    #         result.append(num_list[i])
    # return result
