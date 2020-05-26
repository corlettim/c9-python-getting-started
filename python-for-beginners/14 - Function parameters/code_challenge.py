# Create a calculator function
# The function should accept three parameters:
# first_number: a numeric value for the math operation
# second_number: a numeric value for the math operation
# operation: the word 'add' or 'subtract'. The default operation is 'add'
# the function should return the result of the two numbers added or subtracted
# based on the value passed in for the operator
#
# Test your function using named notation passing in only the numbers 6 and 4
# Should return 10
#
# Test your function using named notation with the values 6,4, subtract
# Should return 2
#
# BONUS: Test your function with the values 6, 4 and divide
# Have your function return an error message when invalid values are received


def calculator(first, second, operation = "add"):
    if operation == "add":
        add = float(first_number) + float(second_number)
        return add
    elif operation == "subtract":
        sub = float(first_number) - float(second_number)
        return sub
    else:
        error = "That operation is not possible"
        return error

first_number = float(input("Please enter a number: "))
second_number = float(input("Please enter another number: "))

# first attempt was to ask for which operation they would like
# however that does not work because they will have to have the option of add or subtract
# and therefore there would be no default of addition
# this we must pass the operation ourselves ad coders rather than it being left up to the user

print("Adding: ", calculator(first_number, second_number))
print("Subtracting: ", calculator(first_number, second_number, operation="subtract"))
print("ERROR: ", calculator(first_number, second_number, operation="divide"))
