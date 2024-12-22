
numbers = []

for i in range(10):
    while True:
        try:
         
            number = int(input(f"შეიყვანეთ {i+1}-ე რიცხვი: "))
            numbers.append(number)
            break
        except ValueError:
            print("გთხოვთ, შეიყვანეთ ვალიდური რიცხვი.")

# მიღებული სიის დაბეჭდვა
print("თქვენი შეყვანილი რიცხვების სია:", numbers)
