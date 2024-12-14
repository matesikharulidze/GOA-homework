# Initialize variables
start = 1
end = 100
sum_even = 0
count_even = 0

# Use a while loop to iterate through numbers
current = start
while current <= end:
    if current % 2 == 0:  # Check if the number is even
        sum_even += current  # Add to sum
        count_even += 1  # Increment the count of even numbers
    current += 1

# Calculate the arithmetic mean
if count_even > 0:
    arithmetic_mean = sum_even / count_even
else:
    arithmetic_mean = 0

print("საშუალო არითმეტიკული:", arithmetic_mean)
