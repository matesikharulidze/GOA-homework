# User input
year = int(input("შეიყვანეთ წელი: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} წელი ნაკიანია.")
else:
    print(f"{year} წელი არ არის ნაკიანი.")
