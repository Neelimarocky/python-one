# Printing basic strings and numbers
print("hello world")  # Prints the string "hello world"
print(2, 3, 4, 5)     # Prints multiple numbers separated by spaces
print("good morning") # Prints the string "good morning"

# Performing arithmetic operations
print(566 + 799)   # Addition: 566 + 799 = 1365
print(566 - 799)   # Subtraction: 566 - 799 = -233
print(566 * 799)   # Multiplication: 566 * 799 = 452234
print(566 ** 799)  # Exponentiation (Power): 566 raised to the power 799 (very large result)
print(566 / 799)   # Division: Gives decimal result
print(566 // 799)  # Floor Division: Only integer quotient
print(566 % 799)   # Modulo: Gives remainder of division

# Using variables for arithmetic operations
a = 678
b = 756

print(a + b)   # Addition: 678 + 756 = 1434
print(a - b)   # Subtraction: 678 - 756 = -78
print(a * b)   # Multiplication: 678 * 756 = 512568
print(a ** b)  # Exponentiation: Very large result
print(a / b)   # Division: Gives decimal result
print(a // b)  # Floor Division: Only integer quotient
print(a % b)   # Modulo: Gives remainder of division

# String Indexing and Slicing
sentence = "Python is a powerful programming language"

# Indexing (Positive)
print(sentence[0])   # 'P' (First character)
print(sentence[7])   # 'i' (8th character, counting from 0)
print(sentence[10])  # 'a'

# Negative Indexing
print(sentence[-1])   # 'e' (Last character)
print(sentence[-5])   # 'g' (5th character from the end)

# Slicing (Extracting a part of the string)
print(sentence[0:6])   # 'Python' (From index 0 to 5)
print(sentence[7:9])   # 'is' (From index 7 to 8)
print(sentence[10:])   # 'a powerful programming language' (From index 10 to end)
print(sentence[:6])    # 'Python' (From start to index 5)

# Negative Slicing
print(sentence[-9:])   # 'language' (Last 8 characters)
print(sentence[-20:-9]) # 'programming' (Extracts word "programming")
print(sentence[::-1])   # Reverses the entire string

# Step Indexing (Skipping Characters)

# Extracting every second character
print(sentence[::2])  # 'Pto sapwflu rgamn agae' (Skips 1 character each time)

# Extracting every third character
print(sentence[::3])  # 'Ph  rpogrglnu' (Skips 2 characters each time)

# Extracting alternate characters from a slice
print(sentence[0:20:2])  # 'Pto sa owr' (First 20 characters, skipping every other)

# Reversing with step
print(sentence[::-2])  # 'eug agmrpwlpas otyP' (Reversing while skipping 1 character)

# Extracting a word in reverse order
print(sentence[17:9:-1])  # 'lufrewop' (Reverse "powerful")

# More Examples with Step Indexing
word = "Programming"

# Extract every second letter
print(word[::2])  # 'Pormig'

# Extract every third letter
print(word[::3])  # 'Paini'

# Reverse only "Programming"
print(word[::-1])  # 'gnimmargorP'

# Extract last 5 characters in reverse order
print(word[-1:-6:-1])  # 'gnimm'
