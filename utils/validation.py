"""
Validation functions for user input (name).

The function(s) in this file are pure functions, meaning 
they retuyn the same output for a given input and have no 
side effects.
"""

import re # importing re (regex) library 

def validate_name_input(name):
    """
    Validates the name input.

    Returns:
        tuple(bool, str)
    """

    name = name.strip()

    if not name:
        return False, "Name cannot be empty!"
    elif re.search(r"\d", name):
        return False, "Name cannot contain numbers!"
    elif not re.fullmatch(r"[A-Za-z\s\-]+", name):
        return False, "Name can only contain letters, spaces and dashes!"
    else:
        return True, ""