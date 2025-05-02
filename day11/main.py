import pyfiglet
import random


def main():
    print(pyfiglet.figlet_format("Black Jack"))

    list_of_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    users_cards = random.sample(list_of_cards, 2)
    dealers_cards = random.sample(list_of_cards, 2)

    print("Your cards: ", users_cards)
    print("Computer's first card: ", dealers_cards[0])


    def calculate_total(cards: list) -> int:
        count = 0
        for card in cards:
            if str(card).isalpha():
                count += 10
            else:
                count += int(card)
        return count


    def check_bust(cards: list):
        total = calculate_total(cards)
        if total >= 21:
            return True
        else:
            return False


    def check_jack(cards: list):
        total = calculate_total(cards)
        if total == 21:
            print("You won.")


    while True:
        choice = input("Type 'y' to get another card or 'n' to pass: ")
        check_jack(users_cards)

        if choice == "y":
            random_card = random.choice(users_cards)
            users_cards.append(random_card)
            print("Added one card: ", users_cards)
            if check_bust(users_cards):
                print("Sorry its a bust. You lost")
                break

if __name__ == "__main__":
    main()
