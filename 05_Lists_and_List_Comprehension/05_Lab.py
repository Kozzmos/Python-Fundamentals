#  LAB 05 Lists and List Comprehension

# Creating a list
fruits = ["apple", "banana", "cherry", "orange"]

# Accessing elements using indexing
print(fruits[0])  # Output: "apple"

# Modifying elements
fruits[1] = "grapes"  # Change "banana" to "grapes"
print(fruits)  # Output: ["apple", "grapes", "cherry", "orange"]

# Adding elements using append()
fruits.append("kiwi")  # Append "kiwi" to the end of the list
print(fruits)  # Output: ["apple", "grapes", "cherry", "orange", "kiwi"]

# Removing elements using remove()
fruits.remove("cherry")  # Remove "cherry" from the list
print(fruits)  # Output: ["apple", "grapes", "orange", "kiwi"]

------------------------------------------------------------------------------------------------

# List comprehension to create a list of squares
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

# List comprehension with conditional filtering
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)  # Output: [4, 16, 36, 64, 100]

# Nested list comprehension
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)  # Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# Using list comprehension to modify elements
fruits = [fruit.upper() for fruit in fruits]  # Convert all elements to uppercase
print(fruits)  # Output: ["APPLE", "GRAPES", "BANANA", "ORANGE", "KIWI"]

------------------------------------------------------------------------------------------------

# Some string operations which you can use with lists:

# Using string methods
sentence = "  hello world  "

# strip whitespace from both ends
sentence_stripped = sentence.strip()
print(sentence_stripped)  # Output: "hello world"

# split the sentence into words
words = sentence_stripped.split()
print(words)  # Output: ['hello', 'world']

# check if the sentence starts with a specific word
starts_with_hello = sentence_stripped.startswith("hello")
print(starts_with_hello)  # Output: True

# replace a word in the sentence
new_sentence = sentence_stripped.replace("world", "Python")
print(new_sentence)  # Output: "hello Python"

# Explanation:

# 1. Creating and Modifying Lists:
#- We start by creating a list `fruits` containing some fruit names.
#- We access elements using indexing (e.g., `fruits[0]` to get the first element).
#- We modify elements by assigning new values to specific indices (`fruits[1] = "grapes"`).
#- We add elements using the `append()` method (`fruits.append("kiwi")` adds "kiwi" to the end).
#- We remove elements using the `remove()` method (`fruits.remove("cherry")` removes "cherry" from the list).
#
# 2. List Comprehension:
#- We use list comprehension to create a list of squares (`squares`).
#- We use conditional filtering within list comprehension to create a list of squares of even numbers (`even_squares`).
#- We demonstrate nested list comprehension to create a matrix (`matrix`) with rows and columns of multiplication results.
#
# List comprehension offers a concise and expressive way to create lists and perform transformations on existing lists, making Python code more readable and efficient.

#  3. String Methods

# strip: The strip() method removes leading and trailing whitespace from a string.
# split: The split() method splits a string into a list of substrings based on whitespace by default.
# startswith: The startswith() method checks if a string starts with a specified prefix.
# replace: The replace() method replaces occurrences of a specified substring with another string.
# By combining lists with list methods and string operations, we can perform various data manipulations and transformations efficiently in Python.