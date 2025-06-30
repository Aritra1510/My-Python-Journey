# This program checks if a user can ride a rollercoaster based on their height.
print("Welcome to the rollercoaster!")

# Ask the user for their height
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age>18:
        print("Your ticket price is $15.")
    else:
        print("Your ticket price is $10.")
else:
    print("Sorry, you are too short to ride the rollercoaster.")