nums = [1, 2, 3, 4]
for num in nums:
    if num % 2 == 0:
        nums.remove(num)

print(nums)  # Unexpected output
Fix:


nums = [1, 2, 3, 4]
nums = [num for num in nums if num % 2 != 0]  # Correct way
print(nums)  # Output: [1, 3]

nums = [1, 2, 3]
for num in nums:
    nums.append(num + 1)  # Causes an infinite loop
Fix:

t
nums = [1, 2, 3]
new_nums = [num + 1 for num in nums]
print(new_nums)  # Output: [2, 3, 4]

nums = [1, 2, 3]
nums.extend(4)  # TypeError
Fix:


nums.extend([4])  # Must be an iterable
print(nums)  # Output: [1, 2, 3, 4]


