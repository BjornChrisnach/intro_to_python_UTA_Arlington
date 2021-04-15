# This function calculates and returns the square root
# of the number wich is given to it as input

def my_square_root(input_number):
    square_root = input_number/2
    accuracy = 0.001
    while abs(input_number-(square_root**2)) > accuracy:
        print(square_root)
        square_root = (square_root+(input_number/square_root))/2
        print(square_root)
    return square_root
# This is the main program to check the my_square_root function


for x in range(1, 21):
    y = my_square_root(x)
    print("Square root of ", x, " is ", y)
