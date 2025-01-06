def calculate_operations(x, y):
    """
    Performs basic arithmetic operations on x and y.
    """
    results = {
        "addition": x + y,
        "subtraction": x - y,
        "multiplication": x * y,
        "integer_division": x // y if y != 0 else "Error: Division by zero"
    }
    return results

# ფუნქციის გამოძახება და შედეგების ბეჭდვა
x = 10
y = 5
operations = calculate_operations(x, y)
for operation, result in operations.items():
    print(f"{operation.capitalize()}: {result}")
