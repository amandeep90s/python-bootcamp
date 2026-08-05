# Primitive data types - string, boolean, integer, float

# Subscripting
print("HELLO"[1])

# String
print("123" + "345")  # Concatenation

# Integer = Whole number (Without decimal points)
print(370 + 130)

# Large number can also be use like this
print(123_456_789)

# Float numbers = Floating point number
print(10.44)

# Boolean - Capitalize the initial character of True and False boolean type values
print(True)
print(False)

# len method doesn't take integer as an argument
print(len("12345"))

# print method is used for checking the datatype of any variable
print(type("Hello World"))

print(type(13456))

print(type(13456.99))

print(type(True))

# Type conversion - Changing the data type of variable to another data type
print(str(123) + "456")  # Integer to string

print("Number of letters in your name " + str(len(input("Enter your name\n"))))