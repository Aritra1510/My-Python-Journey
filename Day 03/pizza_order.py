print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L? ")
pepperoni = input("Do you want pepperoni? Y or N? ")
extra_cheese = input("Do you want extra cheese? Y or N? ")

price = 0

# Base price by size
if size == "S":
    price += 15
elif size == "M":
    price += 20
elif size == "L":
    price += 25
else:
    print("Invalid size selected.")

# Pepperoni price
if pepperoni == "Y" and size == "S":
    price += 2
elif pepperoni == "Y" and (size == "M" or size == "L"):
    price += 3

# Extra cheese price
if extra_cheese == "Y":
    price += 1

# Final bill
print(f"Your final bill is: ${price}.")
