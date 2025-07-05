alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            ]

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for i in original_text:
        shifed_position = (alphabet.index(i) + shift_amount) % 26
        cipher_text += alphabet[shifed_position]
    print(f"Here is the encoded result: {cipher_text}")

def decrypt(original_text, shift_amount):
    cipher_text = ""
    for i in original_text:
        shifted_position = (alphabet.index(i) - shift_amount) % 26
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")

def caesar(original_text, shift_amount, encode_or_decode):
    cipher_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for i in original_text:
        if i not in alphabet:
            cipher_text += i
        else:
            shifted_position = (alphabet.index(i) + shift_amount) % 26
            cipher_text += alphabet[shifted_position]
    if encode_or_decode != "encode" and encode_or_decode != "decode":
        print("You chose wrong option. Please type 'encode' or 'decode'.")
    else:
        print(f"Here is the {encode_or_decode}d result: {cipher_text}")

should_continue = True

while should_continue:
    print("Welcome to the Caesar Cipher!")

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(text, shift, direction)
    
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    if result == "no":
        should_continue = False
        print("Goodbye!")
    elif result != "yes":
        print("You typed wrong option. Please type 'yes' or 'no'.")
        