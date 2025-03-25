from curses.ascii import isalpha
import pyfiglet
import random


print(pyfiglet.figlet_format("Black Jack"))

list_of_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

users_cards = random.sample(list_of_cards, 2)
dealers_cards = random.sample(list_of_cards, 2)

print("Your cards: ", users_cards)
print("Computer's first card: ", dealers_cards[0])

choice = input("Type 'y' to get another card or 'n' to pass: ")

if choice == "y":
    random_card = random.choice(users_cards)
    users_cards.append(random_card)
    print("Added one card: ", users_cards)


def check_bust(cards: list):
    pass

def check_jack(cards: list):
    total = calculate_total(cards)
    if total == 21:
        print("You won.")

def calculate_total(cards: list) -> int:
    count = 0
    for card in cards:
        if str(card).isalpha():
            count += 10
        else:
            count += card
    return count