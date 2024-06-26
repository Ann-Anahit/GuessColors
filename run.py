import random


# ANSI color escape codes
color_codes = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "purple": "\033[95m",
    "teal": "\033[96m",
    "white": "\033[97m",
    "orange": "\033[38;5;208m",
    "maroon": "\033[38;5;88m",
    "olive": "\033[38;5;58m",
    "brown": "\033[38;5;94m",
    "lime": "\033[38;5;10m",
    "amber": "\033[38;5;214m"
}

# List of colors
colors = list(color_codes.keys())

# Dictionary mapping color combinations to the resulting color
color_combinations = {
    ("red", "blue"): "purple",
    ("blue", "yellow"): "green",
    ("yellow", "red"): "orange",
    ("red", "green"): "brown",
    ("blue", "green"): "teal",
    ("yellow", "green"): "lime",
    ("red", "orange"): "maroon",
    ("yellow", "orange"): "amber",
    ("purple", "green"): "olive",
    ("yellow", "blue"): "green",
    ("green", "blue"): "teal",
    ("green", "yellow"): "lime",
    ("blue", "red"): "purple",
    ("green", "red"): "brown",
    ("orange", "blue"): "maroon",
}


def mix_colors(color1, color2):
    """
    Function to mix two colors and return the resulting color.
    """
    # Sort the colors to handle different orderings
    colors = tuple(sorted([color1, color2]))
    return color_combinations.get(colors)


def display_round_instructions(round_count, color1, color2, user_guess):
    """
    Function to display instructions for the current round.
    """
    print(f"Round {round_count}: You mix {color_codes[color1]}{color1}\033[0m "
          f"and {color_codes[color2]}{color2}\033[0m...")
    print("What color do you think you'll get?")


def display_color_options(options):
    """
    Function to display color options for the user to guess.
    """
    for i, option in enumerate(options, 1):
        if option in color_codes:
            print(f"{i}. {color_codes[option]}{option}\033[0m")


def get_user_guess():
    """
    Function to get the user's guess.
    """
    while True:
        choice = input("Enter your choice (1, 2, or 3): ")
        try:
            choice_index = int(choice) - 1
            if choice_index in (0, 1, 2):
                return choice_index
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid choice! Please enter 1, 2, or 3.")


def play_round(round_count):
    """
    Function to play a single round of the game.
    """
    round_score = 0  # Initialize score for the current round
    correct_answers = 0  # Initialize the count of correct answers

    for _ in range(3):  # Play three rounds
        round_count += 1  # Increment round count
        # Pick two random colors
        color1 = random.choice(colors)
        color2 = random.choice(colors)

        # Ensure a valid color combination is selected
        while mix_colors(color1, color2) is None:
            color1 = random.choice(colors)
            color2 = random.choice(colors)

        # Determine the correct answer and two incorrect answers
        correct_answer = mix_colors(color1, color2)
        incorrect_answers = [color for color in colors
                             if color != correct_answer]
        random.shuffle(incorrect_answers)
        options = [correct_answer] + incorrect_answers[:2]
        random.shuffle(options)

        # Allow the player to guess two times
        for attempt in range(2):
            display_round_instructions(round_count, color1, color2, options)
            display_color_options(options)
            choice_index = get_user_guess()
            user_guess = options[choice_index]

            if user_guess == correct_answer:
                print(f"You guessed it right. {color_codes[user_guess]}"
                      f"{user_guess}\033[0m is the resulting color!")

                round_score += 1  # Increment score for correct guess
                correct_answers += 1  # Increment correct answers count
                break
            else:
                print("Sorry, that's not correct.")
                if attempt == 1:  # If this was the second attempt
                    print("Game Over!")
                    return round_score, correct_answers, True

    return round_score, correct_answers, False  # Indicate game not over


def main():
    print("Welcome to the Color Mixing Game!")
    print("Try to guess the resulting color when you mix two colors.")

    play_again = 'y'
    total_score = 0  # Initialize total score

    while play_again.lower() == 'y':
        round_count = 0  # Start the round count from 0
        correct_answers = 0  # Initialize correct answers count

        while correct_answers < 3:
            round_score, new_correct_answers, game_over = \
             play_round(round_count)
            total_score += round_score  # Increment total score
            correct_answers += new_correct_answers  # Increment correct answers

            print(f"Your score for this round: {round_score}")
            print(f"Your total score: {total_score}")  # Display total score

            # Check if the player has achieved 3 correct answers
            if correct_answers >= 3:
                print("You Win! Congratulations! Your score is 3/3.")
                break

            if game_over:
                break  # Stop the game if it's over

        if game_over:
            break  # Stop asking to play again if the game is over

        play_again = input("Do you want to play again? (y/n): ")
        while play_again.lower() not in ('y', 'n'):
            print("Invalid choice! Please enter 'y' or 'n'.")
            play_again = input("Do you want to play again? (y/n): ")

    print("Thank you for playing! See you soon!")


if __name__ == "__main__":
    main()
