
numbers = []


for i in range(10):
    while True:
        try:
            
            number = int(input(f"შეიყვანეთ {i+1}-ე რიცხვი: "))
            numbers.append(number)
            break
        except ValueError:
            print("გთხოვთ, შეიყვანეთ ვალიდური რიცხვი.")


print("თქვენი შეყვანილი რიცხვების სია:", numbers)


max_number = numbers[0]  
for number in numbers:
    if number > max_number:
        max_number = number

print("სიაში უდიდესი რიცხვი არის:", max_number)
