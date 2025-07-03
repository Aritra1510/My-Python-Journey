import random
import string

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

# creating an empty list to store all characters
password = []

# adding random letters
for i in range(0, nr_letters):
    random_letter = random.choice(string.ascii_letters)
    password.append(random_letter)

# adding random symbols
for i in range(0, nr_symbols):
    random_symbol = random.choice(symbols)
    password.append(random_symbol)

# adding random numbers
for i in range(0, nr_numbers):
    random_number = str(random.randint(0, 9))
    password.append(random_number)

# easy password version (in original order)
print(f"Your password is: {''.join(password)}")

# hard password version (shuffled)
random.shuffle(password)
shuffled_password = ''.join(password)
print(f"Your password is: {shuffled_password}")