# 1. Create a list named numbers that contains the integers from 1 to 10
numbers = list(range(1, 11))

# 2. Use list slicing to create a new list named first_half
first_half = numbers[:5]

# 3. Use list slicing to create another list named second_half
second_half = numbers[5:]

# 4. Use a list comprehension to create a new list named squares
squares = [num ** 2 for num in numbers]

# 5. Print all three lists
print("First Half:", first_half)
print("Second Half:", second_half)
print("Squares:", squares)
