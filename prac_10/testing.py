"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    # e.g. repeat_string("hi", 2) -> "hi hi"
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def phrase_to_sentence(phrase):
    """
    Format a phrase as a sentence: starting with a capital and ending with a single full stop.

    >>> phrase_to_sentence('hello')
    'Hello.'
    >>> phrase_to_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> phrase_to_sentence('good morning')
    'Good morning.'
    """
    # Remove leading/trailing spaces
    phrase = phrase.strip()
    if not phrase:
        return ""
    # Capitalise first character, keep the rest as is
    phrase = phrase[0].upper() + phrase[1:]
    # Ensure exactly one full stop at the end
    if phrase.endswith('.'):
        phrase = phrase.rstrip('.') + '.'
    else:
        phrase += '.'
    return phrase


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should now pass
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # write assert statements to show if Car sets the fuel correctly

    # fuel set using the value passed in
    car_with_fuel = Car(fuel=10)
    assert car_with_fuel.fuel == 10, "Car does not set passed-in fuel correctly"

    # fuel set using the default value
    default_fuel_car = Car()
    assert default_fuel_car.fuel == 0, "Car does not set default fuel correctly"


run_tests()

# Run the doctests
doctest.testmod()
