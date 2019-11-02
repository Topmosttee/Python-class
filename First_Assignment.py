# Function to find the squareroot of any number
number = int(input("Enter a number to find the square root: "))
if number<0:
    print("Please enter a number higher than zero")
else:
    sqrroot = number**0.5

print("Square root of {} is {}".format(number,sqrroot))