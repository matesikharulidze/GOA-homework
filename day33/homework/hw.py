# 1. Task
name = input("Enter your name: ")
age = input("Enter your age: ")
formatted_string = "Hello, {}! You are {} years old.".format(name, age)
print(formatted_string)

# 2. Task
words = ["Python", "is", "fun"]
joined_string = " ".join(words)
print(joined_string)

# 3. Task
sentence = input("Enter a sentence: ")
words_list = sentence.split()
print(words_list)

# 4. Task
sentence = input("Enter a sentence: ")
word_to_replace = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")
modified_sentence = sentence.replace(word_to_replace, new_word)
print(modified_sentence)

# 5. Task
mixed_case_string = input("Enter a mixed-case string: ")
lowercase_string = mixed_case_string.lower()
print(lowercase_string)

# 6. Task
sentence = input("Enter a sentence: ")
uppercase_sentence = sentence.upper()
print(uppercase_sentence)
