def main():
    # Day2: Tip Calculator
    print("Welcome to the tip calculator")
    total = float(input("What was the total bill? $"))
    tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
    people = int(input("How many people to split the bill? "))
    cost = (total * (tip + 100) / 100) / people
    print(f"Each person should pay: ${cost:.2f}")

if __name__ == "__main__":
    main()
