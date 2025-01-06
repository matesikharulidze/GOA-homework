def love_letter(name, message):
    """
    Creates a love letter for the user.
    """
    letter = f"{message}\n\nსიყვარულით, {name}"
    return letter

# ფუნქციის გამოძახება
recipient_name = "მარიამი"
personal_message = "მარიამ, შენ ხარ ჩემი ცხოვრების ნათელი სხივი. შენი ღიმილი ყოველთვის მიბედნიერებს. მეყვარები სამუდამოდ."
love_note = love_letter(recipient_name, personal_message)
print(love_note)
