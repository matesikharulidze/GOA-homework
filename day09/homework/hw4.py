# მომხმარებლის ასაკის შეყვანა, როგორც სტრიქონი
age_str = input("შეიყვანეთ თქვენი ასაკი: ")
print("შეყვანილი ასაკის ტიპი:", type(age_str))

# ტიპის შეცვლა int-ად
age_int = int(age_str)
print("Integer:", age_int, "| ტიპი:", type(age_int))

# ტიპის შეცვლა float-ად
age_float = float(age_int)
print("Float:", age_float, "| ტიპი:", type(age_float))
