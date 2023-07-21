#!/usr/bin/python3
"""Defines a function that prints someone's name."""


def say_my_name(first_name, last_name=""):
    """Function that prints someone's name.
    Args:
        first_name
        last_name
    Raises:
        TypeError: first_name and last_name must be strings.
    Returns:
        My name is <first name> <last name>
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
