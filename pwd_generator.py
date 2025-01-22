import string
import random
characters=""
#initially prompt to desired length of password
while True:  # Loop till valid number entered
    try:
        length = int(input("Enter the desired length of password: "))
        if length <= 0:  # Check for non-positive numbers
            print("Please enter a positive number.")
            continue
        break  # Exit the loop once valid 
    except ValueError:
        print("You have pressed a character instead press a number")

# to show the password
while True:
    
# Ask if want to include letters, numbers, and special characters
    letters = input("Include letters? (y/n): ").lower() == 'y'
    numbers = input("Include numbers? (y/n): ").lower() == 'y'
    chars = input("Include special characters? (y/n): ").lower() == 'y'
    if letters:
        characters += string.ascii_letters
    if numbers:
        characters += string.digits
    if chars:
        characters += string.punctuation

    if not characters:  # If no character types are selected
        print("You must select at least one character type.")
        exit()

    password = ''.join(random.choice(characters) for _ in range(length))
    print("Generated password:", password)

    another = input("Do you want to generate another password? (y/n): ").lower()
    if another != 'y':  # To check whether the given password includes all prerequisites
        if (letters and any(c.isalpha() for c in password) and
            numbers and any(c.isdigit() for c in password) and
            chars and any(c in string.punctuation for c in password)):
            print("Password rating: 4.5/5")
        else:
            print("Password rating: 3.5/5")
        break



