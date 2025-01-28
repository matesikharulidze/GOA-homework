# მომხმარებლისგან პირველი რიცხვის შეყვანა
first_number = int(input("შეიყვანეთ ერთი რიცხვი: "))

# რიცხვების სიის შექმნა
numbers = []

# სხვა რიცხვების შეყვანა (უსაზღვროდ)
while True:
    user_input = input("შეიყვანეთ რიცხვი (გასასვლელად დააწკაპუნეთ Enter-ს): ")
    if user_input == "":
        break
    numbers.append(int(user_input))

# შეყვანილი რიცხვების რაოდენობის დაბეჭდვა
print(f"შეყვანილი რიცხვების რაოდენობა: {len(numbers)}")
