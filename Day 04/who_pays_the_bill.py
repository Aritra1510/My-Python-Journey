import random

friends = ["Aritra", "Das", "Shantanu", "Sourav", "Mithun"]
payer = friends[random.randint(0, len(friends) - 1)]

print(f"{payer} will pay the bill today!")