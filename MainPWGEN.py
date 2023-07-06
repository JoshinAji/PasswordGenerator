import string
import random

def generate_password(min_length, numbers=True, special_characters=True):
    letter = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letter
    if numbers:
        characters+=digits
    if special_characters:
        characters+=special

    pwd = ""
    meet_criteria = False
    has_number = False
    has_special = False

    while not meet_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meet_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_characters:
            meet_criteria = meet_criteria and has_special

    return pwd



def Main():
    length = input("Enter the Length of the Password: ")
    num = input("Do you want to have Characters?: (y/n)")
    special = input("Do you want to have Special Characters?: (y/n)")

    if num == "y":
        num == True
    else:
        num = False
    if special == "y":
        special == True
    else:
        special = False

    pwd = generate_password(int(length), num, special)
    print(pwd)

Main()