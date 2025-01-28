# მომხმარებლისგან რიცხვების შეყვანა
user_input = input("შეიყვანეთ რიცხვები მძიმით გამოყოფილად: ")

# რიცხვების სიის შექმნა
numbers = [int(num.strip()) for num in user_input.split(",")]

# რიცხვების ჯამის გამოთვლა
sum_numbers = sum(numbers)

# შედეგის დაბეჭდვა
print(f"რიცხვების ჯამი: {sum_numbers}")