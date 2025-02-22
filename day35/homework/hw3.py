s = "hello"
s[0] = 'H'  # TypeError
Fix:


s = "H" + s[1:]  
print(s)  # Output: "Hello"


s = "apple,banana,orange"
words = s.split()  # Default splits on spaces, not commas
print(words)  
Fix:


words = s.split(",")  
print(words)  # Output: ['apple', 'banana', 'orange']


s = "hello world"
s.replace("world", "Python")
print(s)  # Still prints "hello world"
Fix:


s = s.replace("world", "Python")
print(s)  # Output: "hello Python"
