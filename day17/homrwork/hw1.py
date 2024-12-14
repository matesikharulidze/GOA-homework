# Step 1: Ask the user to input numbers separated by commas
input_numbers = input("შეიყვანეთ რიცხვები, გამოყავით მძიმით (მაგ.: 1, 2, 3, 4): ")

# Step 2: Convert the input string into a list of numbers
numbers = [int(num.strip()) for num in input_numbers.split(",")]

# Step 3: Calculate the sum of the numbers
total_sum = sum(numbers)

# Step 4: Print the result
print("რიცხვების ჯამი არის:", total_sum)
