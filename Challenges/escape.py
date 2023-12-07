import random

class QuitRequest(Exception):
    pass    
    

def get_input(prompt):
    """Takes input from the user, based on a prompt."""
    # This function is used every single time the program gets input from the user!
    input_value = input(prompt)
    
    if input_value == "\quit":
        raise QuitRequest
    
    return input_value

def get_a_number(prompt):
    """Repeatedly requests input from the user until they supply something that can be converted to an integer."""
    # This function uses get_input when it asks the user for their input!
    result = None
    while result is None:
        user_input = get_input(prompt)
        # Note that we catch a ValueError here if the input is not numerical.
        try:
            result = int(user_input)
        except ValueError:
            print("That wasn't a number, please try again.")
    return result

def guess_the_number(the_number):
    """Runs a single game of guess the number - repeatedly asking for guesses until the user gives the correct answer."""
    # This function uses get_a_number every time it asks the user for a guess!
    user_guess = get_a_number("Guess the number I'm thinking of!: ")
    
    while user_guess != the_number:
        user_guess = get_a_number("That wasn't quite right, try again!: ")
    else:
        print(f"That's correct it was {the_number}!\n\n")

def prompt_play(text_insert):
    """Invites the user to play the game."""
    # We don't convert the input to a number here, but we still use get_input!
    choice = get_input(f"""Let's play {text_insert} game! I'll think of a number between 0 and 10, and you have to guess it. You can quit any time by typing '\quit'.
Press Enter to begin: """)

def main_loop():
    """The main loop of the game - invites the user to play again over and over until they quit."""
    # We are using the text_insert variable to make sure our grammar is correct.
    # On the first loop we invite the user to play *a* game.
    text_insert = "a"
    try:
        while True:
            prompt_play(text_insert)
            # After the first loop we invite them to play *another* game.
            text_insert="another"
            guess_the_number(random.randint(0, 10))
    except QuitRequest:
        print("Ok, see you next time!")