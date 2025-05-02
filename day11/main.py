import pyfiglet
import random


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
        return True
    else:
        return False


def main():
    print(pyfiglet.figlet_format("Black Jack"))

    list_of_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    users_cards = random.sample(list_of_cards, 2)
    dealers_cards = random.sample(list_of_cards, 2)

    if check_jack(users_cards):
        print("Blackjack! You Won")
        return

    print(f"Your cards: {users_cards}. Total = {calculate_total(users_cards)}")
    print("Computer's first card: ", dealers_cards[0])

    while True:
        choice = input("Type 'y' to get another card or 'n' to pass: ")

        if choice == "y":
            random_card = random.choice(list_of_cards)  # Get card from deck
            users_cards.append(random_card)
            print(
                f"Added one card: {users_cards}. Total = {calculate_total(users_cards)}"
            )
            if check_bust(users_cards):
                print("Sorry its a bust. You lost")
                break
        else:
            # Dealer's turn to draw cards
            while calculate_total(dealers_cards) < 17:
                random_card = random.choice(list_of_cards)
                dealers_cards.append(random_card)
                print(
                    f"Dealer draws a card: {dealers_cards}. Total = {calculate_total(dealers_cards)}"
                )
                if check_bust(dealers_cards):
                    print("Dealer busts! You win!")
                    break

            if calculate_total(dealers_cards) > 21:
                break  # Dealer already busted so game is over

            if calculate_total(dealers_cards) > calculate_total(users_cards):
                print("Sorry the dealer won")
            elif calculate_total(dealers_cards) == calculate_total(users_cards):
                print("Its a draw")
            else:
                print("Congrats you won")
            break

    print(
        f"Score was You: {calculate_total(users_cards)} -- Dealer: {calculate_total(dealers_cards)}"
    )


if __name__ == "__main__":
    main()
