def greet():
    print("Hello, World!")

# Function is defined but not called, so nothing happens.
Fix:


greet()  # Now it executes and prints "Hello, World!"

def add(a, b):
    return a + b

result = add  # Function reference assigned, but not executed
print(result)
Fix:


result = add(5, 3)
print(result)  # Output: 8

def show():
    print("Function executed")

# Accidentally using parentheses when assigning
x = show()  
print(x)  # None, because function has no return
Fix:

x = show  # Assign function reference without calling
x()  # Calls the function properly


