import random

from hangman_words import word_list
from hangman_art import hangman_stages

guess = ""
life = 6

word = random.choice(word_list)
word_length = len(word)

placeholder = []

for i in word: 
    placeholder.append("_")

# print(word)
print("Welcome to Hangman!\nGuess the word:")
print(''.join(placeholder))

def ask_the_user():
    global guess
    guess = input("Guess an aplhabet of the word: ").lower()

def logic():
    global placeholder, guess, life
    # ask_the_user()
    if guess in word:
        for i in range(word_length):
         if word[i] == guess:
            placeholder[i] = guess
        print(f"Good guess! '{guess}' is in the word.")
    else:
        life -= 1
        print(hangman_stages[life])
        print(f"Wrong guess! You have lost a life.")


while life != 0 and ''.join(placeholder) != word:
    ask_the_user()
    logic()
    print(' '.join(placeholder))

if ''.join(placeholder) == word:
    print("🎉 You guessed the word!")
else:
    print(f"💀 Game over. The word was: {word}")

print("Thanks for playing Hangman!")