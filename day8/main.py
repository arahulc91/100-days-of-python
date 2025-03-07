import os
import pyfiglet


def encode(message, shift_number):
    try:
        message = str(message)
        shift_number = int(shift_number)
    except ValueError:
        print("Invalid shift number. Please enter a valid integer.")
        return

    encoded_message = ""
    for char in message:
        shift = shift_number % 26
        if char.islower():
            encoded_message += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
        elif char.isupper():
            encoded_message += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
        else:
            encoded_message += char

    print(f"Here's your encoded result: {encoded_message}")


def decode(message: str, shift_number: int):
    try:
        message = str(message)
        shift_number = int(shift_number)
    except ValueError:
        print("Invalid shift number. Please enter a valid integer.")
        return

    decoded_message = ""
    for char in message:
        shift = shift_number % 26
        if char.islower():
            decoded_message += chr((ord(char) - ord("a") - shift) % 26 + ord("a"))
        elif char.isupper():
            decoded_message += chr((ord(char) - ord("A") - shift) % 26 + ord("A"))
        else:
            decoded_message += char

    print(f"Here's your decoded result: {decoded_message}")


while True:
    text = "caesar cipher"
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)
    print("Type 'encode' to encrypt, type 'decode' to decrypt:")
    todo = input().strip()
    print("Type your message:")
    message = input().strip()
    print("Type the shift number:")
    shift_number = input().strip()

    if todo.casefold() == "encode":
        encode(message, shift_number)
    elif todo.casefold() == "decode":
        decode(message, shift_number)
    else:
        print("Incorrect choice. Please type 'encode' or 'decode'.")

    print("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if input().strip().casefold() != "yes":
        break
    os.system("clear" if os.name != "nt" else "cls")
