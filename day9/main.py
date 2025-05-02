import os
import pyfiglet

def main():
    bids = []

    while True:
        print(pyfiglet.figlet_format("Silence Bidder"))
        name = input("What is your name?: ")
        bid = float(input("What is your bid?: $"))
        bids.append({"name": name, "bid": bid})
        resp = input("Are there any other bidders? Type 'yes' or 'no': ")
        if resp.casefold() == "yes":
            os.system("clear")
        else:
            highest = max(bids, key=lambda x: x["bid"])
            print(f"The winner is {highest["name"]} with a bid of ${highest["bid"]:.2f}")
            break

if __name__ == "__main__":
    main()
