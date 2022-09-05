"""This file holds math functions to be used throughout the project."""


def calc_percentage(value_a, value_b) -> float:
    """Return the percentage of b that a represents."""
    if value_b == 0:
        value_b = 1
    return round((value_a / value_b) * 100, 2)
