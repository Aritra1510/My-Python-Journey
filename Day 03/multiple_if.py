# This program checks if a user can ride a rollercoaster based on their height.
print("Welcome to the rollercoaster!")

# Ask the user for their height
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age>18:
        bill = 15
        print("Your ticket price is $15.")
    elif age>=12:
        bill = 12
        print("Your ticket price is $12.")
    else:
        bill = 10
        print("Your ticket price is $10.")
    
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if(wants_photo == "Y"):
        print(f"Your final bill is ${bill + 3}.")
    else:
        print(f"Your final bill is ${bill}.")
else:
    print("Sorry, you are too short to ride the rollercoaster.")