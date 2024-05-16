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
    if colors in color_combinations:
        return color_combinations[colors]
    else:
        return None  # Return None if the combination is not in the dictionary


def display_round_instructions(round_count, color1, color2):
    """
    Function to display instructions for the current round.
    """
    print(
        "Round {}: You mix {} and {}...".format(
            round_count,
            color_codes[color1] + color1 + "\033[0m",
            color_codes[color2] + color2 + "\033[0m"
        )
    )
    print("What color do you think you'll get?")


def display_color_options(options):
    """
    Function to display color options for the user to guess.
    """
    for i, option in enumerate(options, 1):
        if option in color_codes:
            print("{}. {}".format(i, color_codes[option] + option + "\033[0m"))


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
    incorrect_guesses = 0  # Initialize count of incorrect guesses
    correct_answers = 0  # Initialize the count of correct answers

    for _ in range(3):  # Play three rounds
        # Reset variables for each round
        correct_answers = 0
        incorrect_guesses = 0

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
        incorrect_answers =
        [color for color in colors if color != correct_answer]
        random.shuffle(incorrect_answers)
        options = [correct_answer] + incorrect_answers[:2]
        random.shuffle(options)

        display_round_instructions(round_count, color1, color2)
        display_color_options(options)

        # Allow the player to guess two times
        for _ in range(2):
            choice_index = get_user_guess()
            user_guess = options[choice_index]

            if user_guess == correct_answer:
                print(
                    "You guessed it right. {}{}{} is the resulting color!"
                    .format(
                        color_codes[user_guess], user_guess, "\033[0m"
                    )
                )
                round_score += 1  # Increment score for correct guess
                correct_answers += 1  # Increment correct answers count
                break
            else:
                print("Sorry, that's not correct.")
                incorrect_guesses += 1  # Increment count of incorrect guesses
                if incorrect_guesses == 2:
                    print("Game Over!")
                    print("Your score for this round: {}".format(round_score))
                    return round_score, correct_answers

    return round_score, correct_answers


def main():
    print("Welcome to the Color Mixing Game!")
    print("Try to guess the resulting color when you mix two colors.")

    play_again = 'y'
    total_score = 0  # Initialize total score

    while play_again.lower() == 'y':
        round_count = 0  # Start the round count from 0
        correct_answers = 0  # Initialize correct answers count

        while correct_answers < 3:
            round_count += 1  # Increment round count
            round_score, correct_answers = play_round(round_count)
            total_score += round_score  # Increment total score

            print("Your score for this round: {}".format(round_score))
            print("Your total score: {}".format(total_score))

            # Check if the player has achieved 3 correct answers
            if correct_answers == 3:
                print("You Win! Congratulations! Your score is 3/3.")
                break

        play_again = input("Do you want to play again? (y/n): ")
        while play_again.lower() not in ('y', 'n'):
            print("Invalid choice! Please enter 'y' or 'n'.")
            play_again = input("Do you want to play again? (y/n): ")

    print("Thank you for playing! See you soon!")


if __name__ == "__main__":
    main()
