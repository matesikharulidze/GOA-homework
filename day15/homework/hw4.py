# User input
score = int(input("შეიყვანეთ ქულა (1-დან 100-ის ჩათვლით): "))

# Check the grade
if 90 <= score <= 100:
    print("Your grade is A")
elif 80 <= score < 90:
    print("Your grade is B")
elif 70 <= score < 80:
    print("Your grade is C")
else:
    print("Your grade is D")
