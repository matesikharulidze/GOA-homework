def greet(name):
    print(f"Hello, {name}!")

greet()  # TypeError: missing 1 required positional argument
Fix:


def add_to_list(value, lst=[]):  
    lst.append(value)
    return lst

print(add_to_list(1))  # Output: [1]
print(add_to_list(2))  # Output: [1, 2] (unexpected behavior)
Fix:


def add_to_list(value, lst=None):
    if lst is None:
        lst = []
    lst.append(value)
    return lst

def multiply(a, b):
    return a * b

nums = [2, 3]
print(multiply(nums))  # TypeError
Fix:


print(multiply(*nums))  # Output: 6