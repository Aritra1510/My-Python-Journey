# subscripting
print("Hello"[0:4])  # Output: Hell
print("Hello"[0])  # Output: H
print("Hello"[-1])  # Output: o

# integer
print(123 + 456)  # Output: 579

# large integer
print(12345_6789_1234_567890)

# float
print(3.14159)  # Output: 3.14159

# large float
print(3.14159_26535_89793_23846)

# boolean
print(True)  # Output: True
print(False)  # Output: False


# type
print(type("Hello"))  # Output: <class 'str'>
print(type(123))  # Output: <class 'int'>
print(type(3.14))  # Output: <class 'float'>
print(type(True))  # Output: <class 'bool'>

# type conversion
print(int("123"))  # Output: 123
print(int("123") + int("456")) # Output: 579

# number = len(input('enter your name: '))
# print("Number of letters in your name: " + str(number))

# mathematical operations 
print(3 + 5)  # Addition
print(10 - 2)  # Subtraction
print(4 * 7)  # Multiplication
print(8 / 2)  # Division (gives float result)
print(8 // 2) # Floor Division (gives integer result)
print(2 ** 3)  # Exponentiation (2 raised to the power of 3)

# rounding numbers
print(round(3.14159))  # Output: 3 (rounds to nearest integer)
print(round(3.14159, 2))  # Output: 3.14 (rounds to 2 decimal places)

# absolute value
print(abs(-5))  # Output: 5 (absolute value)