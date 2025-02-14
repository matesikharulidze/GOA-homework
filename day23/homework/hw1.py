def personal_info(name, surname, age, country, city, hobby):
    """
    Prints a descriptive sentence based on the provided personal details.
    """
    sentence = (
        f"My name is {name} {surname}. "
        f"I am {age} years old. I live in {city}, {country}. "
        f"My favorite hobby is {hobby}."
    )
    return sentence

# Call the function with your details
info = personal_info(
    name="Mate",
    surname="Sikharulidze",
    age=13,
    country="Georgia",
    city="Zahesi",
    hobby="coding"
)
print(info)
