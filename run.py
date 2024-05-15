import random

# Color codes for terminal output
color_codes = {
    "red": "\033[91m",        # Red color
    "blue": "\033[94m",       # Blue color
    "green": "\033[92m",      # Green color
    "yellow": "\033[93m",     # Yellow color
    "purple": "\033[95m",     # Purple color
    "orange": "\033[33m",     # Orange color
    "teal": "\033[96m",       # Teal color
    "olive": "\033[32m",      # Olive color
    "maroon": "\033[31m",     # Maroon color
}

# List of available colors
colors = list(color_codes.keys())

# Additional color combinations
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
}

def mix_colors(color1, color2):
    """
    Function to mix two colors and return the resulting color.
    """
    if (color1, color2) in color_combinations:
        return color_combinations[(color1, color2)]
    elif (color2, color1) in color_combinations:
        return color_combinations[(color2, color1)]
    else:
        return None  # No valid resulting color for the given combination


def display_round_instructions(round_count, color1, color2):
    """
    Function to display instructions for each round.
    """
    print(f"Round {round_count}: You mix {color1} and {color2}...")

def display_color_options(options):
    """
    Function to display color options for the user to choose from.
    """
    print("What color do you think you'll get?")
    for i, option in enumerate(options, 1):
        if option in color_codes:
            print("{}. {}".format(i, color_codes[option] + option + "\033[0m"))

def get_user_guess():
    """
    Function to get the user's guess.
    """
    while True:
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice.isdigit():
            choice_index = int(choice) - 1
            if 0 <= choice_index <= 2:
                return choice_index
        print("Invalid choice! Please enter 1, 2, or 3.")

def play_round(round_count):
    """
    Function to play a single round of the game.
    """
    round_score = 0  # Initialize score for the current round
    incorrect_guesses = 0  # Initialize count of incorrect guesses
    correct_answers = 0  # Initialize the count of correct answers for the round
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
        incorrect_answers = [color for color in colors if color != correct_answer]
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
                print("Congratulations! You guessed it right. {} is the resulting color!".format(color_codes[correct_answer] + correct_answer + "\033[0m"))
                round_score += 1  # Increment score for correct guess
                correct_answers += 1  # Increment correct answers count
                break
            else:
                print("Sorry, that's not correct.")
                incorrect_guesses += 1  # Increment count of incorrect guesses
                if incorrect_guesses == 2:
                    print("Game Over!")
                    return round_score, correct_answers

    return round_score, correct_answers

def main():
    """
    Main function to run the Color Mixing Game.
    """
    print("Welcome to the Color Mixing Game!")
    print("Try to guess the resulting color when you mix two colors.")

    play_again = 'y'
    total_score = 0  # Initialize total score
    round_count = 0  # Initialize round count
    while play_again.lower() == 'y':
        round_score, correct_answers = play_round(round_count)
        total_score += round_score  # Update total score
        round_count += 3  # Increment round count by 3

        print("Your score for this round: {}".format(round_score))  # Display round score
        print("Your total score: {}".format(total_score))  # Display total score

        # Check if the player has achieved 3 correct answers
        if correct_answers == 3:
            print("You Win! Congratulations! Your score is 3/3.")

        # Ask to play again after every third round
        if round_count % 3 == 0:
            while True:
                play_again = input("Do you want to play again? (y/n): ")
                if play_again.lower() in ('y', 'n'):
                    break
                else:
                    print("Invalid choice! Please enter 'y' or 'n'.")

    print("Thank you for playing! See you soon!")

if __name__ == "__main__":
    main()