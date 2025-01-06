# Step 1: Create a list named numbers
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Step 2: Use append() to add the number 100 to the end of the list
numbers.append(100)
print("After appending 100:", numbers)

# Step 3: Use insert() to add the number 5 at the beginning of the list
numbers.insert(0, 5)
print("After inserting 5 at the beginning:", numbers)

# Step 4: Use remove() to remove the number 30 from the list
numbers.remove(30)
print("After removing 30:", numbers)

# Step 5: Use reverse() to reverse the order of the list
numbers.reverse()
print("After reversing the list:", numbers)

# Step 6: Use index() to find the index of the number 50
index_of_50 = numbers.index(50)
print("Index of 50:", index_of_50)

# Step 7: Use count() to count how many times 20 appears in the list
count_of_20 = numbers.count(20)
print("Count of 20:", count_of_20)
