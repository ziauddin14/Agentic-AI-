# Variables store values. Python determines each variable's type automatically.
name = "Alex"                 # str: text
age = 18                      # int: whole number
height = 1.72                 # float: decimal number
is_learning = True            # bool: True or False
favorite_color = None         # NoneType: no value yet

print("Hello,", name)
print("Age:", age)
print("Height:", height)
print("Learning Python:", is_learning)
print("Favorite color:", favorite_color)
print("Type of age:", type(age))

# Arithmetic operators
a = 10
b = 3
print("\nArithmetic operators")
print("Addition:", a + b)          # 13
print("Subtraction:", a - b)       # 7
print("Multiplication:", a * b)     # 30
print("Division:", a / b)           # 3.333...
print("Floor division:", a // b)    # 3
print("Remainder:", a % b)          # 1
print("Power:", a ** b)             # 1000

# Comparison operators return True or False.
print("\nComparison operators")
print("Equal:", a == b)
print("Not equal:", a != b)
print("Greater than:", a > b)
print("Less than:", a < b)
print("Greater than or equal:", a >= b)
print("Less than or equal:", a <= b)

# Logical operators combine or reverse conditions.
print("\nLogical operators")
print("and:", age >= 13 and age < 20)
print("or:", age < 13 or age >= 18)
print("not:", not is_learning)

# Assignment operators update a variable.
print("\nAssignment operators")
score = 10
score += 2
print("After += 2:", score)
score -= 1
print("After -= 1:", score)
score *= 3
print("After *= 3:", score)
score /= 3
print("After /= 3:", score)

# Membership operators check for a value in a collection.
colors = ["red", "green", "blue"]
print("\nMembership operators")
print("green in colors:", "green" in colors)
print("purple not in colors:", "purple" not in colors)

# Identity operators check whether names refer to the same object.
first_list = [1, 2]
second_list = first_list
third_list = [1, 2]
print("\nIdentity operators")
print("first_list is second_list:", first_list is second_list)
print("first_list is third_list:", first_list is third_list)
print("first_list is not third_list:", first_list is not third_list)

# Parentheses can make the order of calculations clear.
result = (a + b) * 2
print("\nParentheses example:", result)
