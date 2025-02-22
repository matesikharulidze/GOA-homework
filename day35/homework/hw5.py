


def square(n):
    result = n * n

print(square(5))  # Output: None
Fix:

def square(n):
    return n * n
print(square(5))  # Output: 25

def divide(a, b):
    return a // b, a % b

result = divide(10, 3)
print(result)  # Output: (3, 1) (Tuple instead of separate values)
Fix:

quotient, remainder = divide(10, 3)
print(quotient, remainder)  # Output: 3 1

def find_even(nums):
    for num in nums:
        if num % 2 == 0:
            return num  # Stops at the first even number

print(find_even([1, 3, 5, 8, 10]))  # Output: 8 (but function stops here)
Fix:


def find_even(nums):
    return [num for num in nums if num % 2 == 0]

print(find_even([1, 3, 5, 8, 10]))  # Output: [8, 10]