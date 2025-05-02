import random
import string

def main():
    letters = list(string.ascii_letters)
    symbols = list("!@#$%^&*()")
    numbers = list(string.digits)

    print("Welcome to PyPassword Generator!")
    print("How many letters would you like in your password?")
    num_letters = int(input())
    print("How many symbols would you like?")
    num_symbols = int(input())
    print("How many numbers would you like?")
    num_numbers = int(input())

    password = []

    for _ in range(num_letters):
        password.append(random.choice(letters))

    for _ in range(num_symbols):
        password.append(random.choice(symbols))

    for _ in range(num_numbers):
        password.append(random.choice(numbers))

    random.shuffle(password)
    print("Your password is: " + "".join(password))

if __name__ == "__main__":
    main()
