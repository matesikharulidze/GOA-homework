def simple_calculator(num1, num2, operation):
    """
    Performs basic arithmetic operations based on the provided operation string.
    """
    if operation == "addition":
        return num1 + num2
    elif operation == "subtraction":
        return num1 - num2
    elif operation == "multiplication":
        return num1 * num2
    elif operation == "division":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation."

# Call the function with various operations and print the results
print(simple_calculator(10, 5, "addition"))        # Output: 15
print(simple_calculator(10, 5, "subtraction"))     # Output: 5
print(simple_calculator(10, 5, "multiplication"))  # Output: 50
print(simple_calculator(10, 0, "division"))        # Output: Error: Division by zero is not allowed.
print(simple_calculator(10, 5, "division"))        # Output: 2.0
