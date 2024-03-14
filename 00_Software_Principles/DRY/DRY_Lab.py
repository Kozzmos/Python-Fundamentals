# Duplicative Code

def calculate_area_of_rectangle(length, width):
    return length * width

def calculate_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

length = 5
width = 10

area = calculate_area_of_rectangle(length, width)
perimeter = calculate_perimeter_of_rectangle(length, width)

print("Area:", area)
print("Perimeter:", perimeter)

# Applying DRY Principle

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# Creating a Rectangle instance
rectangle = Rectangle(5, 10)

area = rectangle.calculate_area()
perimeter = rectangle.calculate_perimeter()

print("Area:", area)
print("Perimeter:", perimeter)

# Explanation:

# In the first example, the functions calculate_area_of_rectangle and calculate_perimeter_of_rectangle calculate the area and perimeter of a rectangle, respectively. However, the same parameters (length and width) are duplicated in both functions.

# In the second example, the DRY principle is applied by creating a Rectangle class. This class encapsulates the properties and behaviors of a rectangle. The methods calculate_area and calculate_perimeter are defined within the class, utilizing the self.length and self.width attributes. This way, there's no need to pass length and width as parameters repeatedly.

# By applying the DRY principle, the second example eliminates code duplication, improves maintainability, and enhances readability. Additionally, if there's a need to change how the area or perimeter is calculated, it can be done in a single place within the Rectangle class.