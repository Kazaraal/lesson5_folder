# # Function to get a number from the user
# def get_number():
#     while True:
#         try:
#             number = int(input("Enter an integer: "))
#             return number
#         except ValueError:
#             print("Please enter a valid integer.")

# # Function to compute the sum of digits of the integer
# def sum_of_digits(number):
#     total = sum(int(digit) for digit in str(abs(number)))  # Convert number to string and sum the digits
#     return total

# # Main flow
# num = get_number()
# digit_sum = sum_of_digits(num)
# print(f"The sum of the digits of {num} is: {digit_sum}")


# GET A TWO-DIGIT NUMBER
# ADD THEM
# MULTIPLY THEM

# def get_number():
#     # Get input of a 2-digit number
#     two_digit_number = input("Enter a 2-digit number: ")
#     # Check if it's a 2-digit number
#     if len(two_digit_number) == 2 and two_digit_number.isdigit():
#         print(two_digit_number)
#         return int(two_digit_number)
#     # Return the number if it is, otherwise ask for input again
#     else:
#         print("Invalid input. Please enter a 2-digit number.")

# get_number()

# def add_numbers(two_digit_number):
#     for number in two_digit_number:
#         print(number)

# add_numbers(two_digit_number)
    
# # def multiply_numbers():

#################################################
# EXAMPLES
#################################################

# EXAMPLE 1
# Greet a list of people
# If they are new, greet them differently

def greet(person, first_time=False):
    if first_time:
        return f"First time for everything, right? Welcome, {person}!"
    else:
        return f"Hello, {person}!"

def greet_all(people):
    for person in people:
        print(greet(person, True))

friends = ["Bob", "Josh", "Austin"]

greet_all(friends)