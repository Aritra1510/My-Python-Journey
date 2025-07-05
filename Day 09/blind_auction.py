print("Welcome to the secret auction program.")

bid_dict = {}

should_continue = True

while should_continue:
    name = input("What is your name? ")
    bid = int(input("What is your bid?: $"))
    
    bid_dict[name] = bid

    bid_continue = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    if bid_continue == "no":
        should_continue = False
  
    elif bid_continue != "yes":
        print("Invalid input. Please type 'yes' or 'no'. ")
        bid_continue = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
        if bid_continue == "yes":
            should_continue = True
        elif bid_continue == "no":
            should_continue = False
        else:
            print("Invalid input. Exiting the program.")
            should_continue = False
    else:
        print("\n" * 50)
        
# Find the highest bid
# max_bid = max(bid_dict.values())
# highest_bidder = max(bid_dict, key=bid_dict.get)

# print(f"The highest bid was ${max_bid} and the highest bidder was {highest_bidder}.")
highest_bid = 0
highest_bidder = []

for i in bid_dict:
    if bid_dict[i] > highest_bid:
        highest_bid = bid_dict[i]
        highest_bidder = [i]
    elif bid_dict[i] == highest_bid:
        highest_bidder.append(i)
        
if len(highest_bidder) == 1:
    print(f"The highest bid was ${highest_bid} and the highest bidder was {highest_bidder[0]}.")
else:
    print(f"The highest bid was ${highest_bid}. The bidders who tied are: {', '.join(highest_bidder)}.")
