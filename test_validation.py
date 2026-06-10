from utils.validation import validate_name_input
# smoke test
def test_smoke():
    """
    Smoke test.
    Ensures pytest testing framework is functional.
    """

    assert 2+2 == 4

def test_valid_name():
    """
    Tests valid name case.
    """

    valid, message = validate_name_input("Akshar Patel")
    assert valid == True
    assert message == ""

def test_empty_input():
    """
    Tests empty name input (error handling).
    """

    valid, message = validate_name_input("")
    assert valid == False
    assert message == "Name cannot be empty!"

def test_name_with_numbers():
    """
    Tests name input with numbers (error handling).
    """

    valid, message = validate_name_input("Akshar123")
    valid == False
    message == "Name cannot contain numbers!"

def test_name_with_symbols():
    """
    Tests invalid symbols in name.
    """

    valid, message = validate_name_input("akshar@")
    assert valid == False