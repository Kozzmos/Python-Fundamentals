#   LAB 06 Tuples

#  Creating and Accessing Tuples:

# Creating a tuple
my_tuple = (1, 2, 3, "hello", True)

# Accessing elements using indexing
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: "hello"

# Slicing tuple
print(my_tuple[1:4])  # Output: (2, 3, "hello")

# Explanation:
# - We create a tuple named `my_tuple` containing integers, strings, and a boolean value.
# - To access elements in a tuple, we use indexing. Indexing starts from 0, so `my_tuple[0]` refers to the first element.
# - Slicing allows us to extract a subset of elements from the tuple. `my_tuple[1:4]` returns elements from index 1 to index 3.

# -------------------------------------------------------------------------------------------------------------------------
# Tuple Methods:

# Tuple methods
my_tuple = (1, 2, 3, 2, 4, 2)
print(my_tuple.count(2))  # Output: 3 (count occurrences of 2)
print(my_tuple.index(4))  # Output: 4 (index of the first occurrence of 4)


# Explanation:
# - The `count()` method returns the number of occurrences of a specified element in the tuple. In this case, it counts the occurrences of the integer 2.
# - The `index()` method returns the index of the first occurrence of a specified element in the tuple. Here, it returns the index of the integer 4.

# -------------------------------------------------------------------------------------------------------------------------
# Advanced Tuple Operations:

# Nested tuples
nested_tuple = ((1, 2), ("hello", "world"))
print(nested_tuple[1][0])  # Output: "hello"

# Packing and unpacking in functions
def get_coordinates():
    return (3, 5)  # Returning a tuple

x, y = get_coordinates()
print(x, y)  # Output: 3 5

# Sorting tuples
numbers = (5, 2, 8, 1)
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 2, 5, 8]


#Explanation:
# - Nested tuples allow us to create tuples within tuples. `nested_tuple[1][0]` accesses the first element of the second tuple within `nested_tuple`.
# - Tuple unpacking is demonstrated in the `get_coordinates()` function, where the function returns a tuple and it is unpacked into individual variables `x` and `y`.
# - Sorting a tuple using the `sorted()` function returns a new sorted list based on the elements in the tuple. Here, `sorted_numbers` contains the sorted elements of the `numbers` tuple.

