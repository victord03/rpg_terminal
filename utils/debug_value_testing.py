"""This file is used for tweaking and debugging.
Contains corresponding helper functions."""

from classes.Character import Character


def check_xp_values(char: Character, number_of_levels: int) -> dict:
    """For a given number of levels of a character, returns all
    values required for each consecutive Character level up.
    Used for tweaking."""

    dict_of_values = {}

    i = 1
    for level in range(1, number_of_levels + 1):

        char.set_xp_bar()
        xp_needed_to_next_level = char.xp_bar

        dict_of_values[i] = char.xp_bar

        char.xp += xp_needed_to_next_level

        if char.is_ready_to_level_up():
            char.level_up()

        i += 1

    return dict_of_values


def display_xp_values(values_dict: dict):
    """Given a 'values_dict' which is provided by the 'check_xp_values'
    debug function, displays all the values stored in the dict."""

    for key, value in values_dict.items():
        print(f"Level {key}: {value} EXP")


def check_xp_yield_values(
    char: Character, number_of_levels: int, level_dict=None
) -> None:
    """For a given number of levels of a character, displays the
    xp_yield values for all tiers."""

    for level in range(1, number_of_levels + 1):

        if isinstance(level_dict, dict):
            print(
                f"Level: {level} (XP needed for next level: {list(level_dict.values())[level - 1]})"
            )
        else:
            print(f"Level: {level}")

        for tier in range(1, 4):

            char.tier = tier

            char.set_xp_yield()

            print(f"\tTier {tier}: {char.xp_yield}")

        char.level += 1
