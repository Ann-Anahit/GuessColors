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
    "orange": "\033[38;5;208m",  # Orange color
    "maroon": "\033[38;5;88m",   # Maroon color
    "olive": "\033[38;5;58m",    # Olive color
    "navy": "\033[38;5;21m",     # Navy color
    "forest green": "\033[38;5;28m",  # Forest Green color
    "burnt umber": "\033[38;5;88m",   # Burnt Umber color
    "burnt sienna": "\033[38;5;130m", # Burnt Sienna color
    "goldenrod": "\033[38;5;136m",    # Goldenrod color
    "amber": "\033[38;5;202m"         # Amber color
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
    ("blue", "orange"): "burnt sienna",
    ("yellow", "orange"): "amber",
    ("purple", "green"): "olive",
    ("purple", "orange"): "bronze",
    ("purple", "yellow"): "goldenrod",
    ("blue", "indigo"): "navy",
    ("green", "indigo"): "forest green",
    ("orange", "indigo"): "burnt umber"
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

def main():
    print("Welcome to the Color Mixing Game!")
    print("Try to guess the resulting color when you mix two colors.")

    play_again = 'y'
    while play_again.lower() == 'y':
        # Pick two random colors
        color1 = random.choice(colors)
        color2 = random.choice(colors)

        # Determine the correct answer and two incorrect answers
        correct_answer = mix_colors(color1, color2)
        incorrect_answers = [color for color in colors if color != correct_answer]
        random.shuffle(incorrect_answers)
        options = [correct_answer] + incorrect_answers[:2]
        random.shuffle(options)

        print("You mix {} and {}...".format(color_codes[color1] + color1 + "\033[0m", color_codes[color2] + color2 + "\033[0m"))
        print("What color do you think you'll get?")
        for i, option in enumerate(options, 1):
            print("{}. {}".format(i, color_codes[option] + option + "\033[0m"))

        # Ask for user's choice
        choice = input("Enter your choice (1, 2, or 3): ")
        try:
            choice_index = int(choice) - 1
            user_guess = options[choice_index]
        except (ValueError, IndexError):
            print("Invalid choice! Please enter 1, 2, or 3.")
            continue

        if user_guess == correct_answer:
            print("Congratulations! You guessed it right. {} is the resulting color!".format(color_codes[correct_answer] + correct_answer + "\033[0m"))
        else:
            print("Sorry, that's not correct. The resulting color is {}.".format(color_codes[correct_answer] + correct_answer + "\033[0m"))

        play_again = input("Do you want to play again? (y/n): ")

    print("Thank you for playing! See you soon!")

if __name__ == "__main__":
    main()