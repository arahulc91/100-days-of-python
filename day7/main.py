import pyfiglet
import requests


print(pyfiglet.figlet_format("hangman"))
query = "marvel superheros"
print("Hint: ", query)


def generate_random_word():
    try:
        response = requests.get(f"https://api.talanoa-ai.com/?query={query}&words=1")
        response.raise_for_status()
        return list(response.json()[0])
    except requests.RequestException as e:
        print(f"Error fetching word: {e}")
        return None


def display_hangman(stage):
    hangman_stages = [
        """
         ------
         |    |
         |
         |
         |
         |
        ---
        """,
        """
         ------
         |    |
         |    O
         |
         |
         |
        ---
        """,
        """
         ------
         |    |
         |    O
         |    |
         |
         |
        ---
        """,
        """
         ------
         |    |
         |    O
         |   /|
         |
         |
        ---
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |
         |
        ---
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   /
         |
        ---
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   / \\
         |
        ---
        """,
    ]
    print(hangman_stages[stage])


def display_score(index):
    print(
        f"***************************** {index}/6 LIVES LEFT *****************************"
    )


def play_game():
    random_word = generate_random_word()
    if not random_word:
        print("Failed to start the game due to an error fetching the word.")
        return

    dashed_word = ["_" for _ in random_word]
    print("Word to guess: " + " ".join(dashed_word))

    is_game_over = False
    error_counter = 6

    # Display initial hangman stage
    display_hangman(0)

    while not is_game_over:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            correct_guess = False
            for index, letter in enumerate(random_word):
                if guess == letter:
                    correct_guess = True
                    dashed_word[index] = letter
            if not correct_guess:
                print(f"You guessed {guess}, thats not in the word. You lose a life.")
                error_counter -= 1
                display_hangman(6 - error_counter)
                display_score(error_counter)
                if error_counter == 0:
                    print("Sorry you lose. The word was: " + "".join(random_word))
                    is_game_over = True
            else:
                print(" ".join(dashed_word))
                if dashed_word == random_word:
                    print("You win")
                    is_game_over = True
        else:
            print("Invalid input. Please guess a single letter.")
            error_counter -= 1
            display_hangman(6 - error_counter)
            if error_counter == 0:
                print("Sorry you lose. The word was: " + "".join(random_word))
                is_game_over = True


play_game()
