"""
Quiz score tests.
"""

from models.quiz import calculate_percentage

# smoke test
def test_smoke():
    """
    Smoke test.
    Ensures pytest testing framework is functional.
    """

    assert 2+2 == 4

def test_percentage_100():
    """
    Testing full marks.
    """

    assert calculate_percentage(10, 10) == 100

def test_percentage_80():
    """
    Testing 80%.
    """

    assert calculate_percentage(8, 10) == 80

def test_percentage_70():
    """
    Testing 70%.
    """

    assert calculate_percentage(7, 10) == 70

def test_percentage_60():
    """
    Testing 60%.
    """

    assert calculate_percentage(6, 10) == 60

def test_percentage_0():
    """
    Testing no marks.
    """

    assert calculate_percentage(0, 10) == 0