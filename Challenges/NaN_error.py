def get_a_number(prompt):
    """Repeatedly asks the user for a number until they give an input that can be converted to an integer. Returns an int."""
    result = None
    user_input = input(prompt)    

    while result is None:
        try:
            result = int(user_input)
        except ValueError:
            print("That wasn't a number, please try again.")
            result = None
            user_input = input(prompt)
    return result