# მომხმარებლის მიერ ტექსტის შეყვანა
text = input("შეიყვანეთ ტექსტი: ")

# 1. ტექსტის მცირე ასოებად გადაქცევა
lower_text = text.lower()
print("მცირე ასოები: ", lower_text)

# 2. ტექსტის დიდი ასოებად გადაქცევა
upper_text = text.upper()
print("დიდი ასოები: ", upper_text)

# 3. მხოლოდ პირველი ასოს გადაქცევა დიდ ასოდ
capitalized_text = text.capitalize()
print("პირველი დიდი ასო: ", capitalized_text)

# 4. მომხმარებლის მიერ შერჩეული სიტყვის პოვნა ტექსტში
search_word = input("შეიყვანეთ საძიებო სიტყვა: ")
index = text.find(search_word)

if index != -1:
    print(f"სიტყვა '{search_word}' მოიძებნა ინდექსზე: {index}")
else:
    print(f"სიტყვა '{search_word}' ვერ მოიძებნა ტექსტში.")
