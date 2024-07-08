#   LAB 07 Dictionary

# Creating a dictionary
my_dict = {"name": "Akif", "age": 25, "city": "Kayseri"}

# Accessing elements using keys
print(my_dict["name"])  # Output: Akif
print(my_dict["age"])  # Output: 25

# Adding a new key-value pair
my_dict["email"] = "akif@example.com"
print(my_dict)  # Output: {'name': 'Akif', 'age': 25, 'city': 'Kayseri', 'email': 'akif@example.com'}

# Updating an existing value
my_dict["age"] = 26
print(my_dict)  # Output: {'name': 'Akif', 'age': 26, 'city': 'Kayseri', 'email': 'akif@example.com'}

# Deleting a key-value pair
del my_dict["city"]
print(my_dict)  # Output: {'name': 'Akif', 'age': 26', 'email': 'akif@example.com'}

### Explanation:
# - We create a dictionary named `my_dict` containing keys (`name`, `age`, `city`) and their corresponding values.
# - To access elements in a dictionary, we use keys. For example, `my_dict["name"]` retrieves the value associated
# with the key `name`.
# - We add a new key-value pair by assigning a value to a new key.
# - Updating an existing value is done by reassigning a value to an existing key.
# - Deleting a key-value pair is done using the `del` statement.

# -----------------------------------------------------------------------------------------------------------------------

## Dictionary Methods:

### Using dictionary methods

my_dict = {"name": "Akif", "age": 25, "age": 30, "city": "Kayseri"}

# get() method
print(my_dict.get("name"))  # Output: Akif
print(my_dict.get("address", "Not Found"))  # Output: Not Found

# keys(), values(), and items() methods
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])
print(my_dict.values())  # Output: dict_values(['Akif', 30, 'Kayseri'])
print(my_dict.items())  # Output: dict_items([('name', 'Akif'), ('age', 30), ('city', 'Kayseri')])

### Explanation:
# - The `get()` method retrieves the value associated with a key. If the key is not found, it returns a default value
# (if provided).
# - The `keys()` method returns a view object containing the keys of the dictionary.
# - The `values()` method returns a view object containing the values of the dictionary.
# - The `items()` method returns a view object containing the key-value pairs of the dictionary.

# ------------------------------------------------------------------------------------------------------------------

## Advanced Dictionary Operations:

### Dictionary comprehension

squares = {x: x*x for x in range(6)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


### Explanation:
# - Dictionary comprehension allows us to create dictionaries in a concise way. Here, we create a dictionary `squares`
# where keys are numbers from 0 to 5 and values are their squares.

# --------------------------------------------------------------------------------------------------------------------

### Nested dictionaries

nested_dict = {
    "person1": {"name": "Akif", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}

print(nested_dict["person1"]["name"])  # Output: Akif
print(nested_dict["person2"]["age"])  # Output: 30


### Explanation:
# - Nested dictionaries are dictionaries within dictionaries. We can access elements in nested dictionaries using multiple keys.

# -------------------------------------------------------------------------------------------------------------------

### Iterating over dictionaries

my_dict = {"name": "Akif", "age": 25}

# Iterating over keys
for key in my_dict:
    print(key)

# Iterating over values
for value in my_dict.values():
    print(value)

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")


### Explanation:
# - We can iterate over dictionaries using loops.
# - Iterating over keys can be done by looping directly over the dictionary.
# - Iterating over values is done using the `values()` method.
# - Iterating over key-value pairs is done using the `items()` method.

# ---------------------------------------------------------------------------------------------------------------------

### Using defaultdict

from collections import defaultdict

default_dict = defaultdict(int)
default_dict["a"] += 1

print(default_dict)  # Output: defaultdict(<class 'int'>, {'a': 1})


### Explanation:
# - `defaultdict` is a subclass of the built-in `dict` class. It overrides one method and adds one writable instance variable.
# - The first argument of `defaultdict` is a default factory, which provides the default value for nonexistent keys.

# --------------------------------------------------------------------------------------------------------------------

### Using OrderedDict

from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict["a"] = 1
ordered_dict["b"] = 2

print(ordered_dict)  # Output: OrderedDict([('a', 1), ('b', 2)])


### Explanation:
# - `OrderedDict` is a subclass of the built-in `dict` class that maintains the order in which keys are inserted.

# --------------------------------------------------------------------------------------------------------------------- 

### Using Counter

from collections import Counter

count = Counter(["a", "b", "c", "a", "b", "a"])
print(count)  # Output: Counter({'a': 3, 'b': 2, 'c': 1})


### Explanation:
# - `Counter` is a subclass of the built-in `dict` class designed for counting hashable objects.
# - It is part of the `collections` module and is useful for counting elements in an iterable.