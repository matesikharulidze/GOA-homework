# 1. Create a list named temperatures with daily temperatures
temperatures = [72, 68, 75, 70, 78, 74, 71]

# 2. Calculate and print the highest temperature
highest_temperature = max(temperatures)
print("Highest Temperature:", highest_temperature)

# 3. Calculate and print the lowest temperature
lowest_temperature = min(temperatures)
print("Lowest Temperature:", lowest_temperature)

# 4. Calculate and print the average temperature
average_temperature = sum(temperatures) / len(temperatures)
print("Average Temperature:", average_temperature)

# 5. Use a list comprehension to create a new list of temperatures above 70 degrees
above_70 = [temp for temp in temperatures if temp > 70]

# 6. Print the above_70 list
print("Temperatures Above 70:", above_70)
