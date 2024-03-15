# WET code examples:

# Redundant code blocks without using functions or abstractions

# Calculate area of a rectangle
length1 = 5
width1 = 10
area1 = length1 * width1
print("Area 1:", area1)

# Calculate area of another rectangle
length2 = 8
width2 = 12
area2 = length2 * width2
print("Area 2:", area2)

# Calculate area of yet another rectangle
length3 = 3
width3 = 7
area3 = length3 * width3
print("Area 3:", area3)

# ---------------------------------------------------------------------------------------------------

# Copy-pasted code segments performing similar tasks

# Task 1: Calculate area
length = 5
width = 10
area = length * width
print("Area:", area)

# Task 2: Calculate perimeter
length = 5
width = 10
perimeter = 2 * (length + width)
print("Perimeter:", perimeter)

# Task 3: Display rectangle details
length = 5
width = 10
print(f"Length: {length}, Width: {width}, Area: {length * width}, Perimeter: {2 * (length + width)}")

# ------------------------------------------------------------------------------------------------------

# Hardcoding values without using variables or constants

# Task 1: Calculate total price with tax
price1 = 100
tax_rate = 0.1
total_price1 = price1 * (1 + tax_rate)
print("Total Price 1:", total_price1)

# Task 2: Calculate total price with different tax rate
price2 = 150
total_price2 = price2 * 1.12  # Hardcoded tax rate instead of using tax_rate variable
print("Total Price 2:", total_price2)

# Task 3: Display product details with hardcoded values
print("Product 1: Price: 100, Tax Rate: 10%, Total Price: 110")
print("Product 2: Price: 150, Tax Rate: 12%, Total Price: 168")

# Explanation:

# In these examples, you can see instances of WET code where similar tasks are performed multiple times without leveraging functions, abstractions, or variables/constants to reduce redundancy.

# Refactoring such code to adhere to the DRY (Don't Repeat Yourself) principle would involve creating reusable functions, using variables/constants, and centralizing shared logic to improve readability, maintainability, and scalability.